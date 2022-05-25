ToDO list:

1. Define business model
        
   events: transaction_started, node_added, conflict_occurred

   commands: abort_transaction, validate_block, mine_block, register_node, download_chain
        
   entities: block, transaction, validator, consensus

2. Define project structure
    	Dockerfile
        Makefile
        Readme.md
        docker-compose.yml
        licence.txt
        mypy.ini
        requirements.txt
        python              blockchain
                                __init__.py
                                adapters
                                    __init__.py
                                    orm.py
                                    repository.py
                                bootstrap.py
                                config.py
                                domain
                                    __init__.py
                                    model.py
                                entrypoints
                                    __init__.py
                                    flask_app.py
                                service
                                    __init__.py
                                    services.py
                                setup.py
                            tests
                                conftest.py
                                e2e
                                    test_api.py
                                integration
                                    test_orm.py
                                    test_repository.py
                                pytest.ini
                                unit
                                    test_model
                                    test_services

3. Write down the tests
4. Create flask endpoints
5. Create a bootstrap file
6. Add orm

15. Add methods to non-model classes
16. Dockerize

