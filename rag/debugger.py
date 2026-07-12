from pathlib import Path


def print_debug_info(result):

    debug = result["debug"]

    print("\n" + "=" * 80)
    print("RETRIEVAL DEBUGGER")
    print("=" * 80)

    # -------------------------------------------------------
    # Question
    # -------------------------------------------------------

    print("\nQUESTION")
    print("-" * 80)
    print(debug.get("question", "Not Available"))

    # -------------------------------------------------------
    # Retrieved Documents
    # -------------------------------------------------------

    print(f"\nRetrieved Chunks : {len(debug['docs_with_scores'])}")

    for i, (doc, score) in enumerate(
            debug["docs_with_scores"],
            start=1
    ):

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

        print(f"{'Document':<12}: {source}")
        print(f"{'Page':<12}: {page}")
        print(f"{'Score':<12}: {score:.4f}")

        print("\nChunk Preview:\n")

        preview = doc.page_content[:400]

        print(preview)

        if len(doc.page_content) > 400:
            print("...")

        print("-" * 80)

    # -------------------------------------------------------
    # Prompt
    # -------------------------------------------------------

    print("\n" + "=" * 80)
    print("PROMPT SENT TO LLM")
    print("=" * 80)

    prompt = debug["prompt"]

    for message in prompt.messages:
        print(message.content)

    # -------------------------------------------------------
    # Performance
    # -------------------------------------------------------

    metrics = debug["metrics"]

    print("\n" + "=" * 80)
    print("PERFORMANCE METRICS")
    print("=" * 80)

    print(
        f"{'Retrieval Time':<18}: "
        f"{metrics['retrieval_time']:.4f} sec"
    )

    print(
        f"{'LLM Time':<18}: "
        f"{metrics['llm_time']:.4f} sec"
    )

    print(
        f"{'Total Time':<18}: "
        f"{metrics['total_time']:.4f} sec"
    )

    print("\n" + "=" * 80)
    print("END DEBUG")
    print("=" * 80)