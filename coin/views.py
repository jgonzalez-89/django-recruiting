import os
from rest_framework.views import APIView
from blockfrost import BlockFrostApi, ApiError, ApiUrls
from rest_framework.response import Response
from rest_framework import status

from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")

class HealthCheckView(APIView):
    def get(self, request):
        api = BlockFrostApi(
            project_id=PROJECT_ID,
            base_url=ApiUrls.mainnet.value
        )

        try:
            health = api.health(return_type='json')
            return Response(health, status=status.HTTP_200_OK)
        except ApiError as e:
            return Response({"response": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AddressDetailsView(APIView):
    def get(self, request, address):
        api = BlockFrostApi(
            project_id=PROJECT_ID,
            base_url=ApiUrls.mainnet.value
        )

        try:
            address_details = api.address(address)
            return Response(address_details, status=status.HTTP_200_OK)
        except ApiError as e:
            return Response({"response": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AddressTransactionsView(APIView):
    def get(self, request, address):
        api = BlockFrostApi(
            project_id=PROJECT_ID,
            base_url=ApiUrls.mainnet.value
        )

        try:
            transactions = api.address_transactions(address)
            return Response(transactions, status=status.HTTP_200_OK)
        except ApiError as e:
            return Response({"response": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class TransactionDetailsView(APIView):
    def get(self, request, tx_hash):
        api = BlockFrostApi(
            project_id=PROJECT_ID,
            base_url=ApiUrls.mainnet.value
        )

        try:
            transaction = api.transaction(tx_hash)
            return Response(transaction, status=status.HTTP_200_OK)
        except ApiError as e:
            return Response({"response": str(e)}, status=status.HTTP_400_BAD_REQUEST)
