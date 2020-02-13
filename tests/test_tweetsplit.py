from unittest import TestCase
from tweetsplit.main import Tweetsplit


class TestTweetsplit(TestCase):

    def test_tweetsplit_should_initialized(self):
        tweetsplit = Tweetsplit(text='Hello World.!')
        self.assertIsNotNone(tweetsplit)

    def test_tweetsplit_should_raise_value_error(self):
        from tweetsplit import main
        main.MAX_LEN = 5
        main.TWEET_LIMIT = 4

        with self.assertRaises(ValueError) as err1:
            Tweetsplit(text='Hello World!.')

        with self.assertRaises(ValueError) as err2:
            Tweetsplit(text='')

        with self.assertRaises(ValueError) as err3:
            Tweetsplit(text="Hello")

        self.assertEqual(str(err1.exception), "text lenght exceeds MAX_LEN")
        self.assertEqual(str(err2.exception),
                         "text lenght must be greather than MIN_LEN")
        self.assertEqual(str(err3.exception),
                         "the text must have a dot delimiter(.) " +
                         "and the each parts shouldn't exceeds %i chars" %
                         main.TWEET_LIMIT)

    def test_tweetsplit_retrieve_posts_should_works(self):
        text = """
            Lorem ipsum dolor sit amet, ut eos latine concludaturque,
            modus regione te sit, at mei oratio detraxit.
            Vis id omnium corpora, pri magna efficiendi eu,
            an per voluptua copiosae dignissim.
            Vel docendi urbanitas definiebas in, mei duis option fastidii ut'.
            Vix ea hinc quaestio, at usu sumo regione epicuri.
            Et perfecto moderatius cum!!!
            Alia dicunt laoreet at sed.
            Ad dicat delicata duo.
            Sed at oratio nusquam invidunt,
            causae dolorem ex sit.
            Et audiam dolores sit.
            Has dictas oporteat consetetur ne, vocent corpora hendrerit sea eu.
            Et reque dicat invidunt pri, tation laoreet maiestatis quo in.
            Per ea impetus appellantur. Esse constituto scribentur ut pro.
            Dicant similique in sed, no nemore alterum eum.
            No facer omnes mei, mei postea iriure cu.
            Cu periculis constituam quo,
            laudem inermis his id, posse epicurei et eam.
            Integre cotidieque contentiones ex mea,
            dolor option mei id, te est stet minimum.
            No eos nostrud nonumes principes,
            vel fastidii persecuti conclusionemque ut.
            Ut dolorem iracundia disputationi sed,
            dico facilis prodesset sed ei.
            Eos ut discere vocibus disputando, usu tation primis id.
            Sadipscing referrentur consectetuer pro ad,
            in sit debet accusam conceptam.
            Sit ea clita detracto. Ei semper recusabo indoctum vix,
            eripuit ancillae pro ut.
            Quo dictas phaedrum dissentiet an, mea assum accommodare ne,
            no vix dolor quaestio.
        """
        expected = '14/Quo dictas phaedrum dissentiet an, '
        expected += 'mea assum accommodare ne, no vix dolor quaestio..'
        tweetsplit = Tweetsplit(text=text)
        result = tweetsplit.retrieve_posts()

        self.assertIsNotNone(result)
        self.assertEqual(result[-1], expected)
