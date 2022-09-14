from flask import send_file, Response
from flask_restful import reqparse, abort, Api, Resource
from src.docx_generator.generator_better import generate_learning_goals
from io import BytesIO

class Generator(Resource):
     async def get(self):
        generated_doc = await generate_learning_goals()
        f = BytesIO()
        generated_doc.save(f)
        f.seek(0)

        return send_file(
            f,
            as_attachment=True,
            download_name='generated_learning_goals.docx'
        )
