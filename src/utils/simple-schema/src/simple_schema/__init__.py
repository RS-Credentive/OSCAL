import dataclasses
import pathlib
import xml.parsers.expat
from xml.etree import ElementTree

# Find the metaschema directories (assume a specific directory layout)
BASE_DIR = [
    parent for parent in pathlib.Path(__file__).parents if parent.name == "OSCAL"
].pop()

print(BASE_DIR.name)

METASCHEMA_DIR = BASE_DIR.joinpath("src/metaschema")


@dataclasses.dataclass
class ParsedFile:
    name: str
    path: pathlib.Path
    etree: ElementTree.ElementTree


def main() -> None:
    print(f"reading files in {METASCHEMA_DIR}")

    metaschemas: list[ParsedFile] = []
    for xml_file in METASCHEMA_DIR.glob("*.xml"):
        try:
            metaschemas.append(
                ParsedFile(
                    name=xml_file.name,
                    path=xml_file,
                    etree=ElementTree.ElementTree(),
                )
            )

            print(f"Parsing {xml_file}")
            p.Parse(xml_file.read_text())
        except xml.parsers.expat.ExpatError as err:
            print("Error: ", err)


def external_entity_ref_handler(parser, context) -> int:
    pass


if __name__ == "__main__":
    main()
