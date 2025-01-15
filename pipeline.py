from tfx.orchestration.experimental.interactive.interactive_context import InteractiveContext
from tfx.components import CsvExampleGen, StatisticsGen, SchemaGen, ExampleValidator, Transform, Trainer
from tfx.components import ResolverNode, Evaluator, Pusher
from tfx.proto import pusher_pb2
from tfx.types.standard_artifacts import Model
from tfx.dsl.experimental import latest_blessed_model_resolver
import os

# Inisialisasi InteractiveContext
context = InteractiveContext()

# Path ke data dan output
data_path = os.path.join(os.getcwd(), 'data')
output_path = os.path.join(os.getcwd(), 'output')

# 1. ExampleGen
example_gen = CsvExampleGen(input_base=data_path)
context.run(example_gen)

# 2. StatisticsGen
statistics_gen = StatisticsGen(examples=example_gen.outputs['examples'])
context.run(statistics_gen)

# 3. SchemaGen
schema_gen = SchemaGen(statistics=statistics_gen.outputs['statistics'])
context.run(schema_gen)

# 4. ExampleValidator
example_validator = ExampleValidator(
    statistics=statistics_gen.outputs['statistics'],
    schema=schema_gen.outputs['schema']
)
context.run(example_validator)

# 5. Transform
from tfx_bsl.public import tfxio
from tfx.proto import transform_pb2

def preprocessing_fn(inputs):
    # Fungsi preprocessing untuk Transform
    return inputs

transform = Transform(
    examples=example_gen.outputs['examples'],
    schema=schema_gen.outputs['schema'],
    module_file=os.path.join(os.getcwd(), 'utils.py')  # Tulis fungsi preprocessing di utils.py
)
context.run(transform)

# 6. Trainer
trainer = Trainer(
    module_file=os.path.join(os.getcwd(), 'utils.py'),  # Define model di utils.py
    examples=transform.outputs['transformed_examples'],
    transform_graph=transform.outputs['transform_graph'],
    schema=schema_gen.outputs['schema'],
)
context.run(trainer)

# 7. Resolver
resolver = ResolverNode(
    instance_name='latest_model_resolver',
    resolver_class=latest_blessed_model_resolver.LatestBlessedModelResolver,
    model=trainer.outputs['model']
)
context.run(resolver)

# 8. Evaluator
evaluator = Evaluator(
    examples=example_gen.outputs['examples'],
    model=trainer.outputs['model']
)
context.run(evaluator)

# 9. Pusher
pusher = Pusher(
    model=trainer.outputs['model'],
    model_blessing=evaluator.outputs['blessing'],
    push_destination=pusher_pb2.PushDestination(
        filesystem=pusher_pb2.PushDestination.Filesystem(
            base_directory=os.path.join(output_path, 'serving_model')
        )
    )
)
context.run(pusher)
