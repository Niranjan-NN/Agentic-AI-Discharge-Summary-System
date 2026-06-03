class DocumentSearchTool:

    @staticmethod
    def search(documents, query):

        results = []

        for doc in documents:

            text = doc.get("text", "")

            if query.lower() in text.lower():
                results.append(text[:1000])

        return results