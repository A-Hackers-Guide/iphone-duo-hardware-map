# Symbols: `/usr/lib/swift/libswiftRegexBuilder.dylib`

Symbol table of this image in the iOS 27.2 dyld shared cache (`ipsw dyld macho -n --demangle`). The class-level view is on the [image page](../userland/usr__lib__swift__libswiftRegexBuilder.dylib.md). **[DSC]**

207 public symbols, 246 private symbols, 0 undefined (imported).

## Public (external)

```
0x194571c70  __TEXT,__text  static RegexBuilder.AlternationBuilder.buildExpression<A where A: _StringProcessing.RegexComponent>(A) -> A
0x194571df4  __TEXT,__text  static RegexBuilder.AlternationBuilder.buildPartialBlock<A where A: _StringProcessing.RegexComponent>(first: A) -> RegexBuilder.ChoiceOf<A.RegexOutput>
0x194579008  __TEXT,__text  type metadata accessor for RegexBuilder.AlternationBuilder
0x19457a2b8  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.AlternationBuilder
0x1e38d2be8  __AUTH_CONST,__const  type metadata for RegexBuilder.AlternationBuilder
0x194577500  __TEXT,__text  static RegexBuilder.RegexComponentBuilder.buildBlock() -> _StringProcessing.Regex<Swift.Substring>
0x194571ca0  __TEXT,__text  static RegexBuilder.RegexComponentBuilder.buildExpression<A where A: _StringProcessing.RegexComponent>(A) -> A
0x1945731ac  __TEXT,__text  static RegexBuilder.RegexComponentBuilder.buildPartialBlock<A where A: _StringProcessing.RegexComponent>(first: A) -> _StringProcessing.Regex<A.RegexOutput>
0x194577698  __TEXT,__text  type metadata accessor for RegexBuilder.RegexComponentBuilder
0x19457a178  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.RegexComponentBuilder
0x1e38d2b68  __AUTH_CONST,__const  type metadata for RegexBuilder.RegexComponentBuilder
0x194578b80  __TEXT,__text  RegexBuilder.Optionally.regex.modify : _StringProcessing.Regex<A>
0x194571de8  __TEXT,__text  RegexBuilder.Optionally.regex.getter : _StringProcessing.Regex<A>
0x194579a8c  __TEXT,__const  property descriptor for RegexBuilder.Optionally.regex : _StringProcessing.Regex<A>
0x194578b7c  __TEXT,__text  RegexBuilder.Optionally.regex.setter : _StringProcessing.Regex<A>
0x194572f34  __TEXT,__text  type metadata accessor for RegexBuilder.Optionally
0x19457a258  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.Optionally
0x194571cd0  __TEXT,__text  RegexBuilder.Optionally.init(_StringProcessing.Regex<A>) -> RegexBuilder.Optionally<A>
0x194579894  __TEXT,__const  protocol conformance descriptor for RegexBuilder.Optionally<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194578c00  __TEXT,__text  RegexBuilder.TryCapture.regex.modify : _StringProcessing.Regex<A>
0x1945793f0  __TEXT,__text  RegexBuilder.TryCapture.regex.getter : _StringProcessing.Regex<A>
0x194579aac  __TEXT,__const  property descriptor for RegexBuilder.TryCapture.regex : _StringProcessing.Regex<A>
0x1945793f4  __TEXT,__text  RegexBuilder.TryCapture.regex.setter : _StringProcessing.Regex<A>
0x194579090  __TEXT,__text  type metadata accessor for RegexBuilder.TryCapture
0x19457a334  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.TryCapture
0x1945793bc  __TEXT,__text  RegexBuilder.TryCapture.init(_StringProcessing.Regex<A>) -> RegexBuilder.TryCapture<A>
0x1945799c4  __TEXT,__const  protocol conformance descriptor for RegexBuilder.TryCapture<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194578b5c  __TEXT,__text  RegexBuilder.ZeroOrMore.regex.modify : _StringProcessing.Regex<A>
0x1945793d0  __TEXT,__text  RegexBuilder.ZeroOrMore.regex.getter : _StringProcessing.Regex<A>
0x194579a84  __TEXT,__const  property descriptor for RegexBuilder.ZeroOrMore.regex : _StringProcessing.Regex<A>
0x1945793d4  __TEXT,__text  RegexBuilder.ZeroOrMore.regex.setter : _StringProcessing.Regex<A>
0x194578f88  __TEXT,__text  type metadata accessor for RegexBuilder.ZeroOrMore
0x19457a228  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.ZeroOrMore
0x1945731a4  __TEXT,__text  RegexBuilder.ZeroOrMore.init(_StringProcessing.Regex<A>) -> RegexBuilder.ZeroOrMore<A>
0x194579848  __TEXT,__const  protocol conformance descriptor for RegexBuilder.ZeroOrMore<A> : _StringProcessing.RegexComponent in RegexBuilder
0x1945731a8  __TEXT,__text  RegexBuilder.makeFactory() -> _StringProcessing._RegexFactory
0x194575018  __TEXT,__text  RegexBuilder.CharacterClass.subtracting(RegexBuilder.CharacterClass) -> RegexBuilder.CharacterClass
0x19457500c  __TEXT,__text  RegexBuilder.CharacterClass.intersection(RegexBuilder.CharacterClass) -> RegexBuilder.CharacterClass
0x194574148  __TEXT,__text  static RegexBuilder.CharacterClass.generalCategory(Swift.Unicode.GeneralCategory) -> RegexBuilder.CharacterClass
0x194579458  __TEXT,__const  protocol conformance descriptor for RegexBuilder.CharacterClass : _StringProcessing.RegexComponent in RegexBuilder
0x19457529c  __TEXT,__text  RegexBuilder.CharacterClass.symmetricDifference(RegexBuilder.CharacterClass) -> RegexBuilder.CharacterClass
0x194573450  __TEXT,__text  RegexBuilder.CharacterClass.regex.getter : _StringProcessing.Regex<Swift.Substring>
0x194579488  __TEXT,__const  property descriptor for RegexBuilder.CharacterClass.regex : _StringProcessing.Regex<Swift.Substring>
0x194574da0  __TEXT,__text  RegexBuilder.CharacterClass.union(RegexBuilder.CharacterClass) -> RegexBuilder.CharacterClass
0x194573588  __TEXT,__text  RegexBuilder.CharacterClass.inverted.getter : RegexBuilder.CharacterClass
0x194579488  __TEXT,__const  property descriptor for RegexBuilder.CharacterClass.inverted : RegexBuilder.CharacterClass
0x194572028  __TEXT,__text  type metadata accessor for RegexBuilder.CharacterClass
0x19457a0b8  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.CharacterClass
0x1ee3a1c80  __DATA_DIRTY,__data  type metadata for RegexBuilder.CharacterClass
0x194576a84  __TEXT,__text  RegexBuilder.NegativeLookahead.regex.modify : _StringProcessing.Regex<A>
0x194576a24  __TEXT,__text  RegexBuilder.NegativeLookahead.regex.getter : _StringProcessing.Regex<A>
0x194579594  __TEXT,__const  property descriptor for RegexBuilder.NegativeLookahead.regex : _StringProcessing.Regex<A>
0x194576a28  __TEXT,__text  RegexBuilder.NegativeLookahead.regex.setter : _StringProcessing.Regex<A>
0x194577304  __TEXT,__text  type metadata accessor for RegexBuilder.NegativeLookahead
0x19457a12c  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.NegativeLookahead
0x194576aa8  __TEXT,__text  RegexBuilder.NegativeLookahead.init<A where A == A1.RegexOutput, A1: _StringProcessing.RegexComponent>(A1) -> RegexBuilder.NegativeLookahead<A>
0x194576c68  __TEXT,__text  RegexBuilder.NegativeLookahead.init<A where A == A1.RegexOutput, A1: _StringProcessing.RegexComponent>(() -> A1) -> RegexBuilder.NegativeLookahead<A>
0x194579558  __TEXT,__const  protocol conformance descriptor for RegexBuilder.NegativeLookahead<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194578b1c  __TEXT,__text  RegexBuilder.One.regex.modify : _StringProcessing.Regex<A>
0x1945793c8  __TEXT,__text  RegexBuilder.One.regex.getter : _StringProcessing.Regex<A>
0x194579a74  __TEXT,__const  property descriptor for RegexBuilder.One.regex : _StringProcessing.Regex<A>
0x1945793cc  __TEXT,__text  RegexBuilder.One.regex.setter : _StringProcessing.Regex<A>
0x194572f7c  __TEXT,__text  type metadata accessor for RegexBuilder.One
0x19457a1c8  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.One
0x194571eec  __TEXT,__text  RegexBuilder.One.init<A where A == A1.RegexOutput, A1: _StringProcessing.RegexComponent>(A1) -> RegexBuilder.One<A>
0x1945797b0  __TEXT,__const  protocol conformance descriptor for RegexBuilder.One<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194574294  __TEXT,__text  RegexBuilder.... infix(Swift.Character, Swift.Character) -> RegexBuilder.CharacterClass
0x1945745bc  __TEXT,__text  RegexBuilder.... infix(Swift.Unicode.Scalar, Swift.Unicode.Scalar) -> RegexBuilder.CharacterClass
0x194578c20  __TEXT,__text  RegexBuilder.Local.regex.modify : _StringProcessing.Regex<A>
0x1945793f8  __TEXT,__text  RegexBuilder.Local.regex.getter : _StringProcessing.Regex<A>
0x194579ab4  __TEXT,__const  property descriptor for RegexBuilder.Local.regex : _StringProcessing.Regex<A>
0x1945793fc  __TEXT,__text  RegexBuilder.Local.regex.setter : _StringProcessing.Regex<A>
0x1945790d0  __TEXT,__text  type metadata accessor for RegexBuilder.Local
0x19457a364  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.Local
0x1945793b8  __TEXT,__text  RegexBuilder.Local.init(_StringProcessing.Regex<A>) -> RegexBuilder.Local<A>
0x194579a10  __TEXT,__const  protocol conformance descriptor for RegexBuilder.Local<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194576990  __TEXT,__text  static RegexBuilder.Anchor.startOfLine.getter : RegexBuilder.Anchor
0x194579588  __TEXT,__const  property descriptor for static RegexBuilder.Anchor.startOfLine : RegexBuilder.Anchor
0x19457696c  __TEXT,__text  static RegexBuilder.Anchor.endOfSubject.getter : RegexBuilder.Anchor
0x194579588  __TEXT,__const  property descriptor for static RegexBuilder.Anchor.endOfSubject : RegexBuilder.Anchor
0x1945769a8  __TEXT,__text  static RegexBuilder.Anchor.wordBoundary.getter : RegexBuilder.Anchor
0x194579588  __TEXT,__const  property descriptor for static RegexBuilder.Anchor.wordBoundary : RegexBuilder.Anchor
0x194576958  __TEXT,__text  static RegexBuilder.Anchor.startOfSubject.getter : RegexBuilder.Anchor
0x194579588  __TEXT,__const  property descriptor for static RegexBuilder.Anchor.startOfSubject : RegexBuilder.Anchor
0x1945794c0  __TEXT,__const  protocol conformance descriptor for RegexBuilder.Anchor : _StringProcessing.RegexComponent in RegexBuilder
0x194576984  __TEXT,__text  static RegexBuilder.Anchor.textSegmentBoundary.getter : RegexBuilder.Anchor
0x194579588  __TEXT,__const  property descriptor for static RegexBuilder.Anchor.textSegmentBoundary : RegexBuilder.Anchor
0x194576960  __TEXT,__text  static RegexBuilder.Anchor.endOfSubjectBeforeNewline.getter : RegexBuilder.Anchor
0x194579588  __TEXT,__const  property descriptor for static RegexBuilder.Anchor.endOfSubjectBeforeNewline : RegexBuilder.Anchor
0x194576978  __TEXT,__text  static RegexBuilder.Anchor.firstMatchingPositionInSubject.getter : RegexBuilder.Anchor
0x194579588  __TEXT,__const  property descriptor for static RegexBuilder.Anchor.firstMatchingPositionInSubject : RegexBuilder.Anchor
0x1945766f8  __TEXT,__text  RegexBuilder.Anchor.regex.getter : _StringProcessing.Regex<Swift.Substring>
0x194579588  __TEXT,__const  property descriptor for RegexBuilder.Anchor.regex : _StringProcessing.Regex<Swift.Substring>
0x1945769b4  __TEXT,__text  RegexBuilder.Anchor.inverted.getter : RegexBuilder.Anchor
0x194579588  __TEXT,__const  property descriptor for RegexBuilder.Anchor.inverted : RegexBuilder.Anchor
0x19457699c  __TEXT,__text  static RegexBuilder.Anchor.endOfLine.getter : RegexBuilder.Anchor
0x194579588  __TEXT,__const  property descriptor for static RegexBuilder.Anchor.endOfLine : RegexBuilder.Anchor
0x194577054  __TEXT,__text  type metadata accessor for RegexBuilder.Anchor
0x19457a0e0  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.Anchor
0x1e38d27a8  __AUTH_CONST,__const  type metadata for RegexBuilder.Anchor
0x194578ba0  __TEXT,__text  RegexBuilder.Repeat.regex.modify : _StringProcessing.Regex<A>
0x1945793d8  __TEXT,__text  RegexBuilder.Repeat.regex.getter : _StringProcessing.Regex<A>
0x194579a94  __TEXT,__const  property descriptor for RegexBuilder.Repeat.regex : _StringProcessing.Regex<A>
0x1945793dc  __TEXT,__text  RegexBuilder.Repeat.regex.setter : _StringProcessing.Regex<A>
0x194578ff0  __TEXT,__text  type metadata accessor for RegexBuilder.Repeat
0x19457a288  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.Repeat
0x194571cd4  __TEXT,__text  RegexBuilder.Repeat.init(_StringProcessing.Regex<A>) -> RegexBuilder.Repeat<A>
0x1945798e0  __TEXT,__const  protocol conformance descriptor for RegexBuilder.Repeat<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194578be0  __TEXT,__text  RegexBuilder.Capture.regex.modify : _StringProcessing.Regex<A>
0x1945793e8  __TEXT,__text  RegexBuilder.Capture.regex.getter : _StringProcessing.Regex<A>
0x194579aa4  __TEXT,__const  property descriptor for RegexBuilder.Capture.regex : _StringProcessing.Regex<A>
0x1945793ec  __TEXT,__text  RegexBuilder.Capture.regex.setter : _StringProcessing.Regex<A>
0x194572f08  __TEXT,__text  type metadata accessor for RegexBuilder.Capture
0x19457a304  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.Capture
0x194572f94  __TEXT,__text  RegexBuilder.Capture.init(_StringProcessing.Regex<A>) -> RegexBuilder.Capture<A>
0x194579978  __TEXT,__const  protocol conformance descriptor for RegexBuilder.Capture<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194578bc0  __TEXT,__text  RegexBuilder.ChoiceOf.regex.modify : _StringProcessing.Regex<A>
0x1945793e0  __TEXT,__text  RegexBuilder.ChoiceOf.regex.getter : _StringProcessing.Regex<A>
0x194579a9c  __TEXT,__const  property descriptor for RegexBuilder.ChoiceOf.regex : _StringProcessing.Regex<A>
0x1945793e4  __TEXT,__text  RegexBuilder.ChoiceOf.regex.setter : _StringProcessing.Regex<A>
0x194572f64  __TEXT,__text  type metadata accessor for RegexBuilder.ChoiceOf
0x19457a2d4  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.ChoiceOf
0x194571ddc  __TEXT,__text  RegexBuilder.ChoiceOf.init(_StringProcessing.Regex<A>) -> RegexBuilder.ChoiceOf<A>
0x194571c48  __TEXT,__text  RegexBuilder.ChoiceOf.init(() -> RegexBuilder.ChoiceOf<A>) -> RegexBuilder.ChoiceOf<A>
0x19457992c  __TEXT,__const  protocol conformance descriptor for RegexBuilder.ChoiceOf<A> : _StringProcessing.RegexComponent in RegexBuilder
0x1945769d0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A>
0x1945774e0  __TEXT,__text  RegexBuilder.Lookahead.regex.getter : _StringProcessing.Regex<A>
0x19457958c  __TEXT,__const  property descriptor for RegexBuilder.Lookahead.regex : _StringProcessing.Regex<A>
0x1945774e4  __TEXT,__text  RegexBuilder.Lookahead.regex.setter : _StringProcessing.Regex<A>
0x19457708c  __TEXT,__text  type metadata accessor for RegexBuilder.Lookahead
0x19457a0fc  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.Lookahead
0x1945769f4  __TEXT,__text  RegexBuilder.Lookahead.init<A where A == A1.RegexOutput, A1: _StringProcessing.RegexComponent>(A1) -> RegexBuilder.Lookahead<A>
0x194576a0c  __TEXT,__text  RegexBuilder.Lookahead.init<A where A == A1.RegexOutput, A1: _StringProcessing.RegexComponent>(() -> A1) -> RegexBuilder.Lookahead<A>
0x19457950c  __TEXT,__const  protocol conformance descriptor for RegexBuilder.Lookahead<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194578b3c  __TEXT,__text  RegexBuilder.OneOrMore.regex.modify : _StringProcessing.Regex<A>
0x1945793c0  __TEXT,__text  RegexBuilder.OneOrMore.regex.getter : _StringProcessing.Regex<A>
0x194579a7c  __TEXT,__const  property descriptor for RegexBuilder.OneOrMore.regex : _StringProcessing.Regex<A>
0x1945793c4  __TEXT,__text  RegexBuilder.OneOrMore.regex.setter : _StringProcessing.Regex<A>
0x194572074  __TEXT,__text  type metadata accessor for RegexBuilder.OneOrMore
0x19457a1f8  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.OneOrMore
0x194572ef8  __TEXT,__text  RegexBuilder.OneOrMore.init(_StringProcessing.Regex<A>) -> RegexBuilder.OneOrMore<A>
0x1945797fc  __TEXT,__const  protocol conformance descriptor for RegexBuilder.OneOrMore<A> : _StringProcessing.RegexComponent in RegexBuilder
0x1945786f4  __TEXT,__text  RegexBuilder.Reference._raw.getter : Swift.Int
0x194579a70  __TEXT,__const  property descriptor for RegexBuilder.Reference._raw : Swift.Int
0x194578c44  __TEXT,__text  RegexBuilder.Reference.regex.getter : _StringProcessing.Regex<A>
0x194579a70  __TEXT,__const  property descriptor for RegexBuilder.Reference.regex : _StringProcessing.Regex<A>
0x1945793a0  __TEXT,__text  type metadata accessor for RegexBuilder.Reference
0x19457a394  __TEXT,__constg_swiftt  nominal type descriptor for RegexBuilder.Reference
0x194578c40  __TEXT,__text  RegexBuilder.Reference.init(A.Type) -> RegexBuilder.Reference<A>
0x194579a40  __TEXT,__const  protocol conformance descriptor for RegexBuilder.Reference<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194574048  __TEXT,__text  static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.whitespace.getter : RegexBuilder.CharacterClass
0x194579488  __TEXT,__const  property descriptor for static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.whitespace : RegexBuilder.CharacterClass
0x194573a54  __TEXT,__text  static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.anyNonNewline.getter : RegexBuilder.CharacterClass
0x194579488  __TEXT,__const  property descriptor for static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.anyNonNewline : RegexBuilder.CharacterClass
0x194574060  __TEXT,__text  static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.newlineSequence.getter : RegexBuilder.CharacterClass
0x194579488  __TEXT,__const  property descriptor for static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.newlineSequence : RegexBuilder.CharacterClass
0x194573c98  __TEXT,__text  static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.anyGraphemeCluster.getter : RegexBuilder.CharacterClass
0x194579488  __TEXT,__const  property descriptor for static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.anyGraphemeCluster : RegexBuilder.CharacterClass
0x19457406c  __TEXT,__text  static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.verticalWhitespace.getter : RegexBuilder.CharacterClass
0x194579488  __TEXT,__const  property descriptor for static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.verticalWhitespace : RegexBuilder.CharacterClass
0x194574054  __TEXT,__text  static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.horizontalWhitespace.getter : RegexBuilder.CharacterClass
0x194579488  __TEXT,__const  property descriptor for static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.horizontalWhitespace : RegexBuilder.CharacterClass
0x194573a48  __TEXT,__text  static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.any.getter : RegexBuilder.CharacterClass
0x194579488  __TEXT,__const  property descriptor for static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.any : RegexBuilder.CharacterClass
0x194573198  __TEXT,__text  static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.word.getter : RegexBuilder.CharacterClass
0x194579488  __TEXT,__const  property descriptor for static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.word : RegexBuilder.CharacterClass
0x194572f4c  __TEXT,__text  static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.anyOf<A where A1: Swift.Sequence, A1.Element == Swift.Character>(A1) -> RegexBuilder.CharacterClass
0x194574078  __TEXT,__text  static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.anyOf<A where A1: Swift.Sequence, A1.Element == Swift.Unicode.Scalar>(A1) -> RegexBuilder.CharacterClass
0x194572efc  __TEXT,__text  static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.digit.getter : RegexBuilder.CharacterClass
0x194579488  __TEXT,__const  property descriptor for static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.digit : RegexBuilder.CharacterClass
0x194573ca4  __TEXT,__text  static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.hexDigit.getter : RegexBuilder.CharacterClass
0x194579488  __TEXT,__const  property descriptor for static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.hexDigit : RegexBuilder.CharacterClass
0x1945748c8  __TEXT,__text  (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.init(RegexBuilder.CharacterClass, RegexBuilder.CharacterClass...) -> RegexBuilder.CharacterClass
0x194571b78  __TEXT,__text  (extension in RegexBuilder):_StringProcessing.Regex.init<A where A == A1.RegexOutput, A1: _StringProcessing.RegexComponent>(() -> A1) -> _StringProcessing.Regex<A>
0x194578d18  __TEXT,__text  (extension in RegexBuilder):_StringProcessing.Regex.Match.subscript.getter : <A>(RegexBuilder.Reference<A1>) -> A1
0x194579a70  __TEXT,__const  property descriptor for (extension in RegexBuilder):_StringProcessing.Regex.Match.subscript<A>(RegexBuilder.Reference<A1>) -> A1
0x1945787c0  __TEXT,__text  (extension in RegexBuilder):Swift.Character.regex.getter : _StringProcessing.Regex<Swift.Substring>
0x194579a70  __TEXT,__const  property descriptor for (extension in RegexBuilder):Swift.Character.regex : _StringProcessing.Regex<Swift.Substring>
0x194579748  __TEXT,__const  protocol conformance descriptor for Swift.Character : _StringProcessing.RegexComponent in RegexBuilder
0x194577d08  __TEXT,__text  (extension in RegexBuilder):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: () -> B1) -> _StringProcessing.Regex<A1>.Match?
0x1945777f0  __TEXT,__text  (extension in RegexBuilder):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstRange<A where A1: _StringProcessing.RegexComponent>(of: () -> A1) -> Swift.Range<Swift.String.Index>?
0x1945776a8  __TEXT,__text  (extension in RegexBuilder):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.wholeMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: () -> B1) -> _StringProcessing.Regex<A1>.Match?
0x1945776c0  __TEXT,__text  (extension in RegexBuilder):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.prefixMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: () -> B1) -> _StringProcessing.Regex<A1>.Match?
0x194577c00  __TEXT,__text  (extension in RegexBuilder):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.trimmingPrefix<A where A1: _StringProcessing.RegexComponent>(() -> A1) -> Swift.Substring
0x1945779e0  __TEXT,__text  (extension in RegexBuilder):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.split<A where A1: _StringProcessing.RegexComponent>(maxSplits: Swift.Int, omittingEmptySubsequences: Swift.Bool, separator: () -> A1) -> [Swift.Substring]
0x1945778f0  __TEXT,__text  (extension in RegexBuilder):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.ranges<A where A1: _StringProcessing.RegexComponent>(of: () -> A1) -> [Swift.Range<Swift.String.Index>]
0x194577ae8  __TEXT,__text  (extension in RegexBuilder):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.starts<A where A1: _StringProcessing.RegexComponent>(with: () -> A1) -> Swift.Bool
0x194577e08  __TEXT,__text  (extension in RegexBuilder):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.matches<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: () -> B1) -> [_StringProcessing.Regex<A1>.Match]
0x1945777d8  __TEXT,__text  (extension in RegexBuilder):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.contains<A where A1: _StringProcessing.RegexComponent>(() -> A1) -> Swift.Bool
0x1945786f8  __TEXT,__text  (extension in RegexBuilder):Swift.String.regex.getter : _StringProcessing.Regex<Swift.Substring>
0x194579a70  __TEXT,__const  property descriptor for (extension in RegexBuilder):Swift.String.regex : _StringProcessing.Regex<Swift.Substring>
0x1945796e0  __TEXT,__const  protocol conformance descriptor for Swift.String : _StringProcessing.RegexComponent in RegexBuilder
0x194577f08  __TEXT,__text  (extension in RegexBuilder):Swift.RangeReplaceableCollection< where A: Swift.BidirectionalCollection, A.Swift.Collection.SubSequence == Swift.Substring>.trimPrefix<A where A1: _StringProcessing.RegexComponent>(() -> A1) -> ()
0x1945785bc  __TEXT,__text  (extension in RegexBuilder):Swift.RangeReplaceableCollection< where A: Swift.BidirectionalCollection, A.Swift.Collection.SubSequence == Swift.Substring>.replace<A, B, C where A1 == C1.RegexOutput, B1: Swift.Collection, C1: _StringProcessing.RegexComponent, B1.Element == Swift.Character>(maxReplaceme
0x194578240  __TEXT,__text  (extension in RegexBuilder):Swift.RangeReplaceableCollection< where A: Swift.BidirectionalCollection, A.Swift.Collection.SubSequence == Swift.Substring>.replace<A, B where A1: Swift.Collection, B1: _StringProcessing.RegexComponent, A1.Element == Swift.Character>(with: A1, maxReplacements: Swift.Int,
0x194578488  __TEXT,__text  (extension in RegexBuilder):Swift.RangeReplaceableCollection< where A: Swift.BidirectionalCollection, A.Swift.Collection.SubSequence == Swift.Substring>.replacing<A, B, C where A1 == C1.RegexOutput, B1: Swift.Collection, C1: _StringProcessing.RegexComponent, B1.Element == Swift.Character>(maxReplace
0x19457812c  __TEXT,__text  (extension in RegexBuilder):Swift.RangeReplaceableCollection< where A: Swift.BidirectionalCollection, A.Swift.Collection.SubSequence == Swift.Substring>.replacing<A, B where A1: Swift.Collection, B1: _StringProcessing.RegexComponent, A1.Element == Swift.Character>(with: A1, maxReplacements: Swift.In
0x194578000  __TEXT,__text  (extension in RegexBuilder):Swift.RangeReplaceableCollection< where A: Swift.BidirectionalCollection, A.Swift.Collection.SubSequence == Swift.Substring>.replacing<A, B where A1: Swift.Collection, B1: _StringProcessing.RegexComponent, A1.Element == Swift.Character>(with: A1, subrange: Swift.Range<Swi
0x19457834c  __TEXT,__text  (extension in RegexBuilder):Swift.RangeReplaceableCollection< where A: Swift.BidirectionalCollection, A.Swift.Collection.SubSequence == Swift.Substring>.replacing<A, B, C where A1 == C1.RegexOutput, B1: Swift.Collection, C1: _StringProcessing.RegexComponent, B1.Element == Swift.Character>(subrange: 
0x194578748  __TEXT,__text  (extension in RegexBuilder):Swift.Substring.regex.getter : _StringProcessing.Regex<Swift.Substring>
0x194579a70  __TEXT,__const  property descriptor for (extension in RegexBuilder):Swift.Substring.regex : _StringProcessing.Regex<Swift.Substring>
0x194579714  __TEXT,__const  protocol conformance descriptor for Swift.Substring : _StringProcessing.RegexComponent in RegexBuilder
0x194572ca0  __TEXT,__text  (extension in RegexBuilder):Swift.StringProtocol< where A.SubSequence == Swift.Substring>.split(separator: Swift.String, maxSplits: Swift.Int, omittingEmptySubsequences: Swift.Bool) -> [Swift.Substring]
0x1945786f0  __TEXT,__text  (extension in RegexBuilder):Swift.StringProtocol< where A.SubSequence == Swift.Substring>.split(separator: Swift.Substring, maxSplits: Swift.Int, omittingEmptySubsequences: Swift.Bool) -> [Swift.Substring]
0x194578974  __TEXT,__text  (extension in RegexBuilder):Swift.Unicode.Scalar.regex.getter : _StringProcessing.Regex<Swift.Substring>
0x194579a70  __TEXT,__const  property descriptor for (extension in RegexBuilder):Swift.Unicode.Scalar.regex : _StringProcessing.Regex<Swift.Substring>
0x19457977c  __TEXT,__const  protocol conformance descriptor for Swift.Unicode.Scalar : _StringProcessing.RegexComponent in RegexBuilder
```

