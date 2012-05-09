from spec import Spec, eq_, skip, ok_, raises

from invoke.parser import Argument


class Argument_(Spec):
    def may_take_names_list(self):
        names = ('--foo', '-f')
        a = Argument(names=names)
        for name in names:
            eq_(a.answers_to(name), True)

    def may_take_name_arg(self):
        eq_(Argument(name='-b').answers_to('-b'), True)

    @raises(TypeError)
    def must_have_at_least_one_name(self):
        Argument()

    def defaults_to_not_needing_a_value(self):
        eq_(Argument(name='a').needs_value, False)

    def may_specify_value_factory(self):
        eq_(Argument(name='a', value=str).needs_value, True)

    class answers_to:
        def returns_True_if_given_name_matches(self):
            eq_(Argument(names=('--foo',)).answers_to('--foo'), True)

    class needs_value:
        def returns_True_if_this_argument_needs_a_value(self):
            eq_(Argument(name='-b', value=str).needs_value, True)

        def returns_False_if_it_does_not_need_a_value(self):
            eq_(Argument(name='-b', value=None).needs_value, False)
