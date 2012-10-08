import subprocess
from optparse import OptionParser

from piecemaker.base import JigsawPieceClips

def piecemaker():
    parser = OptionParser(usage="%prog --dir path/to/dir --svg path/to/svgfile [options] path/to/image",
            description="cut an image by specifying the clips svg")

    parser.add_option("--dir", "-d",
            action="store",
            type="string",
            help="Set the directory to store the files in.",)
    parser.add_option("--number-of-pieces", "-n",
            action="store",
            type="int",
            help="Target count of pieces. Will be adjusted depending on other criteria",)
    parser.add_option("--svg", "-s",
            action="store",
            type="string",
            help="Set the clips svg file instead of creating jigsaw pieces.",)
    parser.add_option("--minimum-piece-size",
            action="store",
            type="int",
            default=42,
            help="Minimum piece size.  Will change the count of pieces to meet this if not set to 0.",)

    parser.add_option("--maximum-piece-size",
            action="store",
            type="int",
            default=0,
            help="""
            Maximum piece size.  Will scale down the original image to meet
            this requirement if not set to 0.
            """,)
    parser.add_option("--scaled-sizes",
            action="store",
            type="string",
            default="",
            help="List of sizes to scale for",)

    parser.add_option("--just-clips",
            action="store_true",
            type="int",
            default=False,
            help="Only create a clips svg file",)

    parser.add_option("--adjacent",
            action="store_true",
            type="int",
            default=True,
            help="""
            Create the adjacent.json file with list of adjacent pieces for each
            piece.
            """,)

    (options, args) = parser.parse_args()

    #if not args:
    #    parser.error("Must set an image")

    jpc = JigsawPieceClips((1280,960), 20)
    print jpc.svg()

    #mydir = options.dir
    #clips = Clips(svgfile=options.svg,
    #            clips_dir=mydir,
    #            size=(options.width, options.height))

    #scissors = Scissors(clips, args[0], mydir)
    #scissors.cut()
