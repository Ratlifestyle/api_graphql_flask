from flask import Flask

app = Flask(__name__)

from flask import request, jsonify
from api_graphql.queries import resolve_produits, resolve_produit
from ariadne.constants import PLAYGROUND_HTML
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, \
    snake_case_fallback_resolvers, ObjectType

query = ObjectType("Query")
query.set_field("produits", resolve_produits)
query.set_field("produit", resolve_produit)

from api_graphql.mutations import resolve_create_produit

mutations = ObjectType("Mutation")
mutations.set_field("createProduit", resolve_create_produit)

type_defs = load_schema_from_path("api_graphql/produit.graphql")
schema = make_executable_schema(
    type_defs, query, mutations, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code