## Private

```
0x194571cd8  __TEXT,__text  merged RegexBuilder.Lookahead.init(_StringProcessing.Regex<A>) -> RegexBuilder.Lookahead<A>
0x194571cd8  __TEXT,__text  merged RegexBuilder.Lookahead.init(_StringProcessing.Regex<A>) -> RegexBuilder.Lookahead<A>
0x194571d30  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance Swift.String : _StringProcessing.RegexComponent in RegexBuilder
0x194571d7c  __TEXT,__text  initializeWithCopy value witness for RegexBuilder.Lookahead
0x194571d7c  __TEXT,__text  initializeWithCopy value witness for RegexBuilder.Lookahead
0x194571d7c  __TEXT,__text  initializeWithCopy value witness for RegexBuilder.Lookahead
0x194571d7c  __TEXT,__text  initializeWithCopy value witness for RegexBuilder.Lookahead
0x194571d7c  __TEXT,__text  initializeWithCopy value witness for RegexBuilder.Lookahead
0x194571d7c  __TEXT,__text  initializeWithCopy value witness for RegexBuilder.Lookahead
0x194571d7c  __TEXT,__text  initializeWithCopy value witness for RegexBuilder.Lookahead
0x194571d7c  __TEXT,__text  initializeWithCopy value witness for RegexBuilder.Lookahead
0x194571d7c  __TEXT,__text  initializeWithCopy value witness for RegexBuilder.Lookahead
0x194571d7c  __TEXT,__text  initializeWithCopy value witness for RegexBuilder.Lookahead
0x194571d7c  __TEXT,__text  initializeWithCopy value witness for RegexBuilder.Lookahead
0x194571d84  __TEXT,__text  merged RegexBuilder.Lookahead.regex.getter : _StringProcessing.Regex<A>
0x194571d84  __TEXT,__text  merged RegexBuilder.Lookahead.regex.getter : _StringProcessing.Regex<A>
0x194571de0  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.OneOrMore<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194571de0  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.OneOrMore<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194571de0  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.OneOrMore<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194571de0  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.OneOrMore<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194571de0  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.OneOrMore<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194571de0  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.OneOrMore<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194571de0  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.OneOrMore<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194571de0  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.OneOrMore<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194571de0  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.OneOrMore<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194571dec  __TEXT,__text  destroy value witness for RegexBuilder.Lookahead
0x194571dec  __TEXT,__text  destroy value witness for RegexBuilder.Lookahead
0x194571dec  __TEXT,__text  destroy value witness for RegexBuilder.Lookahead
0x194571dec  __TEXT,__text  destroy value witness for RegexBuilder.Lookahead
0x194571dec  __TEXT,__text  destroy value witness for RegexBuilder.Lookahead
0x194571dec  __TEXT,__text  destroy value witness for RegexBuilder.Lookahead
0x194571dec  __TEXT,__text  destroy value witness for RegexBuilder.Lookahead
0x194571dec  __TEXT,__text  destroy value witness for RegexBuilder.Lookahead
0x194571dec  __TEXT,__text  destroy value witness for RegexBuilder.Lookahead
0x194571dec  __TEXT,__text  destroy value witness for RegexBuilder.Lookahead
0x194571dec  __TEXT,__text  destroy value witness for RegexBuilder.Lookahead
0x194571f44  __TEXT,__text  merged destroy value witness for RegexBuilder.Lookahead
0x194571f44  __TEXT,__text  merged destroy value witness for RegexBuilder.Lookahead
0x194571f98  __TEXT,__text  merged initializeWithCopy value witness for RegexBuilder.Lookahead
0x194571f98  __TEXT,__text  merged initializeWithCopy value witness for RegexBuilder.Lookahead
0x194571ff8  __TEXT,__text  ___swift_instantiateGenericMetadata
0x19457208c  __TEXT,__text  type metadata completion function for RegexBuilder.CharacterClass
0x19457212c  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree.Atom.CharacterClass?
0x194572184  __TEXT,__text  (extension in Swift):Swift.Sequence.map<A, B where B1: Swift.Error>((A.Element) throws(B1) -> A1) throws(B1) -> [A1]
0x1945727c4  __TEXT,__text  merged static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.anyGraphemeCluster.getter : RegexBuilder.CharacterClass
0x194572a38  __TEXT,__text  destroy value witness for RegexBuilder.CharacterClass
0x194572b14  __TEXT,__text  merged outlined destroy of _StringProcessing.DSLTree.Atom.CharacterClass?
0x194572b6c  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.CharacterClass : _StringProcessing.RegexComponent in RegexBuilder
0x194572ca4  __TEXT,__text  merged static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.anyOf<A where A1: Swift.Sequence, A1.Element == Swift.Character>(A1) -> RegexBuilder.CharacterClass
0x194572e38  __TEXT,__text  closure #1 (Swift.Character) -> _StringProcessing.DSLTree.CustomCharacterClass.Member in static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.anyOf<A where A1: Swift.Sequence, A1.Element == Swift.Character>(A1) -> RegexBuilder.CharacterClass
0x194572f20  __TEXT,__text  type metadata completion function for RegexBuilder.Lookahead
0x194572f20  __TEXT,__text  type metadata completion function for RegexBuilder.Lookahead
0x194572f20  __TEXT,__text  type metadata completion function for RegexBuilder.Lookahead
0x194572f20  __TEXT,__text  type metadata completion function for RegexBuilder.Lookahead
0x194572f20  __TEXT,__text  type metadata completion function for RegexBuilder.Lookahead
0x194572f20  __TEXT,__text  type metadata completion function for RegexBuilder.Lookahead
0x194572f20  __TEXT,__text  type metadata completion function for RegexBuilder.Lookahead
0x194572f20  __TEXT,__text  type metadata completion function for RegexBuilder.Lookahead
0x194572f20  __TEXT,__text  type metadata completion function for RegexBuilder.Lookahead
0x194572f20  __TEXT,__text  type metadata completion function for RegexBuilder.Lookahead
0x194572f20  __TEXT,__text  type metadata completion function for RegexBuilder.Lookahead
0x194572f28  __TEXT,__text  type metadata instantiation function for RegexBuilder.Lookahead
0x194572f28  __TEXT,__text  type metadata instantiation function for RegexBuilder.Lookahead
0x194572f28  __TEXT,__text  type metadata instantiation function for RegexBuilder.Lookahead
0x194572f28  __TEXT,__text  type metadata instantiation function for RegexBuilder.Lookahead
0x194572f28  __TEXT,__text  type metadata instantiation function for RegexBuilder.Lookahead
0x194572f28  __TEXT,__text  type metadata instantiation function for RegexBuilder.Lookahead
0x194572f28  __TEXT,__text  type metadata instantiation function for RegexBuilder.Lookahead
0x194572f28  __TEXT,__text  type metadata instantiation function for RegexBuilder.Lookahead
0x194572f28  __TEXT,__text  type metadata instantiation function for RegexBuilder.Lookahead
0x194572f28  __TEXT,__text  type metadata instantiation function for RegexBuilder.Lookahead
0x194572f28  __TEXT,__text  type metadata instantiation function for RegexBuilder.Lookahead
0x194572f28  __TEXT,__text  type metadata instantiation function for RegexBuilder.Lookahead
0x194572f98  __TEXT,__text  ___swift_instantiateConcreteTypeFromMangledNameV2
0x194572fec  __TEXT,__text  merged type metadata completion function for RegexBuilder.Lookahead
0x194572fec  __TEXT,__text  merged type metadata completion function for RegexBuilder.Lookahead
0x194573068  __TEXT,__text  initializeWithCopy value witness for RegexBuilder.CharacterClass
0x194573a60  __TEXT,__text  merged static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.any.getter : RegexBuilder.CharacterClass
0x194574090  __TEXT,__text  closure #1 (Swift.Unicode.Scalar) -> _StringProcessing.DSLTree.CustomCharacterClass.Member in static (extension in RegexBuilder):_StringProcessing.RegexComponent< where A == RegexBuilder.CharacterClass>.anyOf<A where A1: Swift.Sequence, A1.Element == Swift.Unicode.Scalar>(A1) -> RegexBuilder.Charact
0x194574d44  __TEXT,__text  outlined init with copy of RegexBuilder.CharacterClass
0x194575024  __TEXT,__text  merged RegexBuilder.CharacterClass.intersection(RegexBuilder.CharacterClass) -> RegexBuilder.CharacterClass
0x1945752a8  __TEXT,__text  generic specialization <_StringProcessing.DSLTree.CustomCharacterClass.Member> of Swift.ContiguousArray._createNewBuffer(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> ()
0x1945752c8  __TEXT,__text  generic specialization <_StringProcessing.DSLTree.CustomCharacterClass.Member> of Swift._ContiguousArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ContiguousArrayBuffer<A>
0x19457546c  __TEXT,__text  generic specialization <RegexBuilder.CharacterClass, [RegexBuilder.CharacterClass]> of Swift.Array.append<A where A == A1.Element, A1: Swift.Sequence>(contentsOf: __owned A1) -> ()
0x194575588  __TEXT,__text  generic specialization <RegexBuilder.CharacterClass, Swift.CollectionOfOne<RegexBuilder.CharacterClass>> of Swift.Array.append<A where A == A1.Element, A1: Swift.Sequence>(contentsOf: __owned A1) -> ()
0x1945759e4  __TEXT,__text  generic specialization <RegexBuilder.CharacterClass> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x194575b8c  __TEXT,__text  outlined init with copy of Swift.CollectionOfOne<RegexBuilder.CharacterClass>
0x194575bf4  __TEXT,__text  outlined destroy of RegexBuilder.CharacterClass
0x194575c48  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for RegexBuilder.CharacterClass
0x194575db0  __TEXT,__text  assignWithCopy value witness for RegexBuilder.CharacterClass
0x194575f44  __TEXT,__text  initializeWithTake value witness for RegexBuilder.CharacterClass
0x194576074  __TEXT,__text  assignWithTake value witness for RegexBuilder.CharacterClass
0x194576208  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.CharacterClass
0x19457621c  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.CharacterClass
0x194576230  __TEXT,__text  __swift_stdlib_malloc_size
0x194576234  __TEXT,__text  generic specialization <Swift.CollectionOfOne<RegexBuilder.CharacterClass>> of (extension in Swift):Swift.Sequence._copySequenceContents(initializing: Swift.UnsafeMutableBufferPointer<A.Element>) -> (A.Iterator, Swift.Int)
0x194576508  __TEXT,__text  outlined init with take of RegexBuilder.CharacterClass
0x194576564  __TEXT,__text  outlined assign with take of RegexBuilder.CharacterClass?
0x1945765cc  __TEXT,__text  merged outlined init with take of RegexBuilder.CharacterClass?
0x19457662c  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance RegexBuilder.Anchor.Kind : Swift.Equatable in RegexBuilder
0x194576640  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance RegexBuilder.Anchor.Kind : Swift.Hashable in RegexBuilder
0x194576688  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance RegexBuilder.Anchor.Kind : Swift.Hashable in RegexBuilder
0x1945766b4  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance RegexBuilder.Anchor.Kind : Swift.Hashable in RegexBuilder
0x194576954  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.Anchor : _StringProcessing.RegexComponent in RegexBuilder
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x1945769f0  __TEXT,__text  RegexBuilder.Lookahead.regex.modify : _StringProcessing.Regex<A> with unmangled suffix ".resume.0"
0x194576a2c  __TEXT,__text  merged RegexBuilder.Lookahead.regex.setter : _StringProcessing.Regex<A>
0x194576a2c  __TEXT,__text  merged RegexBuilder.Lookahead.regex.setter : _StringProcessing.Regex<A>
0x194576aa4  __TEXT,__text  RegexBuilder.NegativeLookahead.init(_StringProcessing.Regex<A>) -> RegexBuilder.NegativeLookahead<A>
0x194576ac0  __TEXT,__text  merged RegexBuilder.Lookahead.init<A where A == A1.RegexOutput, A1: _StringProcessing.RegexComponent>(A1) -> RegexBuilder.Lookahead<A>
0x194576c80  __TEXT,__text  merged RegexBuilder.Lookahead.init<A where A == A1.RegexOutput, A1: _StringProcessing.RegexComponent>(() -> A1) -> RegexBuilder.Lookahead<A>
0x194576e80  __TEXT,__text  instantiation function for generic protocol witness table for RegexBuilder.Lookahead<A> : RegexBuilder._BuiltinRegexComponent in RegexBuilder
0x194576ebc  __TEXT,__text  instantiation function for generic protocol witness table for RegexBuilder.NegativeLookahead<A> : RegexBuilder._BuiltinRegexComponent in RegexBuilder
0x194576ef8  __TEXT,__text  ___swift_memcpy2_1
0x194576f04  __TEXT,__text  ___swift_noop_void_return
0x194576f08  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.Anchor
0x194576fa8  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.Anchor
0x194577064  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.Lookahead
0x194577078  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.Lookahead
0x1945770a4  __TEXT,__text  merged initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Lookahead
0x1945770a4  __TEXT,__text  merged initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Lookahead
0x194577100  __TEXT,__text  merged assignWithCopy value witness for RegexBuilder.Lookahead
0x194577100  __TEXT,__text  merged assignWithCopy value witness for RegexBuilder.Lookahead
0x194577160  __TEXT,__text  merged initializeWithTake value witness for RegexBuilder.Lookahead
0x194577160  __TEXT,__text  merged initializeWithTake value witness for RegexBuilder.Lookahead
0x1945771c0  __TEXT,__text  merged assignWithTake value witness for RegexBuilder.Lookahead
0x1945771c0  __TEXT,__text  merged assignWithTake value witness for RegexBuilder.Lookahead
0x194577220  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.NegativeLookahead
0x194577234  __TEXT,__text  ___swift_get_extra_inhabitant_indexTm
0x194577290  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.NegativeLookahead
0x1945772a4  __TEXT,__text  ___swift_store_extra_inhabitant_indexTm
0x19457731c  __TEXT,__text  ___swift_memcpy1_1
0x194577328  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.Anchor.Kind
0x1945773b8  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.Anchor.Kind
0x194577468  __TEXT,__text  getEnumTag value witness for RegexBuilder.Anchor.Kind
0x194577470  __TEXT,__text  destructiveInjectEnumTag value witness for RegexBuilder.Anchor.Kind
0x194577478  __TEXT,__text  type metadata accessor for RegexBuilder.Anchor.Kind
0x194577488  __TEXT,__text  base witness table accessor for Swift.Equatable in RegexBuilder.Anchor.Kind : Swift.Hashable in RegexBuilder
0x19457748c  __TEXT,__text  lazy protocol witness table accessor for type RegexBuilder.Anchor.Kind and conformance RegexBuilder.Anchor.Kind : Swift.Equatable in RegexBuilder
0x1945774e8  __TEXT,__text  RegexBuilder.Lookahead.init(_StringProcessing.Regex<A>) -> RegexBuilder.Lookahead<A>
0x1945774ec  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Lookahead
0x1945774ec  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Lookahead
0x1945774ec  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Lookahead
0x1945774ec  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Lookahead
0x1945774ec  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Lookahead
0x1945774ec  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Lookahead
0x1945774ec  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Lookahead
0x1945774ec  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Lookahead
0x1945774ec  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Lookahead
0x1945774ec  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Lookahead
0x1945774ec  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Lookahead
0x1945774f0  __TEXT,__text  assignWithCopy value witness for RegexBuilder.Lookahead
0x1945774f0  __TEXT,__text  assignWithCopy value witness for RegexBuilder.Lookahead
0x1945774f0  __TEXT,__text  assignWithCopy value witness for RegexBuilder.Lookahead
0x1945774f0  __TEXT,__text  assignWithCopy value witness for RegexBuilder.Lookahead
0x1945774f0  __TEXT,__text  assignWithCopy value witness for RegexBuilder.Lookahead
0x1945774f0  __TEXT,__text  assignWithCopy value witness for RegexBuilder.Lookahead
0x1945774f0  __TEXT,__text  assignWithCopy value witness for RegexBuilder.Lookahead
0x1945774f0  __TEXT,__text  assignWithCopy value witness for RegexBuilder.Lookahead
0x1945774f0  __TEXT,__text  assignWithCopy value witness for RegexBuilder.Lookahead
0x1945774f0  __TEXT,__text  assignWithCopy value witness for RegexBuilder.Lookahead
0x1945774f0  __TEXT,__text  assignWithCopy value witness for RegexBuilder.Lookahead
0x1945774f4  __TEXT,__text  initializeWithTake value witness for RegexBuilder.Lookahead
0x1945774f4  __TEXT,__text  initializeWithTake value witness for RegexBuilder.Lookahead
0x1945774f4  __TEXT,__text  initializeWithTake value witness for RegexBuilder.Lookahead
0x1945774f4  __TEXT,__text  initializeWithTake value witness for RegexBuilder.Lookahead
0x1945774f4  __TEXT,__text  initializeWithTake value witness for RegexBuilder.Lookahead
0x1945774f4  __TEXT,__text  initializeWithTake value witness for RegexBuilder.Lookahead
0x1945774f4  __TEXT,__text  initializeWithTake value witness for RegexBuilder.Lookahead
0x1945774f4  __TEXT,__text  initializeWithTake value witness for RegexBuilder.Lookahead
0x1945774f4  __TEXT,__text  initializeWithTake value witness for RegexBuilder.Lookahead
0x1945774f4  __TEXT,__text  initializeWithTake value witness for RegexBuilder.Lookahead
0x1945774f4  __TEXT,__text  initializeWithTake value witness for RegexBuilder.Lookahead
0x1945774f8  __TEXT,__text  assignWithTake value witness for RegexBuilder.Lookahead
0x1945774f8  __TEXT,__text  assignWithTake value witness for RegexBuilder.Lookahead
0x1945774f8  __TEXT,__text  assignWithTake value witness for RegexBuilder.Lookahead
0x1945774f8  __TEXT,__text  assignWithTake value witness for RegexBuilder.Lookahead
0x1945774f8  __TEXT,__text  assignWithTake value witness for RegexBuilder.Lookahead
0x1945774f8  __TEXT,__text  assignWithTake value witness for RegexBuilder.Lookahead
0x1945774f8  __TEXT,__text  assignWithTake value witness for RegexBuilder.Lookahead
0x1945774f8  __TEXT,__text  assignWithTake value witness for RegexBuilder.Lookahead
0x1945774f8  __TEXT,__text  assignWithTake value witness for RegexBuilder.Lookahead
0x1945774f8  __TEXT,__text  assignWithTake value witness for RegexBuilder.Lookahead
0x1945774f8  __TEXT,__text  assignWithTake value witness for RegexBuilder.Lookahead
0x1945774fc  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.Lookahead<A> : _StringProcessing.RegexComponent in RegexBuilder
0x1945774fc  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.Lookahead<A> : _StringProcessing.RegexComponent in RegexBuilder
0x1945775c0  __TEXT,__text  ___swift_memcpy0_1
0x1945775c4  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.RegexComponentBuilder
0x1945775c4  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.RegexComponentBuilder
0x194577614  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.RegexComponentBuilder
0x194577614  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.RegexComponentBuilder
0x194577690  __TEXT,__text  getEnumTag value witness for RegexBuilder.RegexComponentBuilder
0x1945776d8  __TEXT,__text  merged (extension in RegexBuilder):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.wholeMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: () -> B1) -> _StringProcessing.Regex<A1>.Match?
0x194577b00  __TEXT,__text  merged (extension in RegexBuilder):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.contains<A where A1: _StringProcessing.RegexComponent>(() -> A1) -> Swift.Bool
0x19457877c  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance Swift.Substring : _StringProcessing.RegexComponent in RegexBuilder
0x19457889c  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance Swift.Character : _StringProcessing.RegexComponent in RegexBuilder
0x194578a48  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance Swift.Unicode.Scalar : _StringProcessing.RegexComponent in RegexBuilder
0x194578d14  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance RegexBuilder.Reference<A> : _StringProcessing.RegexComponent in RegexBuilder
0x194578d1c  __TEXT,__text  instantiation function for generic protocol witness table for RegexBuilder.OneOrMore<A> : RegexBuilder._BuiltinRegexComponent in RegexBuilder
0x194578d58  __TEXT,__text  instantiation function for generic protocol witness table for RegexBuilder.ZeroOrMore<A> : RegexBuilder._BuiltinRegexComponent in RegexBuilder
0x194578d94  __TEXT,__text  instantiation function for generic protocol witness table for RegexBuilder.Optionally<A> : RegexBuilder._BuiltinRegexComponent in RegexBuilder
0x194578dd0  __TEXT,__text  instantiation function for generic protocol witness table for RegexBuilder.Repeat<A> : RegexBuilder._BuiltinRegexComponent in RegexBuilder
0x194578e0c  __TEXT,__text  instantiation function for generic protocol witness table for RegexBuilder.ChoiceOf<A> : RegexBuilder._BuiltinRegexComponent in RegexBuilder
0x194578e48  __TEXT,__text  instantiation function for generic protocol witness table for RegexBuilder.Capture<A> : RegexBuilder._BuiltinRegexComponent in RegexBuilder
0x194578e84  __TEXT,__text  instantiation function for generic protocol witness table for RegexBuilder.TryCapture<A> : RegexBuilder._BuiltinRegexComponent in RegexBuilder
0x194578ec0  __TEXT,__text  instantiation function for generic protocol witness table for RegexBuilder.Local<A> : RegexBuilder._BuiltinRegexComponent in RegexBuilder
0x194578efc  __TEXT,__text  dispatch thunk of RegexBuilder._BuiltinRegexComponent.init(_StringProcessing.Regex<A.RegexOutput>) -> A
0x194578f10  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.One
0x194578f24  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.One
0x194578f38  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.OneOrMore
0x194578f4c  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.OneOrMore
0x194578f60  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.ZeroOrMore
0x194578f74  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.ZeroOrMore
0x194578fa0  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.Optionally
0x194578fb4  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.Optionally
0x194578fc8  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.Repeat
0x194578fdc  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.Repeat
0x194579018  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.ChoiceOf
0x19457902c  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.ChoiceOf
0x194579040  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.Capture
0x194579054  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.Capture
0x194579068  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.TryCapture
0x19457907c  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.TryCapture
0x1945790a8  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.Local
0x1945790bc  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.Local
0x1945790e8  __TEXT,__text  type metadata completion function for RegexBuilder.Reference
0x194579160  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for RegexBuilder.Reference
0x1945791b8  __TEXT,__text  destroy value witness for RegexBuilder.Reference
0x194579208  __TEXT,__text  initializeWithCopy value witness for RegexBuilder.Reference
0x194579264  __TEXT,__text  assignWithCopy value witness for RegexBuilder.Reference
0x1945792c0  __TEXT,__text  initializeWithTake value witness for RegexBuilder.Reference
0x19457931c  __TEXT,__text  assignWithTake value witness for RegexBuilder.Reference
0x194579378  __TEXT,__text  getEnumTagSinglePayload value witness for RegexBuilder.Reference
0x19457938c  __TEXT,__text  storeEnumTagSinglePayload value witness for RegexBuilder.Reference
```

