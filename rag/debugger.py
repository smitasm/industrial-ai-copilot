from pathlib import Path


def print_debug_info(result):

    print("\n" + "=" * 80)
    print("RETRIEVAL DEBUGGER")
    print("=" * 80)

    for i, doc in enumerate(result["docs"], start=1):

        metadata = doc.metadata

        source = Path(
            metadata.get("source", "Unknown")
        ).name

        page = metadata.get(
            "page_label",
            metadata.get("page", "Unknown")
        )

        print(f"\nChunk {i}")
        print("-" * 80)

        print(f"Document : {source}")
        print(f"Page     : {page}")

        print("\nChunk:\n")
        print(doc.page_content)

        print("-" * 80)

    print("\n" + "=" * 80)
    print("ANSWER")
    print("=" * 80)

    print(result["answer"])
    print("-" * 80)