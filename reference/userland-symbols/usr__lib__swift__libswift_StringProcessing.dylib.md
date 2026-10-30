# Symbols: `/usr/lib/swift/libswift_StringProcessing.dylib`

Symbol table of this image in the iOS 27.2 dyld shared cache (`ipsw dyld macho -n --demangle`). The class-level view is on the [image page](../userland/usr__lib__swift__libswift_StringProcessing.dylib.md). **[DSC]**

373 public symbols, 1,990 private symbols, 0 undefined (imported).

## Public (external)

```
0x18de49fa0  __TEXT,__constg_swiftt  associated type descriptor for _StringProcessing.RegexComponent.RegexOutput
0x18de12da0  __TEXT,__text  static _StringProcessing.ReferenceID.== infix(_StringProcessing.ReferenceID, _StringProcessing.ReferenceID) -> Swift.Bool
0x18de12d78  __TEXT,__text  _StringProcessing.ReferenceID._raw.getter : Swift.Int
0x18de46868  __TEXT,__const  property descriptor for _StringProcessing.ReferenceID._raw : Swift.Int
0x18de12db4  __TEXT,__text  _StringProcessing.ReferenceID.hash(into: inout Swift.Hasher) -> ()
0x18de12de0  __TEXT,__text  _StringProcessing.ReferenceID.hashValue.getter : Swift.Int
0x18de46868  __TEXT,__const  property descriptor for _StringProcessing.ReferenceID.hashValue : Swift.Int
0x18de12d80  __TEXT,__text  _StringProcessing.ReferenceID.init() -> _StringProcessing.ReferenceID
0x18de15530  __TEXT,__text  type metadata accessor for _StringProcessing.ReferenceID
0x18de4a1c8  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.ReferenceID
0x1e30d1830  __AUTH_CONST,__const  type metadata for _StringProcessing.ReferenceID
0x18de46800  __TEXT,__const  protocol conformance descriptor for _StringProcessing.ReferenceID : Swift.Hashable in _StringProcessing
0x18de46840  __TEXT,__const  protocol conformance descriptor for _StringProcessing.ReferenceID : Swift.Equatable in _StringProcessing
0x18ddef1f4  __TEXT,__text  _StringProcessing._RegexFactory.accumulate<A, B, C where B: _StringProcessing.RegexComponent, C: _StringProcessing.RegexComponent>(B, C) -> _StringProcessing.Regex<A>
0x18ddf8a14  __TEXT,__text  _StringProcessing._RegexFactory.zeroOrMore<A, B where B: _StringProcessing.RegexComponent>(B, _StringProcessing.RegexRepetitionBehavior?) -> _StringProcessing.Regex<A>
0x18de42994  __TEXT,__text  _StringProcessing._RegexFactory.orderedChoice<A, B where B: _StringProcessing.RegexComponent>(B) -> _StringProcessing.Regex<A>
0x18ddf3db4  __TEXT,__text  _StringProcessing._RegexFactory.characterClass<A>(_StringProcessing.DSLTree.Atom.CharacterClass) -> _StringProcessing.Regex<A>
0x18de42b60  __TEXT,__text  _StringProcessing._RegexFactory.captureOptional<A, B, C, D where D: _StringProcessing.RegexComponent>(D, Swift.Int?, (B) throws -> C?) -> _StringProcessing.Regex<A>
0x18de425f8  __TEXT,__text  _StringProcessing._RegexFactory.symbolicReference<A>(_StringProcessing.ReferenceID) -> _StringProcessing.Regex<A>
0x18de42860  __TEXT,__text  _StringProcessing._RegexFactory.atomicNonCapturing<A, B where B: _StringProcessing.RegexComponent>(B) -> _StringProcessing.Regex<A>
0x18ddf5238  __TEXT,__text  _StringProcessing._RegexFactory.customCharacterClass<A>(_StringProcessing.DSLTree.CustomCharacterClass) -> _StringProcessing.Regex<A>
0x18ddedbb4  __TEXT,__text  _StringProcessing._RegexFactory.accumulateAlternation<A, B, C where B: _StringProcessing.RegexComponent, C: _StringProcessing.RegexComponent>(B, C) -> _StringProcessing.Regex<A>
0x18de4286c  __TEXT,__text  _StringProcessing._RegexFactory.lookaheadNonCapturing<A, B where B: _StringProcessing.RegexComponent>(B) -> _StringProcessing.Regex<A>
0x18ddee0ac  __TEXT,__text  _StringProcessing._RegexFactory.ignoreCapturesInTypedOutput<A where A: _StringProcessing.RegexComponent>(A) -> _StringProcessing.Regex<Swift.Substring>
0x18de42878  __TEXT,__text  _StringProcessing._RegexFactory.negativeLookaheadNonCapturing<A, B where B: _StringProcessing.RegexComponent>(B) -> _StringProcessing.Regex<A>
0x18de4257c  __TEXT,__text  _StringProcessing._RegexFactory.char<A>(Swift.Character) -> _StringProcessing.Regex<A>
0x18de424fc  __TEXT,__text  _StringProcessing._RegexFactory.empty<A>() -> _StringProcessing.Regex<A>
0x18de4250c  __TEXT,__text  _StringProcessing._RegexFactory.scalar<A>(Swift.Unicode.Scalar) -> _StringProcessing.Regex<A>
0x18ddf5190  __TEXT,__text  _StringProcessing._RegexFactory.capture<A, B, C, D where D: _StringProcessing.RegexComponent>(D, Swift.Int?, (B) throws -> C) -> _StringProcessing.Regex<A>
0x18ddf4260  __TEXT,__text  _StringProcessing._RegexFactory.capture<A, B where B: _StringProcessing.RegexComponent>(B) -> _StringProcessing.Regex<A>
0x18de42a6c  __TEXT,__text  _StringProcessing._RegexFactory.capture<A, B where B: _StringProcessing.RegexComponent>(B, Swift.Int) -> _StringProcessing.Regex<A>
0x18de42668  __TEXT,__text  _StringProcessing._RegexFactory.exactly<A, B where B: _StringProcessing.RegexComponent>(Swift.Int, B) -> _StringProcessing.Regex<A>
0x18de424f4  __TEXT,__text  _StringProcessing._RegexFactory.assertion<A>(_StringProcessing.DSLTree.Atom.Assertion) -> _StringProcessing.Regex<A>
0x18ddf51f8  __TEXT,__text  _StringProcessing._RegexFactory.oneOrMore<A, B where B: _StringProcessing.RegexComponent>(B, _StringProcessing.RegexRepetitionBehavior?) -> _StringProcessing.Regex<A>
0x18ddcec48  __TEXT,__text  _StringProcessing._RegexFactory.repeating<A, B where B: _StringProcessing.RegexComponent>(Swift.Range<Swift.Int>, _StringProcessing.RegexRepetitionBehavior?, B) -> _StringProcessing.Regex<A>
0x18ddf43b0  __TEXT,__text  _StringProcessing._RegexFactory.zeroOrOne<A, B where B: _StringProcessing.RegexComponent>(B, _StringProcessing.RegexRepetitionBehavior?) -> _StringProcessing.Regex<A>
0x18de424f0  __TEXT,__text  _StringProcessing._RegexFactory.init() -> _StringProcessing._RegexFactory
0x18ddf4f3c  __TEXT,__text  type metadata accessor for _StringProcessing._RegexFactory
0x18de4ab68  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing._RegexFactory
0x1e30d16b0  __AUTH_CONST,__const  type metadata for _StringProcessing._RegexFactory
0x18de172f4  __TEXT,__text  _StringProcessing.AnyRegexOutput.startIndex.getter : Swift.Int
0x18de46df0  __TEXT,__const  property descriptor for _StringProcessing.AnyRegexOutput.startIndex : Swift.Int
0x18de16fdc  __TEXT,__text  _StringProcessing.AnyRegexOutput.extractValues<A>(as: A.Type) -> A?
0x18de172fc  __TEXT,__text  _StringProcessing.AnyRegexOutput.count.getter : Swift.Int
0x18de46df0  __TEXT,__const  property descriptor for _StringProcessing.AnyRegexOutput.count : Swift.Int
0x18de17308  __TEXT,__text  _StringProcessing.AnyRegexOutput.index(after: Swift.Int) -> Swift.Int
0x18de17318  __TEXT,__text  _StringProcessing.AnyRegexOutput.index(before: Swift.Int) -> Swift.Int
0x18de172c4  __TEXT,__text  _StringProcessing.AnyRegexOutput.Element.name.getter : Swift.String?
0x18de46df0  __TEXT,__const  property descriptor for _StringProcessing.AnyRegexOutput.Element.name : Swift.String?
0x18de16f6c  __TEXT,__text  _StringProcessing.AnyRegexOutput.Element.type.getter : Any.Type
0x18de46df0  __TEXT,__const  property descriptor for _StringProcessing.AnyRegexOutput.Element.type : Any.Type
0x18de16f44  __TEXT,__text  _StringProcessing.AnyRegexOutput.Element.range.getter : Swift.Range<Swift.String.Index>?
0x18de46df0  __TEXT,__const  property descriptor for _StringProcessing.AnyRegexOutput.Element.range : Swift.Range<Swift.String.Index>?
0x18ddf5370  __TEXT,__text  _StringProcessing.AnyRegexOutput.Element.value.getter : Any?
0x18de46df0  __TEXT,__const  property descriptor for _StringProcessing.AnyRegexOutput.Element.value : Any?
0x18de17280  __TEXT,__text  _StringProcessing.AnyRegexOutput.Element.substring.getter : Swift.Substring?
0x18de46df0  __TEXT,__const  property descriptor for _StringProcessing.AnyRegexOutput.Element.substring : Swift.Substring?
0x18ddf5048  __TEXT,__text  type metadata accessor for _StringProcessing.AnyRegexOutput.Element
0x18de4a41c  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.AnyRegexOutput.Element
0x1e30d1568  __AUTH_CONST,__const  type metadata for _StringProcessing.AnyRegexOutput.Element
0x18de18c78  __TEXT,__text  _StringProcessing.AnyRegexOutput.endIndex.getter : Swift.Int
0x18de46df0  __TEXT,__const  property descriptor for _StringProcessing.AnyRegexOutput.endIndex : Swift.Int
0x18ddc9774  __TEXT,__text  type metadata accessor for _StringProcessing.AnyRegexOutput
0x18de4a400  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.AnyRegexOutput
0x1e30d14e0  __AUTH_CONST,__const  type metadata for _StringProcessing.AnyRegexOutput
0x18de46c40  __TEXT,__const  protocol conformance descriptor for _StringProcessing.AnyRegexOutput : Swift.BidirectionalCollection in _StringProcessing
0x18de46d88  __TEXT,__const  protocol conformance descriptor for _StringProcessing.AnyRegexOutput : Swift.Sequence in _StringProcessing
0x18de46bf0  __TEXT,__const  protocol conformance descriptor for _StringProcessing.AnyRegexOutput : Swift.RandomAccessCollection in _StringProcessing
0x18de46ca0  __TEXT,__const  protocol conformance descriptor for _StringProcessing.AnyRegexOutput : Swift.Collection in _StringProcessing
0x18de1768c  __TEXT,__text  _StringProcessing.AnyRegexOutput.subscript.getter : (Swift.String) -> _StringProcessing.AnyRegexOutput.Element?
0x18de46df0  __TEXT,__const  property descriptor for _StringProcessing.AnyRegexOutput.subscript(Swift.String) -> _StringProcessing.AnyRegexOutput.Element?
0x18ddf3628  __TEXT,__text  _StringProcessing.AnyRegexOutput.subscript.getter : (Swift.Int) -> _StringProcessing.AnyRegexOutput.Element
0x18de46df0  __TEXT,__const  property descriptor for _StringProcessing.AnyRegexOutput.subscript(Swift.Int) -> _StringProcessing.AnyRegexOutput.Element
0x18de16fc8  __TEXT,__text  _StringProcessing.AnyRegexOutput.init<A>(_StringProcessing.Regex<A>.Match) -> _StringProcessing.AnyRegexOutput
0x18de49f88  __TEXT,__constg_swiftt  protocol descriptor for _StringProcessing.RegexComponent
0x18ddcec34  __TEXT,__text  dispatch thunk of _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput>
0x18de49fa8  __TEXT,__constg_swiftt  method descriptor for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput>
0x18de49f98  __TEXT,__constg_swiftt  protocol requirements base descriptor for _StringProcessing.RegexComponent
0x18de209d0  __TEXT,__text  static _StringProcessing._CompileOptions.enableMetrics.getter : _StringProcessing._CompileOptions
0x18de47634  __TEXT,__const  property descriptor for static _StringProcessing._CompileOptions.enableMetrics : _StringProcessing._CompileOptions
0x18de209c4  __TEXT,__text  static _StringProcessing._CompileOptions.enableTracing.getter : _StringProcessing._CompileOptions
0x18de47634  __TEXT,__const  property descriptor for static _StringProcessing._CompileOptions.enableTracing : _StringProcessing._CompileOptions
0x18de209b8  __TEXT,__text  static _StringProcessing._CompileOptions.disableOptimizations.getter : _StringProcessing._CompileOptions
0x18de47634  __TEXT,__const  property descriptor for static _StringProcessing._CompileOptions.disableOptimizations : _StringProcessing._CompileOptions
0x18de209dc  __TEXT,__text  static _StringProcessing._CompileOptions.default.getter : _StringProcessing._CompileOptions
0x18de47634  __TEXT,__const  property descriptor for static _StringProcessing._CompileOptions.default : _StringProcessing._CompileOptions
0x18de209b0  __TEXT,__text  _StringProcessing._CompileOptions.init(rawValue: Swift.Int) -> _StringProcessing._CompileOptions
0x18de209a8  __TEXT,__text  _StringProcessing._CompileOptions.rawValue.getter : Swift.Int
0x18de47630  __TEXT,__const  property descriptor for _StringProcessing._CompileOptions.rawValue : Swift.Int
0x18de20cbc  __TEXT,__text  type metadata accessor for _StringProcessing._CompileOptions
0x18de4a598  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing._CompileOptions
0x1e30d0fe0  __AUTH_CONST,__const  type metadata for _StringProcessing._CompileOptions
0x18de475d8  __TEXT,__const  protocol conformance descriptor for _StringProcessing._CompileOptions : Swift.Equatable in _StringProcessing
0x18de475a0  __TEXT,__const  protocol conformance descriptor for _StringProcessing._CompileOptions : Swift.RawRepresentable in _StringProcessing
0x18de474d8  __TEXT,__const  protocol conformance descriptor for _StringProcessing._CompileOptions : Swift.SetAlgebra in _StringProcessing
0x18de47600  __TEXT,__const  protocol conformance descriptor for _StringProcessing._CompileOptions : Swift.ExpressibleByArrayLiteral in _StringProcessing
0x18de474a0  __TEXT,__const  protocol conformance descriptor for _StringProcessing._CompileOptions : Swift.OptionSet in _StringProcessing
0x18de10260  __TEXT,__text  static _StringProcessing.RegexSemanticLevel.unicodeScalar.getter : _StringProcessing.RegexSemanticLevel
0x18de46238  __TEXT,__const  property descriptor for static _StringProcessing.RegexSemanticLevel.unicodeScalar : _StringProcessing.RegexSemanticLevel
0x18de10258  __TEXT,__text  static _StringProcessing.RegexSemanticLevel.graphemeCluster.getter : _StringProcessing.RegexSemanticLevel
0x18de46238  __TEXT,__const  property descriptor for static _StringProcessing.RegexSemanticLevel.graphemeCluster : _StringProcessing.RegexSemanticLevel
0x18de1026c  __TEXT,__text  static _StringProcessing.RegexSemanticLevel.== infix(_StringProcessing.RegexSemanticLevel, _StringProcessing.RegexSemanticLevel) -> Swift.Bool
0x18de10280  __TEXT,__text  _StringProcessing.RegexSemanticLevel.hash(into: inout Swift.Hasher) -> ()
0x18de102ac  __TEXT,__text  _StringProcessing.RegexSemanticLevel.hashValue.getter : Swift.Int
0x18de46238  __TEXT,__const  property descriptor for _StringProcessing.RegexSemanticLevel.hashValue : Swift.Int
0x18de104a8  __TEXT,__text  type metadata accessor for _StringProcessing.RegexSemanticLevel
0x18de49e7c  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.RegexSemanticLevel
0x1e30d0bd0  __AUTH_CONST,__const  type metadata for _StringProcessing.RegexSemanticLevel
0x18de46100  __TEXT,__const  protocol conformance descriptor for _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de46140  __TEXT,__const  protocol conformance descriptor for _StringProcessing.RegexSemanticLevel : Swift.Equatable in _StringProcessing
0x18de2a53c  __TEXT,__text  _StringProcessing.renderAsBuilderDSL(ast: Any, maxTopDownLevels: Swift.Int?, minBottomUpLevels: Swift.Int?) -> Swift.String
0x18de10810  __TEXT,__text  static _StringProcessing.RegexWordBoundaryKind.== infix(_StringProcessing.RegexWordBoundaryKind, _StringProcessing.RegexWordBoundaryKind) -> Swift.Bool
0x18de107e0  __TEXT,__text  _StringProcessing.RegexWordBoundaryKind.hash(into: inout Swift.Hasher) -> ()
0x18de107f4  __TEXT,__text  static _StringProcessing.RegexWordBoundaryKind.simple.getter : _StringProcessing.RegexWordBoundaryKind
0x18de46238  __TEXT,__const  property descriptor for static _StringProcessing.RegexWordBoundaryKind.simple : _StringProcessing.RegexWordBoundaryKind
0x18de107f0  __TEXT,__text  static _StringProcessing.RegexWordBoundaryKind.default.getter : _StringProcessing.RegexWordBoundaryKind
0x18de46238  __TEXT,__const  property descriptor for static _StringProcessing.RegexWordBoundaryKind.default : _StringProcessing.RegexWordBoundaryKind
0x18de10808  __TEXT,__text  _StringProcessing.RegexWordBoundaryKind.hashValue.getter : Swift.Int
0x18de46238  __TEXT,__const  property descriptor for _StringProcessing.RegexWordBoundaryKind.hashValue : Swift.Int
0x18de104b8  __TEXT,__text  type metadata accessor for _StringProcessing.RegexWordBoundaryKind
0x18de49e98  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.RegexWordBoundaryKind
0x1e30d06f8  __AUTH_CONST,__const  type metadata for _StringProcessing.RegexWordBoundaryKind
0x18de46168  __TEXT,__const  protocol conformance descriptor for _StringProcessing.RegexWordBoundaryKind : Swift.Hashable in _StringProcessing
0x18de461a8  __TEXT,__const  protocol conformance descriptor for _StringProcessing.RegexWordBoundaryKind : Swift.Equatable in _StringProcessing
0x18de0ff7c  __TEXT,__text  static _StringProcessing.RegexRepetitionBehavior.possessive.getter : _StringProcessing.RegexRepetitionBehavior
0x18de46238  __TEXT,__const  property descriptor for static _StringProcessing.RegexRepetitionBehavior.possessive : _StringProcessing.RegexRepetitionBehavior
0x18de102b0  __TEXT,__text  _StringProcessing.RegexRepetitionBehavior.dslTreeKind.getter : _StringProcessing.DSLTree._AST.QuantificationKind
0x18de46238  __TEXT,__const  property descriptor for _StringProcessing.RegexRepetitionBehavior.dslTreeKind : _StringProcessing.DSLTree._AST.QuantificationKind
0x18de10814  __TEXT,__text  static _StringProcessing.RegexRepetitionBehavior.== infix(_StringProcessing.RegexRepetitionBehavior, _StringProcessing.RegexRepetitionBehavior) -> Swift.Bool
0x18de107e4  __TEXT,__text  _StringProcessing.RegexRepetitionBehavior.hash(into: inout Swift.Hasher) -> ()
0x18de107f8  __TEXT,__text  static _StringProcessing.RegexRepetitionBehavior.eager.getter : _StringProcessing.RegexRepetitionBehavior
0x18de46238  __TEXT,__const  property descriptor for static _StringProcessing.RegexRepetitionBehavior.eager : _StringProcessing.RegexRepetitionBehavior
0x18de1080c  __TEXT,__text  _StringProcessing.RegexRepetitionBehavior.hashValue.getter : Swift.Int
0x18de46238  __TEXT,__const  property descriptor for _StringProcessing.RegexRepetitionBehavior.hashValue : Swift.Int
0x18de107ec  __TEXT,__text  static _StringProcessing.RegexRepetitionBehavior.reluctant.getter : _StringProcessing.RegexRepetitionBehavior
0x18de46238  __TEXT,__const  property descriptor for static _StringProcessing.RegexRepetitionBehavior.reluctant : _StringProcessing.RegexRepetitionBehavior
0x18ddf4f4c  __TEXT,__text  type metadata accessor for _StringProcessing.RegexRepetitionBehavior
0x18de49eb4  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.RegexRepetitionBehavior
0x1e30d05d8  __AUTH_CONST,__const  type metadata for _StringProcessing.RegexRepetitionBehavior
0x18de461d0  __TEXT,__const  protocol conformance descriptor for _StringProcessing.RegexRepetitionBehavior : Swift.Hashable in _StringProcessing
0x18de46210  __TEXT,__const  protocol conformance descriptor for _StringProcessing.RegexRepetitionBehavior : Swift.Equatable in _StringProcessing
0x18de49f54  __TEXT,__constg_swiftt  protocol descriptor for _StringProcessing.CustomConsumingRegexComponent
0x18de10bf4  __TEXT,__text  dispatch thunk of _StringProcessing.CustomConsumingRegexComponent.consuming(_: Swift.String, startingAt: Swift.String.Index, in: Swift.Range<Swift.String.Index>) throws -> (upperBound: Swift.String.Index, output: A.RegexOutput)?
0x18de49f80  __TEXT,__constg_swiftt  method descriptor for _StringProcessing.CustomConsumingRegexComponent.consuming(_: Swift.String, startingAt: Swift.String.Index, in: Swift.Range<Swift.String.Index>) throws -> (upperBound: Swift.String.Index, output: A.RegexOutput)?
0x18de49f78  __TEXT,__constg_swiftt  base conformance descriptor for _StringProcessing.CustomConsumingRegexComponent: _StringProcessing.RegexComponent
0x18ddefa78  __TEXT,__text  (extension in _StringProcessing):_StringProcessing.CustomConsumingRegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput>
0x18de46460  __TEXT,__const  property descriptor for (extension in _StringProcessing):_StringProcessing.CustomConsumingRegexComponent.regex : _StringProcessing.Regex<A.RegexOutput>
0x18de49f70  __TEXT,__constg_swiftt  protocol requirements base descriptor for _StringProcessing.CustomConsumingRegexComponent
0x18de46620  __TEXT,__const  enum case for _StringProcessing.Regex._RegexInternalAction.addOptions<A>(_StringProcessing.Regex<A>._RegexInternalAction.Type) -> (_StringProcessing._CompileOptions) -> _StringProcessing.Regex<A>._RegexInternalAction
0x18de46624  __TEXT,__const  enum case for _StringProcessing.Regex._RegexInternalAction.recompile<A>(_StringProcessing.Regex<A>._RegexInternalAction.Type) -> _StringProcessing.Regex<A>._RegexInternalAction
0x18de110b8  __TEXT,__text  type metadata accessor for _StringProcessing.Regex._RegexInternalAction
0x18de4a09c  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.Regex._RegexInternalAction
0x18ddcf71c  __TEXT,__text  _StringProcessing.Regex.init(_regexString: Swift.String, version: Swift.Int) -> _StringProcessing.Regex<A>
0x18de10c5c  __TEXT,__text  _StringProcessing.Regex.init(_regexString: Swift.String) -> _StringProcessing.Regex<A>
0x18ddf0664  __TEXT,__text  _StringProcessing.Regex.firstMatch(in: Swift.String) throws -> _StringProcessing.Regex<A>.Match?
0x18ddd4580  __TEXT,__text  _StringProcessing.Regex.firstMatch(in: Swift.Substring) throws -> _StringProcessing.Regex<A>.Match?
0x18ddf51cc  __TEXT,__text  _StringProcessing.Regex.wholeMatch(in: Swift.String) throws -> _StringProcessing.Regex<A>.Match?
0x18ddfda7c  __TEXT,__text  _StringProcessing.Regex.wholeMatch(in: Swift.Substring) throws -> _StringProcessing.Regex<A>.Match?
0x18dded9b0  __TEXT,__text  _StringProcessing.Regex.ignoresCase(Swift.Bool) -> _StringProcessing.Regex<A>
0x18ddfda50  __TEXT,__text  _StringProcessing.Regex.prefixMatch(in: Swift.String) throws -> _StringProcessing.Regex<A>.Match?
0x18dde5b30  __TEXT,__text  _StringProcessing.Regex.prefixMatch(in: Swift.Substring) throws -> _StringProcessing.Regex<A>.Match?
0x18de10ea4  __TEXT,__text  _StringProcessing.Regex._forceAction(_StringProcessing.Regex<A>._RegexInternalAction) -> Swift.Bool
0x18de18d8c  __TEXT,__text  _StringProcessing.Regex._literalPattern.getter : Swift.String?
0x18de47040  __TEXT,__const  property descriptor for _StringProcessing.Regex._literalPattern : Swift.String?
0x18de0fc48  __TEXT,__text  _StringProcessing.Regex.asciiOnlyDigits(Swift.Bool) -> _StringProcessing.Regex<A>
0x18de0fc6c  __TEXT,__text  _StringProcessing.Regex.wordBoundaryKind(_StringProcessing.RegexWordBoundaryKind) -> _StringProcessing.Regex<A>
0x18de0ff88  __TEXT,__text  _StringProcessing.Regex.matchingSemantics(_StringProcessing.RegexSemanticLevel) -> _StringProcessing.Regex<A>
0x18de100cc  __TEXT,__text  _StringProcessing.Regex._nsreCompatibility.getter : _StringProcessing.Regex<A>
0x18de46238  __TEXT,__const  property descriptor for _StringProcessing.Regex._nsreCompatibility : _StringProcessing.Regex<A>
0x18de0fda4  __TEXT,__text  _StringProcessing.Regex.dotMatchesNewlines(Swift.Bool) -> _StringProcessing.Regex<A>
0x18de0fdbc  __TEXT,__text  _StringProcessing.Regex.repetitionBehavior(_StringProcessing.RegexRepetitionBehavior) -> _StringProcessing.Regex<A>
0x18de0fc54  __TEXT,__text  _StringProcessing.Regex.asciiOnlyWhitespace(Swift.Bool) -> _StringProcessing.Regex<A>
0x18de0fdb0  __TEXT,__text  _StringProcessing.Regex.anchorsMatchLineEndings(Swift.Bool) -> _StringProcessing.Regex<A>
0x18de0fc3c  __TEXT,__text  _StringProcessing.Regex.asciiOnlyWordCharacters(Swift.Bool) -> _StringProcessing.Regex<A>
0x18de0fc60  __TEXT,__text  _StringProcessing.Regex.asciiOnlyCharacterClasses(Swift.Bool) -> _StringProcessing.Regex<A>
0x18ddf3038  __TEXT,__text  _StringProcessing.Regex.Match.subscript.getter : <A>(dynamicMember: Swift.KeyPath<A, A1>) -> A1
0x18de4641c  __TEXT,__const  property descriptor for _StringProcessing.Regex.Match.subscript<A>(dynamicMember: Swift.KeyPath<A, A1>) -> A1
0x18ddfd808  __TEXT,__text  _StringProcessing.Regex.Match.subscript.getter : (dynamicMember: Swift.KeyPath<(A, _doNotUse: ()), A>) -> A
0x18de4641c  __TEXT,__const  property descriptor for _StringProcessing.Regex.Match.subscript(dynamicMember: Swift.KeyPath<(A, _doNotUse: ()), A>) -> A
0x18de10818  __TEXT,__text  _StringProcessing.Regex.Match.range.getter : Swift.Range<Swift.String.Index>
0x18de46418  __TEXT,__const  property descriptor for _StringProcessing.Regex.Match.range : Swift.Range<Swift.String.Index>
0x18ddf09a0  __TEXT,__text  _StringProcessing.Regex.Match.output.getter : A
0x18de4641c  __TEXT,__const  property descriptor for _StringProcessing.Regex.Match.output : A
0x18de177f4  __TEXT,__text  (extension in _StringProcessing):_StringProcessing.Regex.Match<A where A == _StringProcessing.AnyRegexOutput>.subscript.getter : (dynamicMember: Swift.KeyPath<(Swift.Substring, _doNotUse: ()), Swift.Substring>) -> Swift.Substring
0x18de46df0  __TEXT,__const  property descriptor for (extension in _StringProcessing):_StringProcessing.Regex.Match<A where A == _StringProcessing.AnyRegexOutput>.subscript(dynamicMember: Swift.KeyPath<(Swift.Substring, _doNotUse: ()), Swift.Substring>) -> Swift.Substring
0x18de17d80  __TEXT,__text  (extension in _StringProcessing):_StringProcessing.Regex.Match<A where A == _StringProcessing.AnyRegexOutput>.init<A>(_StringProcessing.Regex<A1>.Match) -> _StringProcessing.Regex<_StringProcessing.AnyRegexOutput>.Match
0x18de17800  __TEXT,__text  (extension in _StringProcessing):_StringProcessing.Regex.Match<A where A == _StringProcessing.AnyRegexOutput>.subscript.getter : (Swift.String) -> _StringProcessing.AnyRegexOutput.Element?
0x18de46df0  __TEXT,__const  property descriptor for (extension in _StringProcessing):_StringProcessing.Regex.Match<A where A == _StringProcessing.AnyRegexOutput>.subscript(Swift.String) -> _StringProcessing.AnyRegexOutput.Element?
0x18ddc9784  __TEXT,__text  type metadata accessor for _StringProcessing.Regex.Match
0x18de49f24  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.Regex.Match
0x18ddf98a0  __TEXT,__text  _StringProcessing.Regex.Match.subscript.getter : <A>(_StringProcessing.ReferenceID) -> A1
0x18de4641c  __TEXT,__const  property descriptor for _StringProcessing.Regex.Match.subscript<A>(_StringProcessing.ReferenceID) -> A1
0x18ddcedb4  __TEXT,__text  _StringProcessing.Regex.regex.getter : _StringProcessing.Regex<A>
0x18de464cc  __TEXT,__const  property descriptor for _StringProcessing.Regex.regex : _StringProcessing.Regex<A>
0x18ddf8b00  __TEXT,__text  _StringProcessing.Regex.init(quoting: Swift.String) -> _StringProcessing.Regex<A>
0x18de17b34  __TEXT,__text  _StringProcessing.Regex.contains(captureNamed: Swift.String) -> Swift.Bool
0x18ddceb20  __TEXT,__text  _StringProcessing.Regex.init(verbatim: Swift.String) -> _StringProcessing.Regex<A>
0x18de17cf4  __TEXT,__text  (extension in _StringProcessing):_StringProcessing.Regex<A where A == _StringProcessing.AnyRegexOutput>.init<A>(_StringProcessing.Regex<A1>) -> _StringProcessing.Regex<_StringProcessing.AnyRegexOutput>
0x18dde65f8  __TEXT,__text  (extension in _StringProcessing):_StringProcessing.Regex<A where A == _StringProcessing.AnyRegexOutput>.init(Swift.String) throws -> _StringProcessing.Regex<_StringProcessing.AnyRegexOutput>
0x18ddcc9c0  __TEXT,__text  type metadata accessor for _StringProcessing.Regex
0x18de49fb0  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.Regex
0x18de17968  __TEXT,__text  _StringProcessing.Regex.init(_: Swift.String, as: A.Type) throws -> _StringProcessing.Regex<A>
0x18de17d9c  __TEXT,__text  _StringProcessing.Regex.init(_: _StringProcessing.Regex<_StringProcessing.AnyRegexOutput>, as: A.Type) -> _StringProcessing.Regex<A>?
0x18de464b0  __TEXT,__const  protocol conformance descriptor for _StringProcessing.Regex<A> : _StringProcessing.RegexComponent in _StringProcessing
0x18de11e2c  __TEXT,__text  static _StringProcessing.DSLTree.CustomCharacterClass.generalCategory(Swift.Unicode.GeneralCategory) -> _StringProcessing.DSLTree.CustomCharacterClass
0x18de46918  __TEXT,__const  enum case for _StringProcessing.DSLTree.CustomCharacterClass.Member.subtraction(_StringProcessing.DSLTree.CustomCharacterClass.Member.Type) -> (_StringProcessing.DSLTree.CustomCharacterClass, _StringProcessing.DSLTree.CustomCharacterClass) -> _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18de46914  __TEXT,__const  enum case for _StringProcessing.DSLTree.CustomCharacterClass.Member.intersection(_StringProcessing.DSLTree.CustomCharacterClass.Member.Type) -> (_StringProcessing.DSLTree.CustomCharacterClass, _StringProcessing.DSLTree.CustomCharacterClass) -> _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18de4690c  __TEXT,__const  enum case for _StringProcessing.DSLTree.CustomCharacterClass.Member.quotedLiteral(_StringProcessing.DSLTree.CustomCharacterClass.Member.Type) -> (Swift.String) -> _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18de4691c  __TEXT,__const  enum case for _StringProcessing.DSLTree.CustomCharacterClass.Member.symmetricDifference(_StringProcessing.DSLTree.CustomCharacterClass.Member.Type) -> (_StringProcessing.DSLTree.CustomCharacterClass, _StringProcessing.DSLTree.CustomCharacterClass) -> _StringProcessing.DSLTree.CustomCharacterClass.Me
0x18de46900  __TEXT,__const  enum case for _StringProcessing.DSLTree.CustomCharacterClass.Member.atom(_StringProcessing.DSLTree.CustomCharacterClass.Member.Type) -> (_StringProcessing.DSLTree.Atom) -> _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18de46904  __TEXT,__const  enum case for _StringProcessing.DSLTree.CustomCharacterClass.Member.range(_StringProcessing.DSLTree.CustomCharacterClass.Member.Type) -> (_StringProcessing.DSLTree.Atom, _StringProcessing.DSLTree.Atom) -> _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18de46908  __TEXT,__const  enum case for _StringProcessing.DSLTree.CustomCharacterClass.Member.custom(_StringProcessing.DSLTree.CustomCharacterClass.Member.Type) -> (_StringProcessing.DSLTree.CustomCharacterClass) -> _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18de46910  __TEXT,__const  enum case for _StringProcessing.DSLTree.CustomCharacterClass.Member.trivia(_StringProcessing.DSLTree.CustomCharacterClass.Member.Type) -> (Swift.String) -> _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18dde0f50  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18de4a140  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree.CustomCharacterClass.Member
0x1ee063aa0  __DATA_DIRTY,__data  type metadata for _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18de11af8  __TEXT,__text  _StringProcessing.DSLTree.CustomCharacterClass.init(members: [_StringProcessing.DSLTree.CustomCharacterClass.Member], isInverted: Swift.Bool) -> _StringProcessing.DSLTree.CustomCharacterClass
0x18de12770  __TEXT,__text  _StringProcessing.DSLTree.CustomCharacterClass.inverted.getter : _StringProcessing.DSLTree.CustomCharacterClass
0x18de46868  __TEXT,__const  property descriptor for _StringProcessing.DSLTree.CustomCharacterClass.inverted : _StringProcessing.DSLTree.CustomCharacterClass
0x18de13a9c  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree.CustomCharacterClass
0x18de4a124  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree.CustomCharacterClass
0x1e30d01b8  __AUTH_CONST,__const  type metadata for _StringProcessing.DSLTree.CustomCharacterClass
0x18de46974  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.unconverted(_StringProcessing.DSLTree.Atom.Type) -> (_StringProcessing.DSLTree._AST.Atom) -> _StringProcessing.DSLTree.Atom
0x18de4697c  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.anyNonNewline(_StringProcessing.DSLTree.Atom.Type) -> _StringProcessing.DSLTree.Atom
0x18de46968  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.backreference(_StringProcessing.DSLTree.Atom.Type) -> (_StringProcessing.DSLTree._AST.Reference) -> _StringProcessing.DSLTree.Atom
0x18de469e8  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.notNewline(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de469ec  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.whitespace(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de46a04  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.anyGrapheme(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de469f0  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.notWhitespace(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de469e4  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.newlineSequence(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de46a08  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.anyUnicodeScalar(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de469f4  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.verticalWhitespace(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de469dc  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.horizontalWhitespace(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de469f8  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.notVerticalWhitespace(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de469e0  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.notHorizontalWhitespace(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de128a4  __TEXT,__text  static _StringProcessing.DSLTree.Atom.CharacterClass.== infix(_StringProcessing.DSLTree.Atom.CharacterClass, _StringProcessing.DSLTree.Atom.CharacterClass) -> Swift.Bool
0x18de128b8  __TEXT,__text  _StringProcessing.DSLTree.Atom.CharacterClass.hash(into: inout Swift.Hasher) -> ()
0x18de469fc  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.word(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de469d4  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.digit(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de46a00  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.notWord(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de12a08  __TEXT,__text  _StringProcessing.DSLTree.Atom.CharacterClass.inverted.getter : _StringProcessing.DSLTree.Atom.CharacterClass?
0x18de46868  __TEXT,__const  property descriptor for _StringProcessing.DSLTree.Atom.CharacterClass.inverted : _StringProcessing.DSLTree.Atom.CharacterClass?
0x18de469d8  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.CharacterClass.notDigit(_StringProcessing.DSLTree.Atom.CharacterClass.Type) -> _StringProcessing.DSLTree.Atom.CharacterClass
0x18de128e4  __TEXT,__text  _StringProcessing.DSLTree.Atom.CharacterClass.hashValue.getter : Swift.Int
0x18de46868  __TEXT,__const  property descriptor for _StringProcessing.DSLTree.Atom.CharacterClass.hashValue : Swift.Int
0x18ddf57b0  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree.Atom.CharacterClass
0x18de4a1ac  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree.Atom.CharacterClass
0x1e30d0138  __AUTH_CONST,__const  type metadata for _StringProcessing.DSLTree.Atom.CharacterClass
0x18de467c0  __TEXT,__const  protocol conformance descriptor for _StringProcessing.DSLTree.Atom.CharacterClass : Swift.Hashable in _StringProcessing
0x18de46798  __TEXT,__const  protocol conformance descriptor for _StringProcessing.DSLTree.Atom.CharacterClass : Swift.Equatable in _StringProcessing
0x18de46960  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.characterClass(_StringProcessing.DSLTree.Atom.Type) -> (_StringProcessing.DSLTree.Atom.CharacterClass) -> _StringProcessing.DSLTree.Atom
0x18de4696c  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.symbolicReference(_StringProcessing.DSLTree.Atom.Type) -> (_StringProcessing.ReferenceID) -> _StringProcessing.DSLTree.Atom
0x18de46970  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.changeMatchingOptions(_StringProcessing.DSLTree.Atom.Type) -> (_StringProcessing.DSLTree._AST.MatchingOptionSequence) -> _StringProcessing.DSLTree.Atom
0x18de46978  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.any(_StringProcessing.DSLTree.Atom.Type) -> _StringProcessing.DSLTree.Atom
0x18de46980  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.dot(_StringProcessing.DSLTree.Atom.Type) -> _StringProcessing.DSLTree.Atom
0x18de46958  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.char(_StringProcessing.DSLTree.Atom.Type) -> (Swift.Character) -> _StringProcessing.DSLTree.Atom
0x18de4695c  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.scalar(_StringProcessing.DSLTree.Atom.Type) -> (Swift.Unicode.Scalar) -> _StringProcessing.DSLTree.Atom
0x18de469b4  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.Assertion.caretAnchor(_StringProcessing.DSLTree.Atom.Assertion.Type) -> _StringProcessing.DSLTree.Atom.Assertion
0x18de469ac  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.Assertion.startOfLine(_StringProcessing.DSLTree.Atom.Assertion.Type) -> _StringProcessing.DSLTree.Atom.Assertion
0x18de469a4  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.Assertion.textSegment(_StringProcessing.DSLTree.Atom.Assertion.Type) -> _StringProcessing.DSLTree.Atom.Assertion
0x18de469b8  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.Assertion.dollarAnchor(_StringProcessing.DSLTree.Atom.Assertion.Type) -> _StringProcessing.DSLTree.Atom.Assertion
0x18de46998  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.Assertion.endOfSubject(_StringProcessing.DSLTree.Atom.Assertion.Type) -> _StringProcessing.DSLTree.Atom.Assertion
0x18de469bc  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.Assertion.wordBoundary(_StringProcessing.DSLTree.Atom.Assertion.Type) -> _StringProcessing.DSLTree.Atom.Assertion
0x18de469a8  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.Assertion.notTextSegment(_StringProcessing.DSLTree.Atom.Assertion.Type) -> _StringProcessing.DSLTree.Atom.Assertion
0x18de46990  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.Assertion.startOfSubject(_StringProcessing.DSLTree.Atom.Assertion.Type) -> _StringProcessing.DSLTree.Atom.Assertion
0x18de469c0  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.Assertion.notWordBoundary(_StringProcessing.DSLTree.Atom.Assertion.Type) -> _StringProcessing.DSLTree.Atom.Assertion
0x18de4699c  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.Assertion.resetStartOfMatch(_StringProcessing.DSLTree.Atom.Assertion.Type) -> _StringProcessing.DSLTree.Atom.Assertion
0x18de46994  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.Assertion.endOfSubjectBeforeNewline(_StringProcessing.DSLTree.Atom.Assertion.Type) -> _StringProcessing.DSLTree.Atom.Assertion
0x18de469a0  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.Assertion.firstMatchingPositionInSubject(_StringProcessing.DSLTree.Atom.Assertion.Type) -> _StringProcessing.DSLTree.Atom.Assertion
0x18dddc830  __TEXT,__text  _StringProcessing.DSLTree.Atom.Assertion.init(rawValue: Swift.UInt64) -> _StringProcessing.DSLTree.Atom.Assertion?
0x18de12864  __TEXT,__text  _StringProcessing.DSLTree.Atom.Assertion.rawValue.getter : Swift.UInt64
0x18de46868  __TEXT,__const  property descriptor for _StringProcessing.DSLTree.Atom.Assertion.rawValue : Swift.UInt64
0x18de469b0  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.Assertion.endOfLine(_StringProcessing.DSLTree.Atom.Assertion.Type) -> _StringProcessing.DSLTree.Atom.Assertion
0x18de154d8  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree.Atom.Assertion
0x18de4a190  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree.Atom.Assertion
0x1e30d00a0  __AUTH_CONST,__const  type metadata for _StringProcessing.DSLTree.Atom.Assertion
0x18de46758  __TEXT,__const  protocol conformance descriptor for _StringProcessing.DSLTree.Atom.Assertion : Swift.Hashable in _StringProcessing
0x18de466f8  __TEXT,__const  protocol conformance descriptor for _StringProcessing.DSLTree.Atom.Assertion : Swift.Equatable in _StringProcessing
0x18de46720  __TEXT,__const  protocol conformance descriptor for _StringProcessing.DSLTree.Atom.Assertion : Swift.RawRepresentable in _StringProcessing
0x18de46964  __TEXT,__const  enum case for _StringProcessing.DSLTree.Atom.assertion(_StringProcessing.DSLTree.Atom.Type) -> (_StringProcessing.DSLTree.Atom.Assertion) -> _StringProcessing.DSLTree.Atom
0x18ddcc9f0  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree.Atom
0x18de4a168  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree.Atom
0x1ee063a70  __DATA_DIRTY,__data  type metadata for _StringProcessing.DSLTree.Atom
0x18ddf8d44  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree._AST.ConditionKind
0x18de4a228  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree._AST.ConditionKind
0x1ef579988  __AUTH,__data  type metadata for _StringProcessing.DSLTree._AST.ConditionKind
0x18ddf8b64  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree._AST.AbsentFunction
0x18de4a2c8  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree._AST.AbsentFunction
0x1ef579958  __AUTH,__data  type metadata for _StringProcessing.DSLTree._AST.AbsentFunction
0x18de11ad8  __TEXT,__text  static _StringProcessing.DSLTree._AST.QuantificationKind.possessive.getter : _StringProcessing.DSLTree._AST.QuantificationKind
0x18de46868  __TEXT,__const  property descriptor for static _StringProcessing.DSLTree._AST.QuantificationKind.possessive : _StringProcessing.DSLTree._AST.QuantificationKind
0x18de11a98  __TEXT,__text  static _StringProcessing.DSLTree._AST.QuantificationKind.eager.getter : _StringProcessing.DSLTree._AST.QuantificationKind
0x18de46868  __TEXT,__const  property descriptor for static _StringProcessing.DSLTree._AST.QuantificationKind.eager : _StringProcessing.DSLTree._AST.QuantificationKind
0x18de11ab8  __TEXT,__text  static _StringProcessing.DSLTree._AST.QuantificationKind.reluctant.getter : _StringProcessing.DSLTree._AST.QuantificationKind
0x18de46868  __TEXT,__const  property descriptor for static _StringProcessing.DSLTree._AST.QuantificationKind.reluctant : _StringProcessing.DSLTree._AST.QuantificationKind
0x18ddcf804  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree._AST.QuantificationKind
0x18de4a250  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree._AST.QuantificationKind
0x1ef579928  __AUTH,__data  type metadata for _StringProcessing.DSLTree._AST.QuantificationKind
0x18de135b4  __TEXT,__text  static _StringProcessing.DSLTree._AST.QuantificationAmount.zeroOrMore.getter : _StringProcessing.DSLTree._AST.QuantificationAmount
0x18de46868  __TEXT,__const  property descriptor for static _StringProcessing.DSLTree._AST.QuantificationAmount.zeroOrMore : _StringProcessing.DSLTree._AST.QuantificationAmount
0x18de13760  __TEXT,__text  static _StringProcessing.DSLTree._AST.QuantificationAmount.range(Swift.Int, Swift.Int) -> _StringProcessing.DSLTree._AST.QuantificationAmount
0x18de13688  __TEXT,__text  static _StringProcessing.DSLTree._AST.QuantificationAmount.upToN(Swift.Int) -> _StringProcessing.DSLTree._AST.QuantificationAmount
0x18de13670  __TEXT,__text  static _StringProcessing.DSLTree._AST.QuantificationAmount.exactly(Swift.Int) -> _StringProcessing.DSLTree._AST.QuantificationAmount
0x18de1367c  __TEXT,__text  static _StringProcessing.DSLTree._AST.QuantificationAmount.nOrMore(Swift.Int) -> _StringProcessing.DSLTree._AST.QuantificationAmount
0x18de135d4  __TEXT,__text  static _StringProcessing.DSLTree._AST.QuantificationAmount.oneOrMore.getter : _StringProcessing.DSLTree._AST.QuantificationAmount
0x18de46868  __TEXT,__const  property descriptor for static _StringProcessing.DSLTree._AST.QuantificationAmount.oneOrMore : _StringProcessing.DSLTree._AST.QuantificationAmount
0x18de135f4  __TEXT,__text  static _StringProcessing.DSLTree._AST.QuantificationAmount.zeroOrOne.getter : _StringProcessing.DSLTree._AST.QuantificationAmount
0x18de46868  __TEXT,__const  property descriptor for static _StringProcessing.DSLTree._AST.QuantificationAmount.zeroOrOne : _StringProcessing.DSLTree._AST.QuantificationAmount
0x18ddd4ec4  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree._AST.QuantificationAmount
0x18de4a278  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree._AST.QuantificationAmount
0x1ef5798f8  __AUTH,__data  type metadata for _StringProcessing.DSLTree._AST.QuantificationAmount
0x18ddf8d64  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree._AST.MatchingOptionSequence
0x18de4a318  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree._AST.MatchingOptionSequence
0x1ef5798c8  __AUTH,__data  type metadata for _StringProcessing.DSLTree._AST.MatchingOptionSequence
0x18ddf9f6c  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree._AST.Atom
0x18de4a340  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree._AST.Atom
0x1ef579898  __AUTH,__data  type metadata for _StringProcessing.DSLTree._AST.Atom
0x18ddfd9e8  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree._AST.ASTNode
0x18de4a2a0  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree._AST.ASTNode
0x1ef579868  __AUTH,__data  type metadata for _StringProcessing.DSLTree._AST.ASTNode
0x18de13594  __TEXT,__text  static _StringProcessing.DSLTree._AST.GroupKind.negativeLookahead.getter : _StringProcessing.DSLTree._AST.GroupKind
0x18de46868  __TEXT,__const  property descriptor for static _StringProcessing.DSLTree._AST.GroupKind.negativeLookahead : _StringProcessing.DSLTree._AST.GroupKind
0x18de13554  __TEXT,__text  static _StringProcessing.DSLTree._AST.GroupKind.atomicNonCapturing.getter : _StringProcessing.DSLTree._AST.GroupKind
0x18de46868  __TEXT,__const  property descriptor for static _StringProcessing.DSLTree._AST.GroupKind.atomicNonCapturing : _StringProcessing.DSLTree._AST.GroupKind
0x18de13574  __TEXT,__text  static _StringProcessing.DSLTree._AST.GroupKind.lookahead.getter : _StringProcessing.DSLTree._AST.GroupKind
0x18de46868  __TEXT,__const  property descriptor for static _StringProcessing.DSLTree._AST.GroupKind.lookahead : _StringProcessing.DSLTree._AST.GroupKind
0x18ddd4ee4  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree._AST.GroupKind
0x18de4a200  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree._AST.GroupKind
0x1ef579838  __AUTH,__data  type metadata for _StringProcessing.DSLTree._AST.GroupKind
0x18ddfaee0  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree._AST.Reference
0x18de4a2f0  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree._AST.Reference
0x1ef579808  __AUTH,__data  type metadata for _StringProcessing.DSLTree._AST.Reference
0x18de15618  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree._AST
0x18de4a1e4  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree._AST
0x1e30cff70  __AUTH_CONST,__const  type metadata for _StringProcessing.DSLTree._AST
0x18de13978  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree
0x18de4a108  __TEXT,__constg_swiftt  nominal type descriptor for _StringProcessing.DSLTree
0x1e30cfed0  __AUTH_CONST,__const  type metadata for _StringProcessing.DSLTree
0x18de051b0  __TEXT,__text  (extension in _StringProcessing):Swift.BidirectionalCollection< where A.Element: Swift.Comparable>.firstRange<A where A1: Swift.Collection, A.Element == A1.Element>(of: A1) -> Swift.Range<A.Index>?
0x18de046a8  __TEXT,__text  (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de05968  __TEXT,__text  (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstRange<A where A1: _StringProcessing.RegexComponent>(of: A1) -> Swift.Range<Swift.String.Index>?
0x18de10820  __TEXT,__text  (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.wholeMatch<A where A1: _StringProcessing.RegexComponent>(of: A1) -> _StringProcessing.Regex<A1.RegexOutput>.Match?
0x18de1084c  __TEXT,__text  (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.prefixMatch<A where A1: _StringProcessing.RegexComponent>(of: A1) -> _StringProcessing.Regex<A1.RegexOutput>.Match?
0x18de08de8  __TEXT,__text  (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.trimmingPrefix<A where A1: _StringProcessing.RegexComponent>(A1) -> Swift.Substring
0x18ddf2344  __TEXT,__text  (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.split<A where A1: _StringProcessing.RegexComponent>(separator: A1, maxSplits: Swift.Int, omittingEmptySubsequences: Swift.Bool) -> [Swift.Substring]
0x18de09da4  __TEXT,__text  (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.ranges<A where A1: _StringProcessing.RegexComponent>(of: A1) -> [Swift.Range<Swift.String.Index>]
0x18dde59f8  __TEXT,__text  (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.starts<A where A1: _StringProcessing.RegexComponent>(with: A1) -> Swift.Bool
0x18ddf33d8  __TEXT,__text  (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.matches<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> [_StringProcessing.Regex<A1>.Match]
0x18ddd32b8  __TEXT,__text  (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.contains<A where A1: _StringProcessing.RegexComponent>(A1) -> Swift.Bool
0x18de08a94  __TEXT,__text  (extension in _StringProcessing):Swift.Collection< where A == A.SubSequence, A.Element: Swift.Equatable>.trimPrefix<A where A1: Swift.Sequence, A.Element == A1.Element>(A1) -> ()
0x18de08498  __TEXT,__text  (extension in _StringProcessing):Swift.Collection< where A == A.SubSequence>.trimPrefix(while: (A.Element) throws -> Swift.Bool) throws -> ()
0x18ddef51c  __TEXT,__text  (extension in _StringProcessing):Swift.Collection.trimmingPrefix(while: (A.Element) throws -> Swift.Bool) throws -> A.SubSequence
0x18ddfdf20  __TEXT,__text  (extension in _StringProcessing):Swift.Collection< where A.Element: Swift.Equatable>.firstRange<A where A1: Swift.Collection, A.Element == A1.Element>(of: A1) -> Swift.Range<A.Index>?
0x18dde5b5c  __TEXT,__text  (extension in _StringProcessing):Swift.Collection< where A.Element: Swift.Equatable>.trimmingPrefix<A where A1: Swift.Sequence, A.Element == A1.Element>(A1) -> A.SubSequence
0x18ddc97a4  __TEXT,__text  (extension in _StringProcessing):Swift.Collection< where A.Element: Swift.Equatable>.split<A where A1: Swift.Collection, A.Element == A1.Element>(separator: A1, maxSplits: Swift.Int, omittingEmptySubsequences: Swift.Bool) -> [A.SubSequence]
0x18de09330  __TEXT,__text  (extension in _StringProcessing):Swift.Collection< where A.Element: Swift.Equatable>.ranges<A where A1: Swift.Collection, A.Element == A1.Element>(of: A1) -> [Swift.Range<A.Index>]
0x18ddfdaa8  __TEXT,__text  (extension in _StringProcessing):Swift.Collection< where A.Element: Swift.Equatable>.contains<A where A1: Swift.Collection, A.Element == A1.Element>(A1) -> Swift.Bool
0x18de08770  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection.trimPrefix(while: (A.Element) throws -> Swift.Bool) throws -> ()
0x18de08f60  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection< where A: Swift.BidirectionalCollection, A.Swift.Collection.SubSequence == Swift.Substring>.trimPrefix<A where A1: _StringProcessing.RegexComponent>(A1) -> ()
0x18de08c38  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection< where A.Element: Swift.Equatable>.trimPrefix<A where A1: Swift.Sequence, A.Element == A1.Element>(A1) -> ()
0x18ddfaac4  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection< where A.Element: Swift.Equatable>.replace<A, B where A1: Swift.Collection, B1: Swift.Collection, A.Element == A1.Element, A1.Element == B1.Element>(_: A1, with: B1, maxReplacements: Swift.Int) -> ()
0x18ddccb0c  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection< where A.Element: Swift.Equatable>.replacing<A, B where A1: Swift.Collection, B1: Swift.Collection, A.Element == A1.Element, A1.Element == B1.Element>(_: A1, with: B1, maxReplacements: Swift.Int) -> A
0x18ddcce2c  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection< where A.Element: Swift.Equatable>.replacing<A, B where A1: Swift.Collection, B1: Swift.Collection, A.Element == A1.Element, A1.Element == B1.Element>(_: A1, with: B1, subrange: Swift.Range<A.Index>, maxReplacements: Swift.Int) -> A
0x18de04e70  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection< where A.SubSequence == Swift.Substring>.replace<A, B, C where A1 == C1.RegexOutput, B1: Swift.Collection, C1: _StringProcessing.RegexComponent, B1.Element == Swift.Character>(_: C1, maxReplacements: Swift.Int, with: (_StringProcessin
0x18ddefddc  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection< where A.SubSequence == Swift.Substring>.replace<A, B where A1: Swift.Collection, B1: _StringProcessing.RegexComponent, A1.Element == Swift.Character>(_: B1, with: A1, maxReplacements: Swift.Int) -> ()
0x18de04da4  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection< where A.SubSequence == Swift.Substring>.replacing<A, B, C where A1 == C1.RegexOutput, B1: Swift.Collection, C1: _StringProcessing.RegexComponent, B1.Element == Swift.Character>(_: C1, maxReplacements: Swift.Int, with: (_StringProcess
0x18dde18cc  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection< where A.SubSequence == Swift.Substring>.replacing<A, B where A1: Swift.Collection, B1: _StringProcessing.RegexComponent, A1.Element == Swift.Character>(_: B1, with: A1, maxReplacements: Swift.Int) -> A
0x18dde14f4  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection< where A.SubSequence == Swift.Substring>.replacing<A, B where A1: Swift.Collection, B1: _StringProcessing.RegexComponent, A1.Element == Swift.Character>(_: B1, with: A1, subrange: Swift.Range<Swift.String.Index>, maxReplacements: Swif
0x18de047d4  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection< where A.SubSequence == Swift.Substring>.replacing<A, B, C where A1 == C1.RegexOutput, B1: Swift.Collection, C1: _StringProcessing.RegexComponent, B1.Element == Swift.Character>(_: C1, subrange: Swift.Range<Swift.String.Index>, maxRep
0x18de05ac0  __TEXT,__text  (extension in _StringProcessing):Swift.StringProtocol.contains(Swift.String) -> Swift.Bool
0x18de05b30  __TEXT,__text  (extension in _StringProcessing):Swift.StringProtocol.contains(Swift.Substring) -> Swift.Bool
0x18ddc7f18  __TEXT,__text  (extension in _StringProcessing):Swift.StringProtocol< where A.SubSequence == Swift.Substring>._split(separator: Swift.String, maxSplits: Swift.Int, omittingEmptySubsequences: Swift.Bool) -> [Swift.Substring]
0x18de05e34  __TEXT,__text  (extension in _StringProcessing):Swift.StringProtocol< where A.SubSequence == Swift.Substring>._split(separator: Swift.Substring, maxSplits: Swift.Int, omittingEmptySubsequences: Swift.Bool) -> [Swift.Substring]
```

## Private

```
0x18ddc80e4  __TEXT,__text  function signature specialization <Arg[2] = Dead> of _StringProcessing.SubstringSearcher.State.init(text: Swift.Substring?, pattern: Swift.Substring) -> _StringProcessing.SubstringSearcher.State
0x18ddc8420  __TEXT,__text  function signature specialization <Arg[0] = Owned To Guaranteed> of generic specialization <Swift.Character, Swift.Int> of Swift.Dictionary.init(dictionaryLiteral: (A, B)...) -> [A : B]
0x18ddc854c  __TEXT,__text  generic specialization <Swift.Character> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(A) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x18ddc85b8  __TEXT,__text  generic specialization <_StringProcessing.SplitSequence<_StringProcessing.SubstringSearcher>> of Swift._copySequenceToContiguousArray<A where A: Swift.Sequence>(A) -> Swift.ContiguousArray<A.Element>
0x18ddc8f04  __TEXT,__text  ___swift_instantiateConcreteTypeFromMangledNameV2
0x18ddc8f58  __TEXT,__text  generic specialization <Swift.Character> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(_: A, hashValue: Swift.Int) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x18ddc9010  __TEXT,__text  generic specialization <Swift.Character, Swift.Int> of Swift._NativeDictionary._copyOrMoveAndResize(capacity: Swift.Int, moveElements: Swift.Bool) -> ()
0x18ddc9290  __TEXT,__text  outlined init with copy of _StringProcessing.SplitSequence<_StringProcessing.SubstringSearcher>
0x18ddc92f8  __TEXT,__text  merged outlined destroy of _StringProcessing.SplitSequence<_StringProcessing.SubstringSearcher>
0x18ddc92f8  __TEXT,__text  merged outlined destroy of _StringProcessing.SplitSequence<_StringProcessing.SubstringSearcher>
0x18ddc92f8  __TEXT,__text  merged outlined destroy of _StringProcessing.SplitSequence<_StringProcessing.SubstringSearcher>
0x18ddc92f8  __TEXT,__text  merged outlined destroy of _StringProcessing.SplitSequence<_StringProcessing.SubstringSearcher>
0x18ddc92f8  __TEXT,__text  merged outlined destroy of _StringProcessing.SplitSequence<_StringProcessing.SubstringSearcher>
0x18ddc92f8  __TEXT,__text  merged outlined destroy of _StringProcessing.SplitSequence<_StringProcessing.SubstringSearcher>
0x18ddc92f8  __TEXT,__text  merged outlined destroy of _StringProcessing.SplitSequence<_StringProcessing.SubstringSearcher>
0x18ddc9350  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.SplitSequence
0x18ddc944c  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.SubstringSearcher
0x18ddc94d0  __TEXT,__text  destroy value witness for _StringProcessing.SplitSequence
0x18ddc94d0  __TEXT,__text  destroy value witness for _StringProcessing.SplitSequence
0x18ddc9580  __TEXT,__text  destroy value witness for _StringProcessing.SubstringSearcher
0x18ddc95b8  __TEXT,__text  __swift_stdlib_malloc_size
0x18ddc95bc  __TEXT,__text  destroy value witness for _StringProcessing.SplitSequence.Iterator
0x18ddc976c  __TEXT,__text  destroy value witness for _StringProcessing.SubstringSearcher.State
0x18ddc976c  __TEXT,__text  destroy value witness for _StringProcessing.SubstringSearcher.State
0x18ddc976c  __TEXT,__text  destroy value witness for _StringProcessing.SubstringSearcher.State
0x18ddc979c  __TEXT,__text  type metadata instantiation function for _StringProcessing.TypedInt
0x18ddc979c  __TEXT,__text  type metadata instantiation function for _StringProcessing.TypedInt
0x18ddc979c  __TEXT,__text  type metadata instantiation function for _StringProcessing.TypedInt
0x18ddc979c  __TEXT,__text  type metadata instantiation function for _StringProcessing.TypedInt
0x18ddc9f88  __TEXT,__text  type metadata accessor for _StringProcessing.SplitSequence
0x18ddc9fa0  __TEXT,__text  generic specialization <Swift.Substring> of (extension in _StringProcessing):Swift.StringProtocol< where A.SubSequence == Swift.Substring>._split(separator: Swift.String, maxSplits: Swift.Int, omittingEmptySubsequences: Swift.Bool) -> [Swift.Substring]
0x18ddca184  __TEXT,__text  type metadata accessor for _StringProcessing.ZSearcher
0x18ddca19c  __TEXT,__text  _StringProcessing.SubstringSearcher.nextRangeNaive(in: Swift.Substring, searchFromEnd: Swift.String.Index) -> (result: Swift.Range<Swift.String.Index>?, nextEnd: Swift.String.Index?)
0x18ddca548  __TEXT,__text  (extension in _StringProcessing):_RegexParser.AST.Node.convert(into: inout [_StringProcessing.DSLTree.Node]) throws -> ()
0x18ddcc958  __TEXT,__text  merged type metadata accessor for _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18ddcc990  __TEXT,__text  ___swift_instantiateGenericMetadata
0x18ddcc9d8  __TEXT,__text  type metadata accessor for _StringProcessing.Regex.Program
0x18ddcca10  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree.QuantificationKind
0x18ddcca30  __TEXT,__text  type metadata instantiation function for _StringProcessing.SplitSequence
0x18ddcca30  __TEXT,__text  type metadata instantiation function for _StringProcessing.SplitSequence
0x18ddcca30  __TEXT,__text  type metadata instantiation function for _StringProcessing.SplitSequence
0x18ddcca30  __TEXT,__text  type metadata instantiation function for _StringProcessing.SplitSequence
0x18ddcca38  __TEXT,__text  type metadata completion function for _StringProcessing.RangesSequence
0x18ddccaf4  __TEXT,__text  type metadata accessor for _StringProcessing.RangesSequence
0x18ddce448  __TEXT,__text  _StringProcessing.SubstringSearcher.nextRange(in: Swift.Substring, searchFromEnd: Swift.String.Index) -> (result: Swift.Range<Swift.String.Index>?, nextEnd: Swift.String.Index?)
0x18ddce820  __TEXT,__text  (extension in _StringProcessing):Swift.Substring._replacingSubstring(_: Swift.Substring, with: Swift.Substring, maxReplacements: Swift.Int) -> Swift.String
0x18ddcea8c  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.RegexRepetitionBehavior
0x18ddcea8c  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.RegexRepetitionBehavior
0x18ddcea94  __TEXT,__text  _StringProcessing.Regex.init(node: _StringProcessing.DSLTree.Node) -> _StringProcessing.Regex<A>
0x18ddceb84  __TEXT,__text  merged storeEnumTagSinglePayload value witness for _StringProcessing.RegexRepetitionBehavior
0x18ddceb84  __TEXT,__text  merged storeEnumTagSinglePayload value witness for _StringProcessing.RegexRepetitionBehavior
0x18ddced30  __TEXT,__text  type metadata instantiation function for _StringProcessing.Executor.Matches
0x18ddced30  __TEXT,__text  type metadata instantiation function for _StringProcessing.Executor.Matches
0x18ddced30  __TEXT,__text  type metadata instantiation function for _StringProcessing.Executor.Matches
0x18ddced30  __TEXT,__text  type metadata instantiation function for _StringProcessing.Executor.Matches
0x18ddced34  __TEXT,__text  type metadata instantiation function for _StringProcessing.DefaultSearcherState
0x18ddced3c  __TEXT,__text  type metadata instantiation function for _StringProcessing.Regex.Program
0x18ddced3c  __TEXT,__text  type metadata instantiation function for _StringProcessing.Regex.Program
0x18ddced44  __TEXT,__text  type metadata completion function for _StringProcessing.Regex.Program
0x18ddceda0  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree.Node
0x18ddcedb0  __TEXT,__text  protocol witness for _StringProcessing.RegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput> in conformance _StringProcessing.Regex<A> : _StringProcessing.RegexComponent in _StringProcessing
0x18ddcedc0  __TEXT,__text  (extension in _StringProcessing):_RegexParser.AST.Atom.dslTreeAtom.getter : _StringProcessing.DSLTree.Atom
0x18ddcf5b0  __TEXT,__text  _StringProcessing.Regex.Program.init(ast: _RegexParser.AST) -> _StringProcessing.Regex<A>.Program
0x18ddcf824  __TEXT,__text  lazy protocol witness table accessor for type Swift.String and conformance Swift.String : Swift.StringProtocol in Swift
0x18ddcf878  __TEXT,__text  _StringProcessing.Regex.init(ast: _RegexParser.AST) -> _StringProcessing.Regex<A>
0x18ddcf980  __TEXT,__text  generic specialization <_StringProcessing.DSLTree.Node> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddcfa84  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.DSLTree._AST.QuantificationKind
0x18ddcfab0  __TEXT,__text  outlined destroy of _StringProcessing.MEProgram
0x18ddcfb04  __TEXT,__text  outlined init with take of _StringProcessing.MEProgram
0x18ddcfb60  __TEXT,__text  _StringProcessing.Processor.cycle() -> ()
0x18ddd0b14  __TEXT,__text  static _StringProcessing.Executor._run(_StringProcessing.MEProgram, inout _StringProcessing.Processor) throws -> _StringProcessing.Regex<A>.Match?
0x18ddd0c8c  __TEXT,__text  _StringProcessing.MEProgram.Builder.assemble() throws -> _StringProcessing.MEProgram
0x18ddd1224  __TEXT,__text  outlined init with copy of _StringProcessing.MEProgram
0x18ddd1280  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.(_canOnlyMatchAtStartImpl in _B1BA5D5716180164B5D5D7DB68D175B1)(inout Swift.ArraySlice<_StringProcessing.DSLTree.Node>) -> Swift.Bool?
0x18ddd1c20  __TEXT,__text  generic specialization <serialized, Swift.String.UnicodeScalarView> of (extension in Swift):Swift.Collection.first.getter : A.Element?
0x18ddd1e14  __TEXT,__text  Swift._StringGuts.validateScalarIndex(Swift.String.Index) -> Swift.String.Index
0x18ddd1eac  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.(tryEmitFastQuant in _B1BA5D5716180164B5D5D7DB68D175B1)(inout Swift.ArraySlice<_StringProcessing.DSLTree.Node>, _RegexParser.AST.Quantification.Kind, Swift.Int, Swift.Int?) -> Swift.Bool
0x18ddd3258  __TEXT,__text  merged outlined init with copy of _StringProcessing.DSLTree._AST.QuantificationAmount
0x18ddd33fc  __TEXT,__text  merged outlined destroy of _StringProcessing.DSLTree._AST.GroupKind
0x18ddd3454  __TEXT,__text  merged outlined init with copy of _StringProcessing.DSLTree._AST.GroupKind
0x18ddd34b4  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.(emitQuantification in _B1BA5D5716180164B5D5D7DB68D175B1)(_RegexParser.AST.Quantification.Amount, _StringProcessing.DSLTree.QuantificationKind, inout Swift.ArraySlice<_StringProcessing.DSLTree.Node>) throws -> ()
0x18ddd40f8  __TEXT,__text  merged outlined init with take of (_RegexParser.CaptureList.Capture, _StringProcessing.Processor._StoredCapture)
0x18ddd40f8  __TEXT,__text  merged outlined init with take of (_RegexParser.CaptureList.Capture, _StringProcessing.Processor._StoredCapture)
0x18ddd4158  __TEXT,__text  destroy value witness for _StringProcessing.DSLTree.Atom
0x18ddd4208  __TEXT,__text  generic specialization <Swift.String.UnicodeScalarView> of (extension in Swift):Swift.DefaultIndices< where A: Swift.BidirectionalCollection>.index(before: A.Index) -> A.Index
0x18ddd431c  __TEXT,__text  merged generic specialization <(extension in _RegexParser):Swift.Unicode.Script> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddd44c8  __TEXT,__text  merged outlined init with take of _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18ddd4528  __TEXT,__text  generic specialization <_RegexParser.AST.Node> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddd4550  __TEXT,__text  ___swift_initWithCopy_strong
0x18ddd45ac  __TEXT,__text  ___swift_destroy_strong
0x18ddd45b4  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.DSLTree.Atom
0x18ddd4730  __TEXT,__text  (extension in _StringProcessing):Swift.ArraySlice<A where A == _StringProcessing.DSLTree.Node>.skipNode(inout Swift.Int) -> ()
0x18ddd48cc  __TEXT,__text  merged _StringProcessing.Regex.firstMatch(in: Swift.Substring) throws -> _StringProcessing.Regex<A>.Match?
0x18ddd49d0  __TEXT,__text  destroy value witness for _StringProcessing.DSLTree
0x18ddd49d0  __TEXT,__text  destroy value witness for _StringProcessing.DSLTree
0x18ddd49dc  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing.State : Swift.Hashable in _StringProcessing
0x18ddd49dc  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing.State : Swift.Hashable in _StringProcessing
0x18ddd49dc  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing.State : Swift.Hashable in _StringProcessing
0x18ddd49dc  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing.State : Swift.Hashable in _StringProcessing
0x18ddd4a08  __TEXT,__text  _StringProcessing.Regex.Program.__deallocating_deinit
0x18ddd4a3c  __TEXT,__text  _StringProcessing.Regex.Program.loweredProgram.getter : _StringProcessing.MEProgram
0x18ddd4d30  __TEXT,__text  loadProgram #1 <A>() -> _StringProcessing.MEProgram? in _StringProcessing.Regex.Program.loweredProgram.getter : _StringProcessing.MEProgram
0x18ddd4dd0  __TEXT,__text  merged generic specialization <Swift.String.Index> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddd4f04  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.emitRoot(inout _StringProcessing.DSLList) throws -> _StringProcessing.MEProgram
0x18ddd51c8  __TEXT,__text  _StringProcessing.Compiler.emitViaList() throws -> _StringProcessing.MEProgram
0x18ddd54b0  __TEXT,__text  _StringProcessing.DSLList.autoPossessifyNextQuantification(_: inout Swift.Int, options: inout _StringProcessing.MatchingOptions) -> (Swift.Int, _StringProcessing.DSLTree.Atom)?
0x18ddd6700  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.(emitNode in _B1BA5D5716180164B5D5D7DB68D175B1)(inout Swift.ArraySlice<_StringProcessing.DSLTree.Node>) throws -> _StringProcessing.TypedInt<_StringProcessing._ValueRegister>?
0x18ddd7528  __TEXT,__text  static (extension in _StringProcessing):_RegexParser.CaptureList.Builder.build(_StringProcessing.DSLList) -> _RegexParser.CaptureList
0x18ddd77e8  __TEXT,__text  (extension in _StringProcessing):_RegexParser.CaptureList.Builder.addCaptures(in: inout Swift.ArraySlice<_StringProcessing.DSLTree.Node>, optionalNesting: _RegexParser.CaptureList.Builder.OptionalNesting, visibleInTypedOutput: Swift.Bool) -> ()
0x18ddd8188  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.emitQuotedLiteral(Swift.String) -> ()
0x18ddd8d1c  __TEXT,__text  generic specialization <_StringProcessing.Instruction> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddd8d30  __TEXT,__text  type metadata accessor for _StringProcessing.MEProgram
0x18ddd8d7c  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.MEProgram
0x18ddd8e24  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.MEProgram
0x18ddd8ec8  __TEXT,__text  outlined destroy of _StringProcessing.MEProgram?
0x18ddd8f28  __TEXT,__text  type metadata accessor for _StringProcessing.Compiler
0x18ddd8f4c  __TEXT,__text  _StringProcessing.MatchingOptions.(Representation in _684D3EBC598AF48CD1B258716A9A78E6).contains(_StringProcessing.MatchingOptions.(Option in _684D3EBC598AF48CD1B258716A9A78E6)) -> Swift.Bool
0x18ddd8f68  __TEXT,__text  function signature specialization <Arg[0] = Owned To Guaranteed> of generic specialization <[Swift.UInt8], _StringProcessing.TypedInt<_StringProcessing._UTF8Register>> of Swift.Dictionary.init(dictionaryLiteral: (A, B)...) -> [A : B]
0x18ddd9074  __TEXT,__text  function signature specialization <Arg[0] = [Closure Propagated : $s17_StringProcessing8CompilerC11ByteCodeGenV17emitQuotedLiteralyySSFSbyKXEfu_Sbs5UInt8Vcfu0_33_278392b31460599335b6d149056d9292AHSbTf3npk_n, Argument Types : []> of generic specialization <Swift.String.UTF8View> of (extension in Swif
0x18ddd920c  __TEXT,__text  function signature specialization <Arg[0] = Owned To Guaranteed> of generic specialization <Swift.Character, _StringProcessing.TypedInt<_StringProcessing._ElementRegister>> of Swift.Dictionary.init(dictionaryLiteral: (A, B)...) -> [A : B]
0x18ddd9338  __TEXT,__text  type metadata accessor for _StringProcessing.Compiler.ByteCodeGen
0x18ddd9384  __TEXT,__text  type metadata accessor for _StringProcessing.MEProgram.Builder
0x18ddd93d0  __TEXT,__text  function signature specialization <Arg[0] = Owned To Guaranteed> of generic specialization <_StringProcessing.ReferenceID, [_StringProcessing.TypedInt<_StringProcessing._InstructionAddress>]> of Swift.Dictionary.init(dictionaryLiteral: (A, B)...) -> [A : B]
0x18ddd94bc  __TEXT,__text  function signature specialization <Arg[0] = Owned To Guaranteed> of generic specialization <_StringProcessing.ReferenceID, Swift.Int> of Swift.Dictionary.init(dictionaryLiteral: (A, B)...) -> [A : B]
0x18ddd95a0  __TEXT,__text  static _StringProcessing.Executor.firstMatch(_: _StringProcessing.MEProgram, _: Swift.String, subjectBounds: Swift.Range<Swift.String.Index>, searchBounds: Swift.Range<Swift.String.Index>) throws -> _StringProcessing.Regex<A>.Match?
0x18ddd96d4  __TEXT,__text  _StringProcessing.Processor.reset(currentPosition: Swift.String.Index, searchBounds: Swift.Range<Swift.String.Index>) -> ()
0x18ddd9844  __TEXT,__text  _StringProcessing.Processor.signalFailure(preservingCaptures: Swift.Bool) -> ()
0x18ddd9a44  __TEXT,__text  destroy value witness for _StringProcessing.MEProgram
0x18ddd9b2c  __TEXT,__text  outlined init with copy of _StringProcessing.Processor.Registers
0x18ddd9b80  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.MEProgram
0x18ddd9d38  __TEXT,__text  static _StringProcessing.Executor._firstMatch(_: _StringProcessing.MEProgram, using: inout _StringProcessing.Processor) throws -> _StringProcessing.Regex<A>.Match?
0x18ddd9ff8  __TEXT,__text  outlined destroy of _StringProcessing.Processor
0x18ddda044  __TEXT,__text  ___swift__destructor.5
0x18ddda070  __TEXT,__text  ___swift__destructor.5
0x18ddda0b0  __TEXT,__text  function signature specialization <Arg[1] = Dead> of _StringProcessing.Instruction.OpCode.init(rawValue: Swift.UInt64) -> _StringProcessing.Instruction.OpCode?
0x18ddda0b8  __TEXT,__text  destroy value witness for _StringProcessing.Processor
0x18ddda150  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.Processor.Registers
0x18ddda220  __TEXT,__text  (extension in _StringProcessing):Swift.String.matchUTF8(_: [Swift.UInt8], at: Swift.String.Index, limitedBy: Swift.String.Index, boundaryCheck: Swift.Bool) -> Swift.String.Index?
0x18ddda434  __TEXT,__text  _StringProcessing.Regex.Program.(ProgramBox in _45BE7334FC47A99CAE19728A97C42F4D).__deallocating_deinit
0x18ddda478  __TEXT,__text  generic specialization <Any> of Swift.Array.init(repeating: A, count: Swift.Int) -> [A]
0x18ddda500  __TEXT,__text  outlined destroy of _StringProcessing.Compiler.ByteCodeGen
0x18ddda554  __TEXT,__text  destroy value witness for _StringProcessing.Compiler.ByteCodeGen
0x18ddda658  __TEXT,__text  ___swift_destroy_boxed_opaque_existential_0
0x18ddda688  __TEXT,__text  outlined destroy of _StringProcessing.Processor._StoredCapture
0x18ddda6d4  __TEXT,__text  generic specialization <_StringProcessing.Processor._StoredCapture> of Swift.Array.init(repeating: A, count: Swift.Int) -> [A]
0x18ddda758  __TEXT,__text  _StringProcessing.MEProgram.Builder.(resolveReferences in _7003A767AD11A95AB4DCA327B623B7AF)() throws -> ()
0x18ddda954  __TEXT,__text  type metadata accessor for _StringProcessing.Regex.Program.(ProgramBox in _45BE7334FC47A99CAE19728A97C42F4D)
0x18ddda96c  __TEXT,__text  destroy value witness for _StringProcessing.Processor._StoredCapture
0x18ddda980  __TEXT,__text  _StringProcessing.Compiler.__deallocating_deinit
0x18ddda9b4  __TEXT,__text  ___swift_get_extra_inhabitant_indexTm
0x18dddaa48  __TEXT,__text  ___swift_get_extra_inhabitant_indexTm
0x18dddaaa8  __TEXT,__text  ___swift_get_extra_inhabitant_indexTm
0x18dddab04  __TEXT,__text  merged outlined destroy of _StringProcessing.DSLTree._AST.QuantificationAmount
0x18dddab5c  __TEXT,__text  generic specialization <Swift.String.UnicodeScalarView> of Swift.DefaultIndices.formIndex(after: inout A.Index) -> ()
0x18dddac18  __TEXT,__text  generic specialization <Swift.ArraySlice<_StringProcessing.DSLTree.Node>> of (extension in Swift):Swift.Collection< where A == A.SubSequence>.popFirst() -> A.Element?
0x18dddac70  __TEXT,__text  Swift._StringGuts.validateInclusiveScalarIndex(Swift.String.Index) -> Swift.String.Index
0x18dddad08  __TEXT,__text  lazy protocol witness table accessor for type _RegexParser.AST.Quantification.Kind and conformance _RegexParser.AST.Quantification.Kind : Swift.Equatable in _RegexParser
0x18dddad60  __TEXT,__text  (extension in _StringProcessing):Swift.String._quickASCIICharacter(at: Swift.String.Index, limitedBy: Swift.String.Index) -> (first: Swift.UInt8, next: Swift.String.Index, crLF: Swift.Bool)?
0x18dddb16c  __TEXT,__text  _StringProcessing.DSLTree.CustomCharacterClass.AsciiBitset.(_matchesWithoutInversionCheck in _D26381CE77B83115F712EBAD681686C9)(Swift.UInt8) -> Swift.Bool
0x18dddb19c  __TEXT,__text  (extension in _StringProcessing):Swift.String.matchASCIIBitset(_: _StringProcessing.DSLTree.CustomCharacterClass.AsciiBitset, at: Swift.String.Index, limitedBy: Swift.String.Index, isScalarSemantics: Swift.Bool) -> Swift.String.Index?
0x18dddb6dc  __TEXT,__text  _StringProcessing.Processor.runQuantify(_StringProcessing.QuantifyPayload) -> Swift.Bool
0x18dddc7dc  __TEXT,__text  ___swift__destructor.2
0x18dddc810  __TEXT,__text  ___swift__destructor.2
0x18dddc820  __TEXT,__text  ___swift__destructor.2
0x18dddc83c  __TEXT,__text  _StringProcessing.Processor.builtinAssert(by: _StringProcessing.AssertionPayload) throws -> Swift.Bool
0x18dddcfd4  __TEXT,__text  outlined consume of _StringProcessing.DSLTree.Node?
0x18dddcfe8  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.emitAssertion(_StringProcessing.DSLTree.Atom.Assertion) throws -> ()
0x18dddd1fc  __TEXT,__text  _StringProcessing.DSLList.(_requiredAtomImpl in _8A2FB539FB7F1C39147DFC7105532072)(_: inout Swift.Int, options: inout _StringProcessing.MatchingOptions, allowOptionsChanges: Swift.Bool) -> _StringProcessing.DSLTree.Atom??
0x18ddddfa4  __TEXT,__text  (extension in _StringProcessing):_RegexParser.AST.Quantification.Kind.applying(_StringProcessing.MatchingOptions) -> _RegexParser.AST.Quantification.Kind
0x18ddde1a8  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.skipNode(_: inout Swift.ArraySlice<_StringProcessing.DSLTree.Node>, preservingCaptures: Swift.Bool) throws -> ()
0x18ddde8f8  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.emitAtom(_StringProcessing.DSLTree.Atom) throws -> ()
0x18dddeeb4  __TEXT,__text  merged lazy protocol witness table accessor for type _RegexParser.Unsupported and conformance _RegexParser.Unsupported : Swift.Error in _RegexParser
0x18dddeefc  __TEXT,__text  merged lazy protocol witness table accessor for type _RegexParser.Unsupported and conformance _RegexParser.Unsupported : Swift.Error in _RegexParser
0x18dddef44  __TEXT,__text  merged lazy protocol witness table accessor for type _RegexParser.Unsupported and conformance _RegexParser.Unsupported : Swift.Error in _RegexParser
0x18dddef8c  __TEXT,__text  merged lazy protocol witness table accessor for type _RegexParser.Unsupported and conformance _RegexParser.Unsupported : Swift.Error in _RegexParser
0x18dddefd4  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.DSLTree._AST.QuantificationKind
0x18dddf000  __TEXT,__text  convert #1 (_RegexParser.AST.CustomCharacterClass.Member) -> _StringProcessing.DSLTree.CustomCharacterClass.Member in (extension in _StringProcessing):_RegexParser.AST.CustomCharacterClass.dslTreeClass.getter : _StringProcessing.DSLTree.CustomCharacterClass
0x18dddfb58  __TEXT,__text  _StringProcessing.DSLTree.CustomCharacterClass.asAsciiBitset(_StringProcessing.MatchingOptions) -> _StringProcessing.DSLTree.CustomCharacterClass.AsciiBitset?
0x18dde0f70  __TEXT,__text  generic specialization <_StringProcessing.DSLTree.CustomCharacterClass.AsciiBitset> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18dde107c  __TEXT,__text  (extension in _StringProcessing):_RegexParser.AST.CustomCharacterClass.dslTreeClass.getter : _StringProcessing.DSLTree.CustomCharacterClass
0x18dde125c  __TEXT,__text  generic specialization <_StringProcessing.DSLTree.CustomCharacterClass.Member> of Swift._ContiguousArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ContiguousArrayBuffer<A>
0x18dde1400  __TEXT,__text  generic specialization <_StringProcessing.DSLTree.CustomCharacterClass.Member> of Swift.ContiguousArray._createNewBuffer(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> ()
0x18dde1420  __TEXT,__text  type metadata completion function for _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18dde14cc  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree.CustomCharacterClass.AsciiBitset
0x18dde14dc  __TEXT,__text  type metadata accessor for _StringProcessing.RegexRangesSequence
0x18dde16b0  __TEXT,__text  (extension in _StringProcessing):Swift.Collection< where A.SubSequence == Swift.Substring>._ranges<A where A1: _StringProcessing.RegexComponent>(of: A1, subjectBounds: Swift.Range<Swift.String.Index>, searchBounds: Swift.Range<Swift.String.Index>) -> _StringProcessing.RegexRangesSequence<A1.RegexOut
0x18dde17ac  __TEXT,__text  type metadata accessor for _StringProcessing.Executor.Matches
0x18dde17c4  __TEXT,__text  _StringProcessing.RegexRangesSequence.init(input: Swift.String, subjectBounds: Swift.Range<Swift.String.Index>, searchBounds: Swift.Range<Swift.String.Index>, regex: _StringProcessing.Regex<A>) -> _StringProcessing.RegexRangesSequence<A>
0x18dde1998  __TEXT,__text  generic specialization <Swift.String> of (extension in Swift):Swift.Collection.first.getter : A.Element?
0x18dde19e0  __TEXT,__text  type metadata completion function for _StringProcessing.Executor.Matches.Iterator
0x18dde1a6c  __TEXT,__text  merged type metadata completion function for _StringProcessing.RegexRangesSequence
0x18dde1aec  __TEXT,__text  type metadata instantiation function for _StringProcessing.RegexRangesSequence
0x18dde1aec  __TEXT,__text  type metadata instantiation function for _StringProcessing.RegexRangesSequence
0x18dde1af0  __TEXT,__text  type metadata completion function for _StringProcessing.RegexRangesSequence
0x18dde1b08  __TEXT,__text  type metadata completion function for _StringProcessing.Executor.Matches
0x18dde1b94  __TEXT,__text  type metadata accessor for _StringProcessing.RegexRangesSequence.Iterator
0x18dde1bac  __TEXT,__text  type metadata completion function for _StringProcessing.RegexRangesSequence.Iterator
0x18dde1bc4  __TEXT,__text  associated type witness table accessor for Swift.Sequence.Iterator : Swift.IteratorProtocol in _StringProcessing.RegexRangesSequence<A> : Swift.Sequence in _StringProcessing
0x18dde1be0  __TEXT,__text  merged type metadata completion function for _StringProcessing.DSLTree._AST.GroupKind
0x18dde1c5c  __TEXT,__text  type metadata completion function for _StringProcessing.DSLTree._AST.QuantificationKind
0x18dde1c74  __TEXT,__text  type metadata completion function for _StringProcessing.DSLTree.Atom
0x18dde1d70  __TEXT,__text  type metadata completion function for _StringProcessing.MEProgram
0x18dde1e24  __TEXT,__text  type metadata completion function for _StringProcessing.DSLTree._AST.QuantificationAmount
0x18dde1e3c  __TEXT,__text  type metadata accessor for _StringProcessing.DSLTree._AST.QuantificationKind?
0x18dde1e94  __TEXT,__text  type metadata completion function for _StringProcessing.DSLTree.QuantificationKind
0x18dde1f20  __TEXT,__text  type metadata completion function for _StringProcessing.Compiler.ByteCodeGen
0x18dde1fc0  __TEXT,__text  type metadata completion function for _StringProcessing.MEProgram.Builder
0x18dde209c  __TEXT,__text  one-time initialization function for enableTracing
0x18dde20ac  __TEXT,__text  one-time initialization function for enableMetrics
0x18dde20bc  __TEXT,__text  one-time initialization function for disableOptimizations
0x18dde20cc  __TEXT,__text  type metadata completion function for _StringProcessing.DSLTree._AST.GroupKind
0x18dde20e4  __TEXT,__text  type metadata accessor for _StringProcessing._UTF8Register
0x18dde20f4  __TEXT,__text  type metadata accessor for _StringProcessing.TypedInt
0x18dde210c  __TEXT,__text  type metadata accessor for _StringProcessing.Instruction
0x18dde211c  __TEXT,__text  type metadata completion function for _StringProcessing.Regex.Program.(ProgramBox in _45BE7334FC47A99CAE19728A97C42F4D)
0x18dde2198  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.emitDot() throws -> ()
0x18dde24a4  __TEXT,__text  _StringProcessing.RegexRangesSequence.Iterator.next() -> Swift.Range<Swift.String.Index>?
0x18dde2590  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection._replacing<A, B where A1: Swift.Sequence, B1: Swift.Collection, A.Element == B1.Element, A1.Element == Swift.Range<A.Index>>(_: A1, with: B1, maxReplacements: Swift.Int) -> A
0x18dde2f84  __TEXT,__text  _StringProcessing.RegexRangesSequence.makeIterator() -> _StringProcessing.RegexRangesSequence<A>.Iterator
0x18dde3050  __TEXT,__text  _StringProcessing.Executor.Matches.Iterator.next() -> _StringProcessing.Regex<A>.Match?
0x18dde3140  __TEXT,__text  type metadata accessor for _StringProcessing.Executor.Matches.Iterator
0x18dde3158  __TEXT,__text  _StringProcessing.Executor.Matches.init(program: _StringProcessing.MEProgram, input: Swift.String, subjectBounds: Swift.Range<Swift.String.Index>, searchBounds: Swift.Range<Swift.String.Index>) -> _StringProcessing.Executor<A>.Matches
0x18dde31e4  __TEXT,__text  _StringProcessing.Executor.Matches.makeIterator() -> _StringProcessing.Executor<A>.Matches.Iterator
0x18dde33b4  __TEXT,__text  destroy value witness for _StringProcessing.RegexRangesSequence.Iterator
0x18dde3534  __TEXT,__text  Swift.Optional.map<A, B where A1: Swift.Error, B1: ~Swift.Copyable>((A) throws(A1) -> B1) throws(A1) -> B1?
0x18dde36bc  __TEXT,__text  protocol witness for Swift.IteratorProtocol.next() -> A.Element? in conformance _StringProcessing.RegexRangesSequence<A>.Iterator : Swift.IteratorProtocol in _StringProcessing
0x18dde36e8  __TEXT,__text  destroy value witness for _StringProcessing.RegexRangesSequence
0x18dde37f8  __TEXT,__text  merged protocol witness for Swift.Sequence.makeIterator() -> A.Iterator in conformance _StringProcessing.RangesSequence<A> : Swift.Sequence in _StringProcessing
0x18dde3848  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.RegexRangesSequence
0x18dde3a6c  __TEXT,__text  protocol witness for Swift.Sequence.makeIterator() -> A.Iterator in conformance _StringProcessing.RegexRangesSequence<A> : Swift.Sequence in _StringProcessing
0x18dde3a84  __TEXT,__text  generic specialization <[Swift.UInt8]> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18dde3bb4  __TEXT,__text  generic specialization <[Swift.UInt8]> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(A) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x18dde3c48  __TEXT,__text  generic specialization <[Swift.UInt8], _StringProcessing.TypedInt<_StringProcessing._UTF8Register>> of Swift._NativeDictionary.setValue(_: __owned B, forKey: A, isUnique: Swift.Bool) -> ()
0x18dde3d58  __TEXT,__text  generic specialization <serialized, Swift.String.UTF8View> of Swift._copyCollectionToContiguousArray<A where A: Swift.Collection>(A) -> Swift.ContiguousArray<A.Element>
0x18dde3e90  __TEXT,__text  generic specialization <[Swift.UInt8], _StringProcessing._UTF8Register> of _StringProcessing.TypedSetVector.store(A) -> _StringProcessing.TypedInt<B>
0x18dde3f98  __TEXT,__text  generic specialization <serialized, Swift.UInt8> of Swift._ContiguousArrayBuffer.init(_uninitializedCount: Swift.Int, minimumCapacity: Swift.Int) -> Swift._ContiguousArrayBuffer<A>
0x18dde4008  __TEXT,__text  generic specialization <[Swift.UInt8], _StringProcessing.TypedInt<_StringProcessing._UTF8Register>> of Swift._NativeDictionary._copyOrMoveAndResize(capacity: Swift.Int, moveElements: Swift.Bool) -> ()
0x18dde42b4  __TEXT,__text  generic specialization <[Swift.UInt8]> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(_: A, hashValue: Swift.Int) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x18dde4364  __TEXT,__text  generic specialization <_StringProcessing.ReferenceID, [_StringProcessing.TypedInt<_StringProcessing._InstructionAddress>]> of Swift._NativeDictionary._insert(at: Swift._HashTable.Bucket, key: __owned A, value: __owned B) -> ()
0x18dde4364  __TEXT,__text  generic specialization <_StringProcessing.ReferenceID, [_StringProcessing.TypedInt<_StringProcessing._InstructionAddress>]> of Swift._NativeDictionary._insert(at: Swift._HashTable.Bucket, key: __owned A, value: __owned B) -> ()
0x18dde43ac  __TEXT,__text  _StringProcessing.DSLTree.Atom.excludes(_: _StringProcessing.DSLTree.Atom, options: _StringProcessing.MatchingOptions) -> Swift.Bool
0x18dde4e74  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.emitAnyNonNewline() -> ()
0x18dde4fb8  __TEXT,__text  outlined consume of _StringProcessing.Regex<A1.RegexOutput>.Match?<A><A1 where A: Swift.BidirectionalCollection, A1: _StringProcessing.RegexComponent, A.SubSequence == Swift.Substring>
0x18dde4fb8  __TEXT,__text  outlined consume of _StringProcessing.Regex<A1.RegexOutput>.Match?<A><A1 where A: Swift.BidirectionalCollection, A1: _StringProcessing.RegexComponent, A.SubSequence == Swift.Substring>
0x18dde4fb8  __TEXT,__text  outlined consume of _StringProcessing.Regex<A1.RegexOutput>.Match?<A><A1 where A: Swift.BidirectionalCollection, A1: _StringProcessing.RegexComponent, A.SubSequence == Swift.Substring>
0x18dde4ff0  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.Regex.Match
0x18dde5034  __TEXT,__text  type metadata completion function for _StringProcessing.SplitSequence
0x18dde50c8  __TEXT,__text  type metadata accessor for _StringProcessing.SubstringSearcher
0x18dde50d8  __TEXT,__text  type metadata accessor for _StringProcessing.RangesSequence.Iterator
0x18dde50f0  __TEXT,__text  type metadata completion function for _StringProcessing.SplitSequence.Iterator
0x18dde5224  __TEXT,__text  type metadata completion function for _StringProcessing.RangesSequence.Iterator
0x18dde52f0  __TEXT,__text  type metadata accessor for _StringProcessing.SubstringSearcher.State
0x18dde5300  __TEXT,__text  type metadata accessor for _StringProcessing.SplitSequence.Iterator
0x18dde5318  __TEXT,__text  type metadata instantiation function for _StringProcessing.SplitSequence.Iterator
0x18dde5320  __TEXT,__text  associated type witness table accessor for _StringProcessing.CollectionSearcher.Searched : Swift.Collection in _StringProcessing.SubstringSearcher : _StringProcessing.CollectionSearcher in _StringProcessing
0x18dde5324  __TEXT,__text  lazy protocol witness table accessor for type Swift.Substring and conformance Swift.Substring : Swift.Collection in Swift
0x18dde5378  __TEXT,__text  type metadata accessor for _StringProcessing.MatchingOptions.(Representation in _684D3EBC598AF48CD1B258716A9A78E6)
0x18dde5388  __TEXT,__text  type metadata accessor for _StringProcessing._InstructionAddress
0x18dde5398  __TEXT,__text  type metadata accessor for _StringProcessing.Processor.SavePoint
0x18dde53a8  __TEXT,__text  type metadata instantiation function for _StringProcessing.FixedPatternConsumer
0x18dde53b0  __TEXT,__text  _StringProcessing.FixedPatternConsumer.consuming(_: A, in: Swift.Range<A.Index>) -> A.Index?
0x18dde59e8  __TEXT,__text  type metadata accessor for _StringProcessing.MEProgram.Builder.AddressFixup
0x18dde5d0c  __TEXT,__text  type metadata accessor for _StringProcessing.FixedPatternConsumer
0x18dde5d24  __TEXT,__text  _StringProcessing.FixedPatternConsumer.init(pattern: B) -> _StringProcessing.FixedPatternConsumer<A, B>
0x18dde5d4c  __TEXT,__text  type metadata completion function for _StringProcessing.FixedPatternConsumer
0x18dde5dc8  __TEXT,__text  (extension in _StringProcessing):Swift.Collection._trimmingPrefix<A where A == A1.Consumed, A1: _StringProcessing.CollectionConsumer>(A1) -> A.SubSequence
0x18dde611c  __TEXT,__text  (extension in _StringProcessing):_StringProcessing.CollectionConsumer.consuming(A.Consumed) -> A.Consumed.Index?
0x18dde646c  __TEXT,__text  associated type witness table accessor for _StringProcessing.CollectionConsumer.Consumed : Swift.Collection in _StringProcessing.FixedPatternConsumer<A, B> : _StringProcessing.CollectionConsumer in _StringProcessing
0x18dde6474  __TEXT,__text  protocol witness for _StringProcessing.CollectionConsumer.consuming(_: A.Consumed, in: Swift.Range<A.Consumed.Index>) -> A.Consumed.Index? in conformance _StringProcessing.FixedPatternConsumer<A, B> : _StringProcessing.CollectionConsumer in _StringProcessing
0x18dde6478  __TEXT,__text  destroy value witness for _StringProcessing.FixedPatternConsumer
0x18dde649c  __TEXT,__text  static _StringProcessing.Executor._run(_: _StringProcessing.MEProgram, _: Swift.String, subjectBounds: Swift.Range<Swift.String.Index>, searchBounds: Swift.Range<Swift.String.Index>, mode: _StringProcessing.MatchMode) throws -> _StringProcessing.Regex<A>.Match?
0x18dde65d0  __TEXT,__text  static _StringProcessing.Executor.prefixMatch(_: _StringProcessing.MEProgram, _: Swift.String, subjectBounds: Swift.Range<Swift.String.Index>, searchBounds: Swift.Range<Swift.String.Index>) throws -> _StringProcessing.Regex<A>.Match?
0x18dde6800  __TEXT,__text  generic specialization <_StringProcessing.DSLTree.CustomCharacterClass.Member, [_StringProcessing.DSLTree.CustomCharacterClass.Member]> of Swift.Array.append<A where A == A1.Element, A1: Swift.Sequence>(contentsOf: __owned A1) -> ()
0x18dde691c  __TEXT,__text  generic specialization <Swift.String> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18dde6a20  __TEXT,__text  destroy value witness for _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18dde6c14  __TEXT,__text  outlined assign with take of _StringProcessing.Processor._StoredCapture
0x18dde6c68  __TEXT,__text  finish() -> [_StringProcessing.DSLTree.CustomCharacterClass.Member] in Accumulator #1 in _StringProcessing.Compiler.ByteCodeGen.coalescingCustomCharacterClassMembers([_StringProcessing.DSLTree.CustomCharacterClass.Member]) -> [_StringProcessing.DSLTree.CustomCharacterClass.Member]
0x18dde730c  __TEXT,__text  merged outlined init with copy of _StringProcessing.DSLTree.Atom
0x18dde736c  __TEXT,__text  merged outlined init with copy of _StringProcessing.DSLTree.Atom
0x18dde73cc  __TEXT,__text  merged outlined init with copy of _StringProcessing.DSLTree.Atom
0x18dde742c  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.coalescingCustomCharacterClassMembers([_StringProcessing.DSLTree.CustomCharacterClass.Member]) -> [_StringProcessing.DSLTree.CustomCharacterClass.Member]
0x18dde7dbc  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.emitCustomCharacterClass(_StringProcessing.DSLTree.CustomCharacterClass) throws -> ()
0x18dde8ba8  __TEXT,__text  closure #1 (_StringProcessing.DSLTree.CustomCharacterClass.Member) -> _StringProcessing.DSLTree.CustomCharacterClass.Member in _StringProcessing.Compiler.ByteCodeGen.coalescingCustomCharacterClassMembers([_StringProcessing.DSLTree.CustomCharacterClass.Member]) -> [_StringProcessing.DSLTree.CustomCha
0x18dde8ea0  __TEXT,__text  generic specialization <Swift.String> of Swift._ArrayBuffer._consumeAndCreateNew() -> Swift._ArrayBuffer<A>
0x18dde8eb4  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.flatteningCustomCharacterClassMembers([_StringProcessing.DSLTree.CustomCharacterClass.Member]) -> [_StringProcessing.DSLTree.CustomCharacterClass.Member]
0x18dde92e0  __TEXT,__text  generic specialization <_StringProcessing.DSLTree.CustomCharacterClass.Member> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18dde9308  __TEXT,__text  generic specialization <Swift.Character> of Swift._NativeSet.insertNew(_: __owned A, at: Swift._HashTable.Bucket, isUnique: Swift.Bool) -> ()
0x18dde947c  __TEXT,__text  generic specialization <Swift.Character> of Swift.Set._Variant.insert(__owned A) -> (inserted: Swift.Bool, memberAfterInsert: A)
0x18dde95cc  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18dde9a60  __TEXT,__text  _StringProcessing.DSLTree._AST.QuantificationAmount.requiresAtLeastOne.getter : Swift.Bool
0x18dde9d44  __TEXT,__text  merged outlined destroy of _StringProcessing.DSLTree.Atom
0x18dde9d9c  __TEXT,__text  merged outlined destroy of _StringProcessing.DSLTree.Atom
0x18dde9df4  __TEXT,__text  _StringProcessing.DSLTree.CustomCharacterClass.containsDot.getter : Swift.Bool
0x18dde9ef4  __TEXT,__text  generic specialization <_StringProcessing.Processor._StoredCapture> of Swift._ArrayBuffer._consumeAndCreateNew() -> Swift._ArrayBuffer<A>
0x18dde9f08  __TEXT,__text  (extension in _StringProcessing):Swift.String.(matchZeroOrMoreRegexDot in _8B839612429B33A9C47D451A3C268A2F)(at: Swift.String.Index, limitedBy: Swift.String.Index, produceSavePointRange: Swift.Bool, anyMatchesNewline: Swift.Bool, isScalarSemantics: Swift.Bool) -> (next: Swift.String.Index, savePoint
0x18ddea1c4  __TEXT,__text  generic specialization <_StringProcessing.Processor._StoredCapture> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddea2e0  __TEXT,__text  outlined init with copy of _StringProcessing.Processor._StoredCapture
0x18ddea334  __TEXT,__text  ___swift__destructor.9
0x18ddea344  __TEXT,__text  ___swift__destructor.9
0x18ddea384  __TEXT,__text  _StringProcessing.Processor.SavePoint.takePositionFromQuantifiedRange(Swift.String) -> ()
0x18ddea51c  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.Processor._StoredCapture
0x18ddea5ac  __TEXT,__text  Swift._StringGuts.validateSubscalarIndex(Swift.String.Index) -> Swift.String.Index
0x18ddea620  __TEXT,__text  Swift._StringGuts.scalarAlignSlow(Swift.String.Index) -> Swift.String.Index
0x18ddea714  __TEXT,__text  generic specialization <Swift.Character> of Swift._NativeSet.copyAndResize(capacity: Swift.Int) -> ()
0x18ddea924  __TEXT,__text  assignWithTake value witness for _StringProcessing.Processor._StoredCapture
0x18ddea98c  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.(_guaranteesForwardProgressImpl in _B1BA5D5716180164B5D5D7DB68D175B1)(_: Swift.ArraySlice<_StringProcessing.DSLTree.Node>, position: inout Swift.Int) -> Swift.Bool
0x18ddeae0c  __TEXT,__text  outlined destroy of _StringProcessing.Processor.SavePoint
0x18ddeae58  __TEXT,__text  (extension in _StringProcessing):Swift.String.matchScalar(_: Swift.Unicode.Scalar, at: Swift.String.Index, limitedBy: Swift.String.Index, boundaryCheck: Swift.Bool, isCaseInsensitive: Swift.Bool) -> Swift.String.Index?
0x18ddeb234  __TEXT,__text  generic specialization <_StringProcessing.Processor.SavePoint> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddeb350  __TEXT,__text  _StringProcessing.MEProgram.Builder.buildBranch(to: _StringProcessing.TypedInt<_StringProcessing.MEProgram.Builder._AddressToken>) -> ()
0x18ddeb358  __TEXT,__text  generic specialization <_StringProcessing.Instruction> of Swift._ArrayBuffer._consumeAndCreateNew() -> Swift._ArrayBuffer<A>
0x18ddeb36c  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.(emitAlternation in _B1BA5D5716180164B5D5D7DB68D175B1)(_: inout Swift.ArraySlice<_StringProcessing.DSLTree.Node>, alternationCount: Swift.Int) throws -> ()
0x18ddeb594  __TEXT,__text  generic specialization <_StringProcessing.MatchingOptions.(Representation in _684D3EBC598AF48CD1B258716A9A78E6)> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddeb690  __TEXT,__text  _StringProcessing.MEProgram.Builder.buildSave(_StringProcessing.TypedInt<_StringProcessing.MEProgram.Builder._AddressToken>) -> ()
0x18ddeb698  __TEXT,__text  generic specialization <_StringProcessing.TypedInt<_StringProcessing._InstructionAddress>?> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddeb790  __TEXT,__text  merged _StringProcessing.MEProgram.Builder.buildBranch(to: _StringProcessing.TypedInt<_StringProcessing.MEProgram.Builder._AddressToken>) -> ()
0x18ddeb8b4  __TEXT,__text  generic specialization <(_StringProcessing.TypedInt<_StringProcessing._InstructionAddress>, _StringProcessing.MEProgram.Builder.AddressFixup)> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddeb9ac  __TEXT,__text  destroy value witness for _StringProcessing.Processor.SavePoint
0x18ddeb9e4  __TEXT,__text  generic specialization <_StringProcessing.Processor.SavePoint> of Swift.Array._customRemoveLast() -> A?
0x18ddeba6c  __TEXT,__text  ___swift__destructor
0x18ddeba98  __TEXT,__text  ___swift__destructor
0x18ddebacc  __TEXT,__text  ___swift__destructor
0x18ddebaf8  __TEXT,__text  ___swift__destructor
0x18ddebb2c  __TEXT,__text  ___swift__destructor
0x18ddebb60  __TEXT,__text  ___swift__destructor
0x18ddebb94  __TEXT,__text  ___swift__destructor
0x18ddebbc0  __TEXT,__text  type metadata accessor for _StringProcessing.Processor._StoredCapture
0x18ddebbd0  __TEXT,__text  generic specialization <[Swift.Int]> of (extension in _StringProcessing):Swift.MutableCollection._setAll(to: A.Element) -> ()
0x18ddebc7c  __TEXT,__text  generic specialization <Swift.Int> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddebd78  __TEXT,__text  generic specialization <Swift.Int> of Swift._ArrayBuffer._consumeAndCreateNew() -> Swift._ArrayBuffer<A>
0x18ddebd8c  __TEXT,__text  _StringProcessing.MatchingOptions.defaultQuantificationKind.getter : _RegexParser.AST.Quantification.Kind
0x18ddebe64  __TEXT,__text  _StringProcessing.MEProgram.Builder.buildCondBranch(to: _StringProcessing.TypedInt<_StringProcessing.MEProgram.Builder._AddressToken>, ifZeroElseDecrement: _StringProcessing.TypedInt<_StringProcessing._IntRegister>) -> ()
0x18ddebf90  __TEXT,__text  _StringProcessing.MEProgram.Builder.buildSplit(to: _StringProcessing.TypedInt<_StringProcessing.MEProgram.Builder._AddressToken>, saving: _StringProcessing.TypedInt<_StringProcessing.MEProgram.Builder._AddressToken>) -> ()
0x18ddec0bc  __TEXT,__text  generic specialization <[Any]> of (extension in _StringProcessing):Swift.MutableCollection._setAll(to: A.Element) -> ()
0x18ddec14c  __TEXT,__text  generic specialization <[Swift.String.Index]> of (extension in _StringProcessing):Swift.MutableCollection._setAll(to: A.Element) -> ()
0x18ddec1f8  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.DSLTree._AST.GroupKind
0x18ddec210  __TEXT,__text  merged _StringProcessing.Regex.ignoresCase(Swift.Bool) -> _StringProcessing.Regex<A>
0x18ddec338  __TEXT,__text  merged initializeWithCopy value witness for _StringProcessing.DSLTree._AST.GroupKind
0x18ddec398  __TEXT,__text  outlined init with copy of _RegexParser.Source.Location?
0x18ddec400  __TEXT,__text  merged destroy value witness for _StringProcessing.DSLTree._AST.GroupKind
0x18ddec454  __TEXT,__text  _StringProcessing.MatchingOptions.(Representation in _684D3EBC598AF48CD1B258716A9A78E6).apply(_RegexParser.AST.MatchingOptionSequence) -> ()
0x18dded164  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.(emitNoncapturingGroup in _B1BA5D5716180164B5D5D7DB68D175B1)(_RegexParser.AST.Group.Kind, inout Swift.ArraySlice<_StringProcessing.DSLTree.Node>) throws -> ()
0x18dded984  __TEXT,__text  generic specialization <_StringProcessing.MatchingOptions.(Representation in _684D3EBC598AF48CD1B258716A9A78E6)> of Swift._ArrayBuffer._consumeAndCreateNew() -> Swift._ArrayBuffer<A>
0x18dded998  __TEXT,__text  destroy value witness for _StringProcessing.DSLTree._AST.GroupKind
0x18dded9bc  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.DSLTree
0x18dded9bc  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.DSLTree
0x18dded9bc  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.DSLTree
0x18dded9bc  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.DSLTree
0x18dded9f4  __TEXT,__text  function signature specialization <Arg[2] = Owned To Guaranteed> of generic specialization <Swift._ArrayBuffer<_StringProcessing.DSLTree.Node>, Swift.CollectionOfOne<_StringProcessing.DSLTree.Node>> of (extension in Swift):Swift._ArrayBufferProtocol.replaceSubrange<A where A1: Swift.Collection, A.El
0x18ddedb28  __TEXT,__text  ___swift_memcpy8_8
0x18ddedb34  __TEXT,__text  ___swift_noop_void_return
0x18ddedb38  __TEXT,__text  lazy protocol witness table accessor for type [_StringProcessing.DSLTree.Node] and conformance [A] : Swift.Collection in Swift
0x18ddedba0  __TEXT,__text  generic specialization <_StringProcessing.DSLTree.Node> of Swift._ArrayBuffer._consumeAndCreateNew() -> Swift._ArrayBuffer<A>
0x18ddedcec  __TEXT,__text  outlined init with take of _StringProcessing.DSLTree.QuantificationKind
0x18ddedd48  __TEXT,__text  _StringProcessing.Regex.prepending<A>(_StringProcessing.DSLTree.Node) -> _StringProcessing.Regex<A1>
0x18ddede24  __TEXT,__text  _StringProcessing.Regex.alternating<A, B where B1: Swift.Collection, B1.Element == _StringProcessing.DSLTree.Node>(with: B1) -> _StringProcessing.Regex<A1>
0x18ddee2e0  __TEXT,__text  ___swift_store_extra_inhabitant_indexTm
0x18ddee374  __TEXT,__text  ___swift_store_extra_inhabitant_indexTm
0x18ddee3d8  __TEXT,__text  ___swift_store_extra_inhabitant_indexTm
0x18ddee438  __TEXT,__text  (extension in _StringProcessing):_StringProcessing.RegexComponent.(wrapInOption in _8D4513B35AC037599F29FBAF7E5049EC)(_: _RegexParser.AST.MatchingOption.Kind, addingIf: Swift.Bool) -> _StringProcessing.Regex<A.RegexOutput>
0x18ddee7c0  __TEXT,__text  generic specialization <_StringProcessing.DSLTree.Node, [_StringProcessing.DSLTree.Node]> of Swift.Array.append<A where A == A1.Element, A1: Swift.Sequence>(contentsOf: __owned A1) -> ()
0x18ddee8b8  __TEXT,__text  _StringProcessing.DSLList.indexOfCoalescableAtom(startingAt: Swift.Int, findLast: Swift.Bool) -> Swift.Int?
0x18ddeeab0  __TEXT,__text  _StringProcessing.DSLList.coalesce(withFirstAtomIn: inout _StringProcessing.DSLList) -> ()
0x18ddeefb0  __TEXT,__text  function signature specialization <Return = Owned To Guaranteed> of _StringProcessing.Regex.list.getter : _StringProcessing.DSLList
0x18ddeefc0  __TEXT,__text  _StringProcessing.Regex.concatenating<A>(_StringProcessing.DSLList) -> _StringProcessing.Regex<A1>
0x18ddef304  __TEXT,__text  _StringProcessing.DSLTree.Atom.literalCharacterValue.getter : Swift.Character?
0x18ddef414  __TEXT,__text  outlined destroy of _StringProcessing.DSLTree.Atom
0x18ddef468  __TEXT,__text  _StringProcessing.Regex.init(list: _StringProcessing.DSLList) -> _StringProcessing.Regex<A>
0x18ddef4c0  __TEXT,__text  outlined init with copy of _StringProcessing.DSLTree.Atom
0x18ddef74c  __TEXT,__text  (extension in _StringProcessing):Swift.Collection.(_endOfPrefix in _4A2CD2DC1DC5298E753BB2050E73EF4D)(while: (A.Element) throws -> Swift.Bool) throws -> A.Index
0x18ddef920  __TEXT,__text  partial apply forwarder for closure #1 (A.Element) throws -> Swift.Bool in (extension in _StringProcessing):Swift.Collection.(_endOfPrefix in _4A2CD2DC1DC5298E753BB2050E73EF4D)(while: (A.Element) throws -> Swift.Bool) throws -> A.Index
0x18ddef950  __TEXT,__text  generic specialization <Any.Type> of Swift.ContiguousArray._createNewBuffer(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> ()
0x18ddef970  __TEXT,__text  outlined init with copy of Any
0x18ddef9c4  __TEXT,__text  outlined init with take of Any
0x18ddef9d4  __TEXT,__text  partial apply forwarder for closure #1 (Swift.String, Swift.String.Index, Swift.Range<Swift.String.Index>) throws -> (Swift.String.Index, Any)? in (extension in _StringProcessing):_StringProcessing.CustomConsumingRegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput>
0x18ddefa10  __TEXT,__text  partial apply forwarder for closure #1 (Swift.String, Swift.String.Index, Swift.Range<Swift.String.Index>) throws -> (Swift.String.Index, Any)? in _StringProcessing.Compiler.ByteCodeGen.emitMatcher((Swift.String, Swift.String.Index, Swift.Range<Swift.String.Index>) throws -> (Swift.String.Index, Any
0x18ddefa38  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@guaranteed Swift.String, @unowned Swift.String.Index, @unowned Swift.Range<Swift.String.Index>) -> (@out (Swift.String.Index, Any)?, @error @owned Swift.Error) to @escaping @callee_guaranteed (@in_guaranteed S
0x18ddefbe8  __TEXT,__text  closure #1 (Swift.String, Swift.String.Index, Swift.Range<Swift.String.Index>) throws -> (Swift.String.Index, Any)? in (extension in _StringProcessing):_StringProcessing.CustomConsumingRegexComponent.regex.getter : _StringProcessing.Regex<A.RegexOutput>
0x18ddeff00  __TEXT,__text  outlined destroy of _StringProcessing.DSLTree.QuantificationKind
0x18ddeff54  __TEXT,__text  merged generic specialization <(Swift.String, _StringProcessing.Processor._StoredCapture) throws -> Any?> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddf0078  __TEXT,__text  generic specialization <(Swift.String, Swift.String.Index, Swift.Range<Swift.String.Index>) throws -> (Swift.String.Index, Any)?> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddf008c  __TEXT,__text  _StringProcessing.Compiler.ByteCodeGen.emitMatcher((Swift.String, Swift.String.Index, Swift.Range<Swift.String.Index>) throws -> (Swift.String.Index, Any)?) -> _StringProcessing.TypedInt<_StringProcessing._ValueRegister>
0x18ddf0244  __TEXT,__text  ___swift_allocate_boxed_opaque_existential_0
0x18ddf0294  __TEXT,__text  merged _StringProcessing.Regex.wholeMatch(in: Swift.String) throws -> _StringProcessing.Regex<A>.Match?
0x18ddf03a8  __TEXT,__text  _StringProcessing.DSLTree.Atom.CharacterClass.asRuntimeModel(_StringProcessing.MatchingOptions) -> _StringProcessing._CharacterClassModel
0x18ddf0550  __TEXT,__text  _StringProcessing._CharacterClassModel.Representation.isStrictAscii(options: _StringProcessing.MatchingOptions) -> Swift.Bool
0x18ddf0690  __TEXT,__text  (extension in _StringProcessing):_RegexParser.AST.Atom.EscapedBuiltin.dslAssertionKind.getter : _StringProcessing.DSLTree.Atom.Assertion?
0x18ddf07e0  __TEXT,__text  (extension in _StringProcessing):_RegexParser.AST.Atom.EscapedBuiltin.dslCharacterClass.getter : _StringProcessing.DSLTree.Atom.CharacterClass?
0x18ddf0c28  __TEXT,__text  generic specialization <_StringProcessing.AnyRegexOutput> of (extension in _StringProcessing):Swift.Sequence< where A.Element == _StringProcessing.AnyRegexOutput.Element>.existentialOutput(from: Swift.String) -> Any
0x18ddf0fd8  __TEXT,__text  (extension in _StringProcessing):Swift.String.(matchOneOrMoreRegexDot in _8B839612429B33A9C47D451A3C268A2F)(at: Swift.String.Index, limitedBy: Swift.String.Index, produceSavePointRange: Swift.Bool, anyMatchesNewline: Swift.Bool, isScalarSemantics: Swift.Bool) -> (next: Swift.String.Index, savePointR
0x18ddf128c  __TEXT,__text  generic specialization <Any> of Swift.ContiguousArray._createNewBuffer(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> ()
0x18ddf12ac  __TEXT,__text  generic specialization <Any> of Swift._ContiguousArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ContiguousArrayBuffer<A>
0x18ddf13b0  __TEXT,__text  generic specialization <_StringProcessing.AnyRegexOutput.Element> of Swift.ContiguousArray._createNewBuffer(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> ()
0x18ddf13d0  __TEXT,__text  generic specialization <_StringProcessing.AnyRegexOutput.Element> of Swift._ContiguousArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ContiguousArrayBuffer<A>
0x18ddf14ec  __TEXT,__text  merged outlined destroy of Any?
0x18ddf1540  __TEXT,__text  static _StringProcessing.Executor.createExistentialElements(_: _StringProcessing.MEProgram, matchRange: Swift.Range<Swift.String.Index>, storedCaptures: [_StringProcessing.Processor._StoredCapture], wholeMatchValue: Any?) -> [_StringProcessing.AnyRegexOutput.ElementRepresentation]
0x18ddf1e4c  __TEXT,__text  generic specialization <Swift.ArraySlice<_RegexParser.CaptureList.Capture>, [_StringProcessing.Processor._StoredCapture]> of Swift.Zip2Sequence.Iterator.next() -> (A.Element, B.Element)?
0x18ddf2104  __TEXT,__text  outlined init with copy of Any?
0x18ddf2170  __TEXT,__text  outlined destroy of Any?
0x18ddf21d4  __TEXT,__text  generic specialization <_StringProcessing.AnyRegexOutput.ElementRepresentation> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddf22f0  __TEXT,__text  destroy value witness for _StringProcessing.AnyRegexOutput.ElementRepresentation
0x18ddf232c  __TEXT,__text  _StringProcessing.Regex.Match.init(anyRegexOutput: _StringProcessing.AnyRegexOutput, range: Swift.Range<Swift.String.Index>) -> _StringProcessing.Regex<A>.Match
0x18ddf275c  __TEXT,__text  (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>._matches<A where A1: _StringProcessing.RegexComponent>(of: A1) -> _StringProcessing.Executor<A1.RegexOutput>.Matches
0x18ddf2924  __TEXT,__text  destroy value witness for _StringProcessing.Executor.Matches
0x18ddf2a28  __TEXT,__text  _StringProcessing.Executor.Matches.Iterator.nextSearchIndex(after: Swift.Range<Swift.String.Index>) -> Swift.String.Index?
0x18ddf2b38  __TEXT,__text  (extension in _StringProcessing):Swift.String._quickMatch(_: _StringProcessing._CharacterClassModel.Representation, at: Swift.String.Index, limitedBy: Swift.String.Index, isScalarSemantics: Swift.Bool) -> (next: Swift.String.Index, matchResult: Swift.Bool)?
0x18ddf2d4c  __TEXT,__text  function signature specialization <Arg[1] = Dead> of _StringProcessing._CharacterClassModel.Representation.init(rawValue: Swift.UInt64) -> _StringProcessing._CharacterClassModel.Representation?
0x18ddf2d54  __TEXT,__text  outlined init with copy of _StringProcessing.AnyRegexOutput.ElementRepresentation
0x18ddf2da8  __TEXT,__text  type metadata accessor for _StringProcessing.AnyRegexOutput.ElementRepresentation
0x18ddf2db8  __TEXT,__text  partial apply forwarder for implicit closure #1 (_StringProcessing.Regex<A>.Match) -> Swift.Range<Swift.String.Index> in _StringProcessing.RegexRangesSequence.Iterator.next() -> Swift.Range<Swift.String.Index>?
0x18ddf2dd8  __TEXT,__text  implicit closure #1 (_StringProcessing.Regex<A>.Match) -> Swift.Range<Swift.String.Index> in _StringProcessing.RegexRangesSequence.Iterator.next() -> Swift.Range<Swift.String.Index>?
0x18ddf2e5c  __TEXT,__text  merged function signature specialization <Arg[1] = Owned To Guaranteed> of generic specialization <Swift.String> of (extension in Swift):Swift.Collection.dropFirst(Swift.Int) -> A.SubSequence
0x18ddf2f20  __TEXT,__text  function signature specialization <Arg[1] = Owned To Guaranteed> of generic specialization <Swift.String> of (extension in Swift):Swift.Collection.dropFirst(Swift.Int) -> A.SubSequence
0x18ddf2f4c  __TEXT,__text  merged function signature specialization <Arg[1] = Owned To Guaranteed> of generic specialization <Swift.String> of (extension in Swift):Swift.Collection.dropLast(Swift.Int) -> A.SubSequence
0x18ddf35dc  __TEXT,__text  outlined destroy of _StringProcessing.AnyRegexOutput.Element
0x18ddf3690  __TEXT,__text  generic specialization <Swift.Substring> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddf3794  __TEXT,__text  function signature specialization <Arg[1] = Stack Promoted from Box, Arg[3] = Stack Promoted from Box> of appendSubsequence #1 <A><A1 where A: Swift.BidirectionalCollection, A1: _StringProcessing.RegexComponent, A.SubSequence == Swift.Substring>(end: Swift.String.Index) -> Swift.Bool in (extension i
0x18ddf38c4  __TEXT,__text  destroy value witness for _StringProcessing.Executor.Matches.Iterator
0x18ddf3a38  __TEXT,__text  generic specialization <Swift.Character> of Swift._NativeSet.resize(capacity: Swift.Int) -> ()
0x18ddf3c84  __TEXT,__text  function signature specialization <Arg[1] = Dead> of generic specialization <_StringProcessing.Processor.SavePoint, Swift.EmptyCollection<_StringProcessing.Processor.SavePoint>> of Swift.Array.replaceSubrange<A where A == A1.Element, A1: Swift.Collection>(_: Swift.Range<Swift.Int>, with: __owned A1)
0x18ddf3d40  __TEXT,__text  merged _StringProcessing._RegexFactory.assertion<A>(_StringProcessing.DSLTree.Atom.Assertion) -> _StringProcessing.Regex<A>
0x18ddf3dbc  __TEXT,__text  function signature specialization <Arg[1] = Stack Promoted from Box> of wrap #1 <A>(A) -> () in _StringProcessing.constructExistentialOutputComponent(from: Swift.String, component: (range: Swift.Range<Swift.String.Index>, value: Any?)?, optionalCount: Swift.Int) -> Any
0x18ddf3e6c  __TEXT,__text  reabstraction thunk helper <A, B> from @escaping @callee_guaranteed (@guaranteed Swift.Substring) -> (@out B, @error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.Substring) -> (@out Any?, @error @owned Swift.Error)
0x18ddf3f3c  __TEXT,__text  destroy value witness for _StringProcessing.AnyRegexOutput.Element
0x18ddf3f80  __TEXT,__text  merged _StringProcessing._RegexFactory.zeroOrOne<A, B where B: _StringProcessing.RegexComponent>(B, _StringProcessing.RegexRepetitionBehavior?) -> _StringProcessing.Regex<A>
0x18ddf434c  __TEXT,__text  makeNil #1 <A>(A.Type) -> Any in _StringProcessing.constructExistentialOutputComponent(from: Swift.String, component: (range: Swift.Range<Swift.String.Index>, value: Any?)?, optionalCount: Swift.Int) -> Any
0x18ddf43bc  __TEXT,__text  generic specialization <Any> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddf44c4  __TEXT,__text  generic specialization <Any.Type> of Swift._ContiguousArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ContiguousArrayBuffer<A>
0x18ddf45bc  __TEXT,__text  merged partial apply forwarder for reabstraction thunk helper <A, B> from @escaping @callee_guaranteed (@in_guaranteed Swift.Substring) -> (@out B?, @error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.Substring) -> (@out B?, @error @owned Swift.Error)
0x18ddf45f8  __TEXT,__text  partial apply forwarder for reabstraction thunk helper <A, B> from @escaping @callee_guaranteed (@in_guaranteed Swift.Substring) -> (@out B?, @error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.Substring) -> (@out B?, @error @owned Swift.Error)
0x18ddf4610  __TEXT,__text  partial apply forwarder for reabstraction thunk helper <A, B> from @escaping @callee_guaranteed (@in_guaranteed Swift.Substring) -> (@out B, @error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.Substring) -> (@out B, @error @owned Swift.Error)
0x18ddf4628  __TEXT,__text  partial apply forwarder for reabstraction thunk helper <A, B> from @escaping @callee_guaranteed (@guaranteed Swift.Substring) -> (@out B, @error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.Substring) -> (@out Any?, @error @owned Swift.Error)
0x18ddf4648  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.AnyRegexOutput.ElementRepresentation
0x18ddf470c  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.Regex.Match
0x18ddf475c  __TEXT,__text  ___swift_memcpy65_8
0x18ddf4780  __TEXT,__text  destroy value witness for _StringProcessing.Regex.Match
0x18ddf4780  __TEXT,__text  destroy value witness for _StringProcessing.Regex.Match
0x18ddf47b0  __TEXT,__text  lazy protocol witness table accessor for type [Any] and conformance [A] : Swift.BidirectionalCollection in Swift
0x18ddf4818  __TEXT,__text  ___swift_exist.box.addr_destructor
0x18ddf4844  __TEXT,__text  ___swift_exist.box.addr_destructor
0x18ddf4870  __TEXT,__text  ___swift_exist.box.addr_destructor
0x18ddf489c  __TEXT,__text  ___swift_exist.box.addr_destructor
0x18ddf48c8  __TEXT,__text  ___swift_exist.box.addr_destructor
0x18ddf48f4  __TEXT,__text  closure #1 (Swift.String, _StringProcessing.Processor._StoredCapture) throws -> Any? in _StringProcessing.Compiler.ByteCodeGen.(emitNode in _B1BA5D5716180164B5D5D7DB68D175B1)(inout Swift.ArraySlice<_StringProcessing.DSLTree.Node>) throws -> _StringProcessing.TypedInt<_StringProcessing._ValueRegister
0x18ddf4a48  __TEXT,__text  _StringProcessing.CaptureTransform.callAsFunction(Swift.Substring) throws -> Any?
0x18ddf4b24  __TEXT,__text  partial apply forwarder for closure #1 (Swift.String, _StringProcessing.Processor._StoredCapture) throws -> Any? in _StringProcessing.Compiler.ByteCodeGen.(emitNode in _B1BA5D5716180164B5D5D7DB68D175B1)(inout Swift.ArraySlice<_StringProcessing.DSLTree.Node>) throws -> _StringProcessing.TypedInt<_Str
0x18ddf4b40  __TEXT,__text  generic specialization <Any> of Swift._ArrayBuffer._consumeAndCreateNew() -> Swift._ArrayBuffer<A>
0x18ddf4b54  __TEXT,__text  ___swift_assign_boxed_opaque_existential_0
0x18ddf4d04  __TEXT,__text  outlined destroy of (Swift.String.Index, Any)?
0x18ddf4d64  __TEXT,__text  ___swift_closure_destructor.18
0x18ddf4d68  __TEXT,__text  ___swift_closure_destructor
0x18ddf4d78  __TEXT,__text  ___swift_closure_destructor
0x18ddf4d88  __TEXT,__text  ___swift_closure_destructor
0x18ddf4d98  __TEXT,__text  ___swift_closure_destructor
0x18ddf4e04  __TEXT,__text  ___swift_closure_destructor
0x18ddf4e30  __TEXT,__text  ___swift_closure_destructor
0x18ddf4e40  __TEXT,__text  ___swift_closure_destructor
0x18ddf4e6c  __TEXT,__text  ___swift_closure_destructor
0x18ddf4e98  __TEXT,__text  ___swift_closure_destructor
0x18ddf4ec8  __TEXT,__text  ___swift_closure_destructor.15
0x18ddf4ef4  __TEXT,__text  generic specialization <(Swift.String, _StringProcessing.Processor._StoredCapture) throws -> Any?> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddf4f08  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18ddf4f08  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18ddf4f08  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18ddf4f08  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18ddf4f08  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18ddf4f08  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18ddf4f08  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18ddf4f0c  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing._CharacterClassModel.Representation
0x18ddf4f0c  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing._CharacterClassModel.Representation
0x18ddf4f0c  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing._CharacterClassModel.Representation
0x18ddf4f0c  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing._CharacterClassModel.Representation
0x18ddf4f14  __TEXT,__text  static _StringProcessing.Executor.wholeMatch(_: _StringProcessing.MEProgram, _: Swift.String, subjectBounds: Swift.Range<Swift.String.Index>, searchBounds: Swift.Range<Swift.String.Index>) throws -> _StringProcessing.Regex<A>.Match?
0x18ddf4f5c  __TEXT,__text  outlined copy of _StringProcessing.CaptureTransform?
0x18ddf4f74  __TEXT,__text  lazy protocol witness table accessor for type [Any.Type] and conformance [A] : Swift.Collection in Swift
0x18ddf4fd8  __TEXT,__text  outlined init with copy of _StringProcessing.DSLTree.QuantificationKind
0x18ddf5034  __TEXT,__text  ___swift_memcpy40_8
0x18ddf5058  __TEXT,__text  merged _StringProcessing._RegexFactory.capture<A, B, C, D where D: _StringProcessing.RegexComponent>(D, Swift.Int?, (B) throws -> C) -> _StringProcessing.Regex<A>
0x18ddf5204  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed (@guaranteed Swift.String, @in_guaranteed _StringProcessing.Processor._StoredCapture) -> (@out Any?, @error @owned Swift.Error) to @escaping @callee_guaranteed (@in_guaranteed Swift.String, @in_guaranteed _Strin
0x18ddf52a0  __TEXT,__text  function signature specialization <Arg[2] = Dead> of generic specialization <Swift._ArrayBuffer<_StringProcessing.Processor.SavePoint>, Swift.EmptyCollection<_StringProcessing.Processor.SavePoint>> of (extension in Swift):Swift._ArrayBufferProtocol.replaceSubrange<A where A1: Swift.Collection, A.Ele
0x18ddf5498  __TEXT,__text  ___swift_memcpy104_8
0x18ddf54c4  __TEXT,__text  ___swift_memcpy24_8
0x18ddf54d8  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.DSLTree.Atom.CharacterClass
0x18ddf5588  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing.DSLTree.Atom
0x18ddf5588  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing.DSLTree.Atom
0x18ddf558c  __TEXT,__text  destructiveInjectEnumTag value witness for (extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)
0x18ddf559c  __TEXT,__text  ___swift_memcpy1_1
0x18ddf55a8  __TEXT,__text  _StringProcessing.CaptureTransform.init<A, B>((A) throws -> B) -> _StringProcessing.CaptureTransform
0x18ddf56f0  __TEXT,__text  ___swift_project_boxed_opaque_existential_0
0x18ddf5720  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.DSLTree.Atom.CharacterClass
0x18ddf57c0  __TEXT,__text  outlined copy of _StringProcessing.CaptureTransform.Closure
0x18ddf57d4  __TEXT,__text  ___swift_memcpy9_8
0x18ddf57e8  __TEXT,__text  (extension in _StringProcessing):_RegexParser.AST.Node.(coalescedChildrenWithDisplay in _82B5E4654D7C852D8E64E11200486B92).getter : [(extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)]
0x18ddf7078  __TEXT,__text  outlined consume of _StringProcessing.DSLTree.Node
0x18ddf70e8  __TEXT,__text  outlined init with copy of _StringProcessing.RangesSequence<_StringProcessing.ZSearcher<Swift.Substring>>
0x18ddf7150  __TEXT,__text  generic specialization <Swift.String, _StringProcessing.RangesSequence<_StringProcessing.ZSearcher<Swift.Substring>>, Swift.String> of (extension in _StringProcessing):Swift.RangeReplaceableCollection._replacing<A, B where A1: Swift.Sequence, B1: Swift.Collection, A.Element == B1.Element, A1.Element
0x18ddf737c  __TEXT,__text  function signature specialization <Arg[1] = Stack Promoted from Box, Arg[2] = Stack Promoted from Box> of tryAccumulateAtom #1 (_RegexParser.AST.Atom) -> Swift.Bool in (extension in _StringProcessing):_RegexParser.AST.Node.(coalescedChildrenWithDisplay in _82B5E4654D7C852D8E64E11200486B92).getter : 
0x18ddf7bb0  __TEXT,__text  generic specialization <Swift.Substring, Swift.String> of (extension in _StringProcessing):Swift.Collection< where A.Element: Swift.Equatable>._ranges<A where A1: Swift.Collection, A.Element == A1.Element>(of: A1) -> _StringProcessing.RangesSequence<_StringProcessing.ZSearcher<A>>
0x18ddf7f74  __TEXT,__text  generic specialization <Swift.String, Swift.String, Swift.String> of (extension in _StringProcessing):Swift.RangeReplaceableCollection< where A: Swift.BidirectionalCollection, A.Swift.Sequence.Element: Swift.Comparable>._replacing<A, B where A1: Swift.Collection, B1: Swift.Collection, A.Swift.Sequen
0x18ddf80a4  __TEXT,__text  generic specialization <serialized, Swift.Character> of Swift._ContiguousArrayBuffer.init(_uninitializedCount: Swift.Int, minimumCapacity: Swift.Int) -> Swift._ContiguousArrayBuffer<A>
0x18ddf8124  __TEXT,__text  type metadata accessor for (extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)
0x18ddf8170  __TEXT,__text  generic specialization <(extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18ddf8198  __TEXT,__text  merged outlined init with take of _StringProcessing.DSLTree._AST.QuantificationKind
0x18ddf81f8  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.RangesSequence
0x18ddf82b8  __TEXT,__text  generic specialization <Swift.Substring> of _StringProcessing.ZSearcher.search(_: A, in: Swift.Range<A.Index>) -> Swift.Range<A.Index>?
0x18ddf85b4  __TEXT,__text  destroy value witness for (extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)
0x18ddf862c  __TEXT,__text  generic specialization <serialized, Swift.String> of (extension in Swift):Swift.Sequence._copySequenceContents(initializing: Swift.UnsafeMutableBufferPointer<A.Element>) -> (A.Iterator, Swift.Int)
0x18ddf86f4  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.ZSearcher
0x18ddf8744  __TEXT,__text  generic not re-abstracted specialization <Swift.Substring, Swift.String> of implicit closure #1 (A.Element, A.Element) -> Swift.Bool in (extension in _StringProcessing):Swift.Collection< where A.Element: Swift.Equatable>._ranges<A where A1: Swift.Collection, A.Element == A1.Element>(of: A1) -> _Stri
0x18ddf8774  __TEXT,__text  generic specialization <Swift.String, Swift.PartialRangeFrom<Swift.String.Index>> of (extension in Swift):Swift.Collection.subscript.getter : <A where A1: Swift.RangeExpression, A.Index == A1.Bound>(A1) -> A.SubSequence
0x18ddf87c0  __TEXT,__text  lazy protocol witness table accessor for type Swift.Substring and conformance Swift.Substring : Swift.Sequence in Swift
0x18ddf8814  __TEXT,__text  generic specialization <Swift.ArraySlice<_StringProcessing.DSLTree.Node>> of (extension in _StringProcessing):Swift.Sequence< where A.Element == _StringProcessing.DSLTree.Node>.wholeMatchType.getter : Any.Type
0x18ddf88c8  __TEXT,__text  generic specialization <[_StringProcessing.DSLTree.Node]> of (extension in _StringProcessing):Swift.Sequence< where A.Element == _StringProcessing.DSLTree.Node>.wholeMatchType.getter : Any.Type
0x18ddf8950  __TEXT,__text  outlined copy of _StringProcessing.DSLTree.Node
0x18ddf89c0  __TEXT,__text  ___swift_closure_destructor.64
0x18ddf89c4  __TEXT,__text  ___swift_closure_destructor.67
0x18ddf89c8  __TEXT,__text  ___swift__destructor.13
0x18ddf89d8  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.DSLTree.CustomCharacterClass
0x18ddf89d8  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.DSLTree.CustomCharacterClass
0x18ddf89d8  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.DSLTree.CustomCharacterClass
0x18ddf89d8  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.DSLTree.CustomCharacterClass
0x18ddf8a20  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.Processor._StoredCapture
0x18ddf8a20  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.Processor._StoredCapture
0x18ddf8a20  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.Processor._StoredCapture
0x18ddf8a20  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.Processor._StoredCapture
0x18ddf8a20  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.Processor._StoredCapture
0x18ddf8a20  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.Processor._StoredCapture
0x18ddf8a20  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.Processor._StoredCapture
0x18ddf8a4c  __TEXT,__text  generic specialization <Swift.Range<Swift.Int>> of (extension in Swift):Swift.RandomAccessCollection.index(_: A.Index, offsetBy: Swift.Int, limitedBy: A.Index) -> A.Index?
0x18ddf8ab4  __TEXT,__text  wrapIfNecessary #1 <A>(A.Type) -> Any.Type in _StringProcessing.AnyRegexOutput.ElementRepresentation.type.getter : Any.Type
0x18ddf8ac0  __TEXT,__text  outlined consume of _StringProcessing.CaptureTransform.Closure
0x18ddf8ad4  __TEXT,__text  ___swift_closure_destructor.3
0x18ddf8b84  __TEXT,__text  partial apply forwarder for reabstraction thunk helper <A, B> from @escaping @callee_guaranteed (@guaranteed Swift.Substring) -> (@out B?, @error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.Substring) -> (@out Any?, @error @owned Swift.Error)
0x18ddf8ba4  __TEXT,__text  reabstraction thunk helper <A, B> from @escaping @callee_guaranteed (@guaranteed Swift.Substring) -> (@out B?, @error @owned Swift.Error) to @escaping @callee_guaranteed (@guaranteed Swift.Substring) -> (@out Any?, @error @owned Swift.Error)
0x18ddf8cf8  __TEXT,__text  outlined destroy of _StringProcessing.SubstringSearcher
0x18ddf8d84  __TEXT,__text  generic specialization <Swift.String.UnicodeScalarView> of (extension in Swift):Swift.Collection.first.getter : A.Element?
0x18ddf8f84  __TEXT,__text  lazy protocol witness table accessor for type _StringProcessing.RegexCompilationError and conformance _StringProcessing.RegexCompilationError : Swift.Error in _StringProcessing
0x18ddf8fd8  __TEXT,__text  generic specialization <_StringProcessing.AnyRegexOutput> of _StringProcessing.Regex.Program.init(ast: _RegexParser.AST) -> _StringProcessing.Regex<A>.Program
0x18ddf9144  __TEXT,__text  generic specialization <Swift.String.Index> of Swift.Set._Variant.insert(__owned A) -> (inserted: Swift.Bool, memberAfterInsert: A)
0x18ddf924c  __TEXT,__text  generic specialization <Swift.String.Index> of Swift._NativeSet.insertNew(_: __owned A, at: Swift._HashTable.Bucket, isUnique: Swift.Bool) -> ()
0x18ddf9398  __TEXT,__text  generic specialization <Swift.String.Index> of Swift._NativeSet.copyAndResize(capacity: Swift.Int) -> ()
0x18ddf9590  __TEXT,__text  generic specialization <Swift.String.Index> of Swift._NativeSet.resize(capacity: Swift.Int) -> ()
0x18ddf97cc  __TEXT,__text  generic specialization <Swift.String.Index> of Swift.Set.contains(A) -> Swift.Bool
0x18ddf9a28  __TEXT,__text  type metadata completion function for _StringProcessing.DSLTree._AST.AbsentFunction
0x18ddf9a40  __TEXT,__text  type metadata completion function for _StringProcessing.DSLTree._AST.ConditionKind
0x18ddf9a58  __TEXT,__text  type metadata completion function for _StringProcessing.DSLTree._AST.MatchingOptionSequence
0x18ddf9a70  __TEXT,__text  _StringProcessing.DSLTree.CustomCharacterClass.Member.asAsciiBitset(_StringProcessing.MatchingOptions, Swift.Bool) -> _StringProcessing.DSLTree.CustomCharacterClass.AsciiBitset?
0x18ddf9f8c  __TEXT,__text  function signature specialization <Arg[3] = Dead> of _StringProcessing.DSLTree.CustomCharacterClass.AsciiBitset.init(Swift.UInt8, Swift.Bool, Swift.Bool) -> _StringProcessing.DSLTree.CustomCharacterClass.AsciiBitset
0x18ddfa00c  __TEXT,__text  _StringProcessing.zAlgorithm<A>(_: [A], by: (A, A) -> Swift.Bool) -> [Swift.Int]
0x18ddfa26c  __TEXT,__text  merged lazy protocol witness table accessor for type Swift.Range<Swift.Int> and conformance < where A: Swift.Strideable, A.Stride: Swift.SignedInteger> Swift.Range<A> : Swift.RandomAccessCollection in Swift
0x18ddfa2e8  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.PatternSegment
0x18ddfa32c  __TEXT,__text  (extension in _StringProcessing):Swift.Collection._split<A where A == A1.Searched, A1: _StringProcessing.CollectionSearcher>(by: A1, maxSplits: Swift.Int, omittingEmptySubsequences: Swift.Bool) -> _StringProcessing.SplitSequence<A1>
0x18ddfa490  __TEXT,__text  _StringProcessing.SplitSequence.init(input: A.Searched, searcher: A, maxSplits: Swift.Int, omittingEmptySubsequences: Swift.Bool) -> _StringProcessing.SplitSequence<A>
0x18ddfa594  __TEXT,__text  (extension in _StringProcessing):Swift.Collection._ranges<A where A == A1.Searched, A1: _StringProcessing.CollectionSearcher>(of: A1) -> _StringProcessing.RangesSequence<A1>
0x18ddfa6e0  __TEXT,__text  _StringProcessing.RangesSequence.init(input: A.Searched, searcher: A) -> _StringProcessing.RangesSequence<A>
0x18ddfa7a8  __TEXT,__text  ___swift_memcpy32_8
0x18ddfa7b4  __TEXT,__text  destroy value witness for _StringProcessing.ZSearcher
0x18ddfa7ec  __TEXT,__text  protocol witness for Swift.Sequence._copyToContiguousArray() -> Swift.ContiguousArray<A.Element> in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18ddfa7ec  __TEXT,__text  protocol witness for Swift.Sequence._copyToContiguousArray() -> Swift.ContiguousArray<A.Element> in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18ddfa7ec  __TEXT,__text  protocol witness for Swift.Sequence._copyToContiguousArray() -> Swift.ContiguousArray<A.Element> in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18ddfa854  __TEXT,__text  function signature specialization <Arg[0] = Owned To Guaranteed> of (extension in Swift):Swift.Sequence._copyToContiguousArray() -> Swift.ContiguousArray<A.Element>
0x18ddfa858  __TEXT,__text  protocol witness for Swift.Sequence.underestimatedCount.getter : Swift.Int in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18ddfa858  __TEXT,__text  protocol witness for Swift.Sequence.underestimatedCount.getter : Swift.Int in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18ddfa858  __TEXT,__text  protocol witness for Swift.Sequence.underestimatedCount.getter : Swift.Int in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18ddfa858  __TEXT,__text  protocol witness for Swift.Sequence.underestimatedCount.getter : Swift.Int in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18ddfa858  __TEXT,__text  protocol witness for Swift.Sequence.underestimatedCount.getter : Swift.Int in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18ddfa860  __TEXT,__text  _StringProcessing.SplitSequence.makeIterator() -> _StringProcessing.SplitSequence<A>.Iterator
0x18ddfa944  __TEXT,__text  protocol witness for Swift.Sequence.makeIterator() -> A.Iterator in conformance _StringProcessing.SplitSequence<A> : Swift.Sequence in _StringProcessing
0x18ddfa990  __TEXT,__text  _StringProcessing.SplitSequence.Iterator.init(ranges: _StringProcessing.RangesSequence<A>, maxSplits: Swift.Int, omittingEmptySubsequences: Swift.Bool) -> _StringProcessing.SplitSequence<A>.Iterator
0x18ddfae98  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.Regex.Match
0x18ddfaf00  __TEXT,__text  destroy value witness for _StringProcessing.DSLTree._AST.ASTNode
0x18ddfaf18  __TEXT,__text  _StringProcessing.ZSearcher.init(pattern: [A.Element], by: (A.Element, A.Element) -> Swift.Bool) -> _StringProcessing.ZSearcher<A>
0x18ddfaf90  __TEXT,__text  _StringProcessing.RangesSequence.makeIterator() -> _StringProcessing.RangesSequence<A>.Iterator
0x18ddfb044  __TEXT,__text  (extension in _StringProcessing):_StringProcessing.StatelessCollectionSearcher.state(for: A.Searched, in: Swift.Range<A.Searched.Index>) -> _StringProcessing.DefaultSearcherState<A.Searched>
0x18ddfb24c  __TEXT,__text  _StringProcessing.DefaultSearcherState.init(position: _StringProcessing.DefaultSearcherState<A>.Position, end: A.Index) -> _StringProcessing.DefaultSearcherState<A>
0x18ddfb328  __TEXT,__text  type metadata accessor for _StringProcessing.DefaultSearcherState
0x18ddfb340  __TEXT,__text  _StringProcessing.RangesSequence.Iterator.init(_StringProcessing.RangesSequence<A>) -> _StringProcessing.RangesSequence<A>.Iterator
0x18ddfb744  __TEXT,__text  protocol witness for _StringProcessing.CollectionSearcher.state(for: A.Searched, in: Swift.Range<A.Searched.Index>) -> A.State in conformance _StringProcessing.ZSearcher<A> : _StringProcessing.CollectionSearcher in _StringProcessing
0x18ddfb7a4  __TEXT,__text  type metadata accessor for _StringProcessing.DefaultSearcherState.Position
0x18ddfb7bc  __TEXT,__text  protocol witness for Swift.IteratorProtocol.next() -> A.Element? in conformance _StringProcessing.SplitSequence<A>.Iterator : Swift.IteratorProtocol in _StringProcessing
0x18ddfb7c0  __TEXT,__text  _StringProcessing.SplitSequence.Iterator.next() -> A.Searched.SubSequence?
0x18ddfbfdc  __TEXT,__text  protocol witness for _StringProcessing.CollectionSearcher.search(A.Searched, inout A.State) -> Swift.Range<A.Searched.Index>? in conformance _StringProcessing.ZSearcher<A> : _StringProcessing.CollectionSearcher in _StringProcessing
0x18ddfc04c  __TEXT,__text  (extension in _StringProcessing):_StringProcessing.StatelessCollectionSearcher.search(A.Searched, inout _StringProcessing.DefaultSearcherState<A.Searched>) -> Swift.Range<A.Searched.Index>?
0x18ddfc768  __TEXT,__text  protocol witness for _StringProcessing.StatelessCollectionSearcher.search(_: A.Searched, in: Swift.Range<A.Searched.Index>) -> Swift.Range<A.Searched.Index>? in conformance _StringProcessing.ZSearcher<A> : _StringProcessing.StatelessCollectionSearcher in _StringProcessing
0x18ddfc77c  __TEXT,__text  _StringProcessing.ZSearcher.search(_: A, in: Swift.Range<A.Index>) -> Swift.Range<A.Index>?
0x18ddfce44  __TEXT,__text  partial apply forwarder for implicit closure #1 (A.Element, A.Element) -> Swift.Bool in (extension in _StringProcessing):Swift.Collection< where A.Element: Swift.Equatable>._firstRangeGeneric<A where A1: Swift.Collection, A.Element == A1.Element>(of: A1) -> Swift.Range<A.Index>?
0x18ddfce44  __TEXT,__text  partial apply forwarder for implicit closure #1 (A.Element, A.Element) -> Swift.Bool in (extension in _StringProcessing):Swift.Collection< where A.Element: Swift.Equatable>._firstRangeGeneric<A where A1: Swift.Collection, A.Element == A1.Element>(of: A1) -> Swift.Range<A.Index>?
0x18ddfce44  __TEXT,__text  partial apply forwarder for implicit closure #1 (A.Element, A.Element) -> Swift.Bool in (extension in _StringProcessing):Swift.Collection< where A.Element: Swift.Equatable>._firstRangeGeneric<A where A1: Swift.Collection, A.Element == A1.Element>(of: A1) -> Swift.Range<A.Index>?
0x18ddfceb0  __TEXT,__text  $defer #1 <A where A: _StringProcessing.CollectionSearcher>() -> () in _StringProcessing.SplitSequence.Iterator.next() -> A.Searched.SubSequence?
0x18ddfcfd0  __TEXT,__text  finish #1 <A where A: _StringProcessing.CollectionSearcher>() -> A.Searched.SubSequence? in _StringProcessing.SplitSequence.Iterator.next() -> A.Searched.SubSequence?
0x18ddfd53c  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.SplitSequence.Iterator
0x18ddfd75c  __TEXT,__text  function signature specialization <Arg[4] = Dead> of _StringProcessing.DSLTree.CustomCharacterClass.AsciiBitset.init(low: Swift.UInt8, high: Swift.UInt8, isInverted: Swift.Bool, isCaseInsensitive: Swift.Bool) -> _StringProcessing.DSLTree.CustomCharacterClass.AsciiBitset
0x18ddfd84c  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.AnyRegexOutput.Element
0x18ddfd920  __TEXT,__text  merged outlined destroy of _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18ddfd978  __TEXT,__text  merged outlined destroy of _StringProcessing.DSLTree.CustomCharacterClass.Member
0x18ddfd9d0  __TEXT,__text  destroy value witness for _StringProcessing.DSLTree._AST.MatchingOptionSequence
0x18ddfda08  __TEXT,__text  type metadata completion function for _StringProcessing.DSLTree._AST.ASTNode
0x18ddfda20  __TEXT,__text  type metadata completion function for _StringProcessing.DSLTree._AST.Atom
0x18ddfda38  __TEXT,__text  type metadata completion function for _StringProcessing.DSLTree._AST.Reference
0x18ddfe6c4  __TEXT,__text  (extension in _StringProcessing):Swift.Collection< where A.Element: Swift.Equatable>._firstRangeGeneric<A where A1: Swift.Collection, A.Element == A1.Element>(of: A1) -> Swift.Range<A.Index>?
0x18ddfebfc  __TEXT,__text  function signature specialization <Arg[7] = Stack Promoted from Box, Arg[8] = Stack Promoted from Box, Arg[9] = Stack Promoted from Box, Arg[10] = Stack Promoted from Box> of compare #1 <A where A: Swift.Collection>(start: A.Index, end: A.Index, minLength: Swift.Int) -> Swift.Range<A.Index>? in _Str
0x18ddff144  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.Regex
0x18ddff144  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.Regex
0x18ddff180  __TEXT,__text  function signature specialization <Arg[2] = Dead> of static _StringProcessing.DSLTree.Node.repeating(Swift.Range<Swift.Int>, _StringProcessing.RegexRepetitionBehavior?) -> _StringProcessing.DSLTree.Node
0x18ddff674  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.Regex
0x18ddff674  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.Regex
0x18de000f4  __TEXT,__text  protocol witness for Swift.Sequence.withContiguousStorageIfAvailable<A>((Swift.UnsafeBufferPointer<A.Element>) throws -> A1) throws -> A1? in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de000f4  __TEXT,__text  protocol witness for Swift.Sequence.withContiguousStorageIfAvailable<A>((Swift.UnsafeBufferPointer<A.Element>) throws -> A1) throws -> A1? in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de000f4  __TEXT,__text  protocol witness for Swift.Sequence.withContiguousStorageIfAvailable<A>((Swift.UnsafeBufferPointer<A.Element>) throws -> A1) throws -> A1? in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de000f4  __TEXT,__text  protocol witness for Swift.Sequence.withContiguousStorageIfAvailable<A>((Swift.UnsafeBufferPointer<A.Element>) throws -> A1) throws -> A1? in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de000f4  __TEXT,__text  protocol witness for Swift.Sequence.withContiguousStorageIfAvailable<A>((Swift.UnsafeBufferPointer<A.Element>) throws -> A1) throws -> A1? in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de00118  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing._CharacterClassModel.Representation : Swift.Equatable in _StringProcessing
0x18de00118  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing._CharacterClassModel.Representation : Swift.Equatable in _StringProcessing
0x18de00118  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing._CharacterClassModel.Representation : Swift.Equatable in _StringProcessing
0x18de00118  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing._CharacterClassModel.Representation : Swift.Equatable in _StringProcessing
0x18de0012c  __TEXT,__text  getEnumTag value witness for _StringProcessing._CharacterClassModel.Representation
0x18de0012c  __TEXT,__text  getEnumTag value witness for _StringProcessing._CharacterClassModel.Representation
0x18de0012c  __TEXT,__text  getEnumTag value witness for _StringProcessing._CharacterClassModel.Representation
0x18de0012c  __TEXT,__text  getEnumTag value witness for _StringProcessing._CharacterClassModel.Representation
0x18de00134  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing.ReferenceID : Swift.Equatable in _StringProcessing
0x18de00134  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing.ReferenceID : Swift.Equatable in _StringProcessing
0x18de00134  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing.ReferenceID : Swift.Equatable in _StringProcessing
0x18de00148  __TEXT,__text  protocol witness for Swift.Sequence._copyContents(initializing: Swift.UnsafeMutableBufferPointer<A.Element>) -> (A.Iterator, Swift.Int) in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de00148  __TEXT,__text  protocol witness for Swift.Sequence._copyContents(initializing: Swift.UnsafeMutableBufferPointer<A.Element>) -> (A.Iterator, Swift.Int) in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de00148  __TEXT,__text  protocol witness for Swift.Sequence._copyContents(initializing: Swift.UnsafeMutableBufferPointer<A.Element>) -> (A.Iterator, Swift.Int) in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de0014c  __TEXT,__text  getEnumTag value witness for (extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)
0x18de00150  __TEXT,__text  __swift_string_processing_getMphIdx
0x18de00270  __TEXT,__text  __swift_string_processing_getScalarBitArrayIdx
0x18de00334  __TEXT,__text  __swift_string_processing_getScript
0x18de003b8  __TEXT,__text  __swift_string_processing_getScriptExtensions
0x18de00424  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for Swift.Range
0x18de00518  __TEXT,__text  destroy value witness for Swift.Range
0x18de005a4  __TEXT,__text  initializeWithCopy value witness for Swift.Range
0x18de00634  __TEXT,__text  assignWithCopy value witness for Swift.Range
0x18de006c4  __TEXT,__text  initializeWithTake value witness for Swift.Range
0x18de00754  __TEXT,__text  assignWithTake value witness for Swift.Range
0x18de007e4  __TEXT,__text  getEnumTagSinglePayload value witness for Swift.Range
0x18de00918  __TEXT,__text  storeEnumTagSinglePayload value witness for Swift.Range
0x18de00b00  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for Swift.Optional
0x18de00c38  __TEXT,__text  destroy value witness for Swift.Optional
0x18de00cd4  __TEXT,__text  initializeWithCopy value witness for Swift.Optional
0x18de00dbc  __TEXT,__text  assignWithCopy value witness for Swift.Optional
0x18de00f24  __TEXT,__text  initializeWithTake value witness for Swift.Optional
0x18de0100c  __TEXT,__text  assignWithTake value witness for Swift.Optional
0x18de01174  __TEXT,__text  getEnumTagSinglePayload value witness for Swift.Optional
0x18de012d0  __TEXT,__text  storeEnumTagSinglePayload value witness for Swift.Optional
0x18de014c4  __TEXT,__text  getEnumTag value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014ec  __TEXT,__text  destructiveProjectEnumData value witness for Swift.Optional
0x18de014f0  __TEXT,__text  destructiveInjectEnumTag value witness for Swift.Optional
0x18de01518  __TEXT,__text  protocol witness for Swift.RawRepresentable.init(rawValue: A.RawValue) -> A? in conformance _StringProcessing._CharacterClassModel.Representation : Swift.RawRepresentable in _StringProcessing
0x18de01544  __TEXT,__text  protocol witness for Swift.RawRepresentable.rawValue.getter : A.RawValue in conformance _StringProcessing._CharacterClassModel.Representation : Swift.RawRepresentable in _StringProcessing
0x18de01544  __TEXT,__text  protocol witness for Swift.RawRepresentable.rawValue.getter : A.RawValue in conformance _StringProcessing._CharacterClassModel.Representation : Swift.RawRepresentable in _StringProcessing
0x18de01544  __TEXT,__text  protocol witness for Swift.RawRepresentable.rawValue.getter : A.RawValue in conformance _StringProcessing._CharacterClassModel.Representation : Swift.RawRepresentable in _StringProcessing
0x18de01550  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance _StringProcessing._CharacterClassModel.Representation : Swift.Hashable in _StringProcessing
0x18de01598  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing._CharacterClassModel.Representation : Swift.Hashable in _StringProcessing
0x18de01598  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing._CharacterClassModel.Representation : Swift.Hashable in _StringProcessing
0x18de01598  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing._CharacterClassModel.Representation : Swift.Hashable in _StringProcessing
0x18de015c4  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance _StringProcessing._CharacterClassModel.Representation : Swift.Hashable in _StringProcessing
0x18de01608  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance _StringProcessing._CharacterClassModel : Swift.Hashable in _StringProcessing
0x18de01690  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing._CharacterClassModel : Swift.Hashable in _StringProcessing
0x18de016f0  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance _StringProcessing._CharacterClassModel : Swift.Hashable in _StringProcessing
0x18de01774  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing._CharacterClassModel : Swift.Equatable in _StringProcessing
0x18de017d8  __TEXT,__text  protocol witness for Swift.CustomStringConvertible.description.getter : Swift.String in conformance _StringProcessing._CharacterClassModel.Representation : Swift.CustomStringConvertible in _StringProcessing
0x18de018e8  __TEXT,__text  _StringProcessing._CharacterClassModel.description.getter : Swift.String
0x18de01a70  __TEXT,__text  protocol witness for Swift.CustomStringConvertible.description.getter : Swift.String in conformance _StringProcessing._CharacterClassModel : Swift.CustomStringConvertible in _StringProcessing
0x18de01aa8  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing._CharacterClassModel.Representation
0x18de01b38  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing._CharacterClassModel.Representation
0x18de01be8  __TEXT,__text  type metadata accessor for _StringProcessing._CharacterClassModel.Representation
0x18de01bf8  __TEXT,__text  ___swift_memcpy4_1
0x18de01c04  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing._CharacterClassModel
0x18de01c48  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing._CharacterClassModel
0x18de01c88  __TEXT,__text  type metadata accessor for _StringProcessing._CharacterClassModel
0x18de01c98  __TEXT,__text  base witness table accessor for Swift.Equatable in _StringProcessing._CharacterClassModel : Swift.Hashable in _StringProcessing
0x18de01c9c  __TEXT,__text  lazy protocol witness table accessor for type _StringProcessing._CharacterClassModel and conformance _StringProcessing._CharacterClassModel : Swift.Equatable in _StringProcessing
0x18de01cf0  __TEXT,__text  base witness table accessor for Swift.Equatable in _StringProcessing._CharacterClassModel.Representation : Swift.Hashable in _StringProcessing
0x18de01cf4  __TEXT,__text  lazy protocol witness table accessor for type _StringProcessing._CharacterClassModel.Representation and conformance _StringProcessing._CharacterClassModel.Representation : Swift.Equatable in _StringProcessing
0x18de01d48  __TEXT,__text  function signature specialization <Arg[2] = Dead> of static _StringProcessing._CharacterClassModel.== infix(_StringProcessing._CharacterClassModel, _StringProcessing._CharacterClassModel) -> Swift.Bool
0x18de01d5c  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.Executor.Matches.Iterator
0x18de020d4  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.Executor.Matches.Iterator
0x18de02414  __TEXT,__text  assignWithCopy value witness for _StringProcessing.Executor.Matches.Iterator
0x18de0282c  __TEXT,__text  initializeWithTake value witness for _StringProcessing.Executor.Matches.Iterator
0x18de02994  __TEXT,__text  assignWithTake value witness for _StringProcessing.Executor.Matches.Iterator
0x18de02ca0  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.Executor.Matches.Iterator
0x18de02cb4  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.Executor.Matches.Iterator
0x18de02cc8  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.Executor.Matches
0x18de02f10  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.Executor.Matches
0x18de03120  __TEXT,__text  assignWithCopy value witness for _StringProcessing.Executor.Matches
0x18de033b0  __TEXT,__text  initializeWithTake value witness for _StringProcessing.Executor.Matches
0x18de034f4  __TEXT,__text  assignWithTake value witness for _StringProcessing.Executor.Matches
0x18de036f0  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.Executor.Matches
0x18de03704  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.Executor.Matches
0x18de03718  __TEXT,__text  associated type witness table accessor for Swift.Sequence.Iterator : Swift.IteratorProtocol in _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de03734  __TEXT,__text  _StringProcessing.Executor.Matches.Iterator.init(program: _StringProcessing.MEProgram, processor: _StringProcessing.Processor, finished: Swift.Bool) -> _StringProcessing.Executor<A>.Matches.Iterator
0x18de037d0  __TEXT,__text  protocol witness for Swift.IteratorProtocol.next() -> A.Element? in conformance _StringProcessing.Executor<A>.Matches.Iterator : Swift.IteratorProtocol in _StringProcessing
0x18de037d4  __TEXT,__text  protocol witness for Swift.Sequence.makeIterator() -> A.Iterator in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de03820  __TEXT,__text  protocol witness for Swift.Sequence._customContainsEquatableElement(A.Element) -> Swift.Bool? in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de03820  __TEXT,__text  protocol witness for Swift.Sequence._customContainsEquatableElement(A.Element) -> Swift.Bool? in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de03820  __TEXT,__text  protocol witness for Swift.Sequence._customContainsEquatableElement(A.Element) -> Swift.Bool? in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de03820  __TEXT,__text  protocol witness for Swift.Sequence._customContainsEquatableElement(A.Element) -> Swift.Bool? in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de03820  __TEXT,__text  protocol witness for Swift.Sequence._customContainsEquatableElement(A.Element) -> Swift.Bool? in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de03820  __TEXT,__text  protocol witness for Swift.Sequence._customContainsEquatableElement(A.Element) -> Swift.Bool? in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de03820  __TEXT,__text  protocol witness for Swift.Sequence._customContainsEquatableElement(A.Element) -> Swift.Bool? in conformance _StringProcessing.Executor<A>.Matches : Swift.Sequence in _StringProcessing
0x18de03828  __TEXT,__text  type metadata instantiation function for _StringProcessing.Executor
0x18de03828  __TEXT,__text  type metadata instantiation function for _StringProcessing.Executor
0x18de03830  __TEXT,__text  type metadata accessor for _StringProcessing.Executor
0x18de03848  __TEXT,__text  _StringProcessing.AnyRegexOutput.Element.existentialOutputComponent(from: Swift.String) -> Any
0x18de03974  __TEXT,__text  (extension in _StringProcessing):(extension in _RegexParser):Swift.Unicode.Script.init(Swift.Unicode.Scalar) -> (extension in _RegexParser):Swift.Unicode.Script
0x18de03a80  __TEXT,__text  static (extension in _StringProcessing):(extension in _RegexParser):Swift.Unicode.Script.extensions(for: Swift.Unicode.Scalar) -> [(extension in _RegexParser):Swift.Unicode.Script]
0x18de03cc0  __TEXT,__text  (extension in _StringProcessing):Swift.Unicode.Scalar.isNFC.getter : Swift.Bool
0x18de03f10  __TEXT,__text  (extension in _StringProcessing):Swift.String.singleNFCScalar.getter : Swift.Unicode.Scalar?
0x18de04120  __TEXT,__text  (extension in _StringProcessing):Swift.String.singleScalar.getter : Swift.Unicode.Scalar?
0x18de041ec  __TEXT,__text  _StringProcessing.Processor.atSimpleBoundary(Swift.Bool, _StringProcessing.MatchingOptions.SemanticLevel) -> Swift.Bool
0x18de043d0  __TEXT,__text  matchesWord #1 (at: Swift.String.Index) -> Swift.Bool in _StringProcessing.Processor.atSimpleBoundary(Swift.Bool, _StringProcessing.MatchingOptions.SemanticLevel) -> Swift.Bool
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047bc  __TEXT,__text  implicit closure #1 (Swift.UnboundedRange_) -> () in (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.firstMatch<A, B where A1 == B1.RegexOutput, B1: _StringProcessing.RegexComponent>(of: B1) -> _StringProcessing.Regex<A1>.Match?
0x18de047c0  __TEXT,__text  dispatch thunk of _StringProcessing.MatchingCollectionSearcher.matchingSearch(A.Searched, inout A.State) -> (range: Swift.Range<A.Searched.Index>, match: A.Match)?
0x18de04d50  __TEXT,__text  lazy protocol witness table accessor for type Swift.Substring and conformance Swift.Substring : Swift.BidirectionalCollection in Swift
0x18de04fe4  __TEXT,__text  merged lazy protocol witness table accessor for type Swift.PartialRangeUpTo<Swift.String.Index> and conformance Swift.PartialRangeUpTo<A> : Swift.RangeExpression in Swift
0x18de04fe4  __TEXT,__text  merged lazy protocol witness table accessor for type Swift.PartialRangeUpTo<Swift.String.Index> and conformance Swift.PartialRangeUpTo<A> : Swift.RangeExpression in Swift
0x18de05028  __TEXT,__text  (extension in _StringProcessing):Swift.Substring._firstRangeSubstring(of: Swift.Substring) -> Swift.Range<Swift.String.Index>?
0x18de05ba4  __TEXT,__text  lazy protocol witness table accessor for type Swift.String and conformance Swift.String : Swift.Collection in Swift
0x18de05bf8  __TEXT,__text  _StringProcessing.SplitSequence.Iterator.input.getter : A.Searched
0x18de05c60  __TEXT,__text  generic specialization <Swift.Substring> of (extension in _StringProcessing):Swift.StringProtocol< where A.SubSequence == Swift.Substring>._split(separator: Swift.Substring, maxSplits: Swift.Int, omittingEmptySubsequences: Swift.Bool) -> [Swift.Substring]
0x18de05ff8  __TEXT,__text  generic specialization <Swift.String.Index> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18de0600c  __TEXT,__text  generic specialization <(extension in _RegexParser):Swift.Unicode.Script> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18de06034  __TEXT,__text  generic specialization <Swift.Character> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18de06138  __TEXT,__text  generic specialization <_StringProcessing.TypedInt<_StringProcessing._InstructionAddress>> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18de0614c  __TEXT,__text  generic specialization <(Swift.String, Swift.Range<Swift.String.Index>) -> Swift.String.Index?> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18de06160  __TEXT,__text  generic specialization <Any.Type> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18de0625c  __TEXT,__text  generic specialization <_StringProcessing.PatternSegment> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x18de06370  __TEXT,__text  generic specialization <_StringProcessing.SubstringSearcher> of Swift._copySequenceToContiguousArray<A where A: Swift.Sequence>(A) -> Swift.ContiguousArray<A.Element>
0x18de0658c  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.SplitSequence
0x18de06718  __TEXT,__text  assignWithCopy value witness for _StringProcessing.SplitSequence
0x18de06814  __TEXT,__text  initializeWithTake value witness for _StringProcessing.SplitSequence
0x18de06910  __TEXT,__text  assignWithTake value witness for _StringProcessing.SplitSequence
0x18de06a0c  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.SplitSequence
0x18de06c1c  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.SplitSequence
0x18de06eec  __TEXT,__text  associated type witness table accessor for Swift.Sequence.Iterator : Swift.IteratorProtocol in _StringProcessing.SplitSequence<A> : Swift.Sequence in _StringProcessing
0x18de06f08  __TEXT,__text  outlined init with copy of _StringProcessing.SubstringSearcher
0x18de06f5c  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.SplitSequence.Iterator
0x18de07284  __TEXT,__text  assignWithCopy value witness for _StringProcessing.SplitSequence.Iterator
0x18de074a4  __TEXT,__text  initializeWithTake value witness for _StringProcessing.SplitSequence.Iterator
0x18de076c4  __TEXT,__text  assignWithTake value witness for _StringProcessing.SplitSequence.Iterator
0x18de078e4  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.SplitSequence.Iterator
0x18de07ca8  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.SplitSequence.Iterator
0x18de0817c  __TEXT,__text  (extension in _StringProcessing):Swift.Collection< where A == A.SubSequence>._trimPrefix<A where A1: _StringProcessing.CollectionConsumer, A.SubSequence == A1.Consumed>(A1) -> ()
0x18de081b0  __TEXT,__text  (extension in _StringProcessing):Swift.RangeReplaceableCollection._trimPrefix<A where A == A1.Consumed, A1: _StringProcessing.CollectionConsumer>(A1) -> ()
0x18de090d4  __TEXT,__text  _StringProcessing.RangesSequence.Iterator.next() -> Swift.Range<A.Searched.Index>?
0x18de09154  __TEXT,__text  protocol witness for Swift.IteratorProtocol.next() -> A.Element? in conformance _StringProcessing.RangesSequence<A>.Iterator : Swift.IteratorProtocol in _StringProcessing
0x18de09158  __TEXT,__text  protocol witness for Swift.Sequence.makeIterator() -> A.Iterator in conformance _StringProcessing.RangesSequence<A> : Swift.Sequence in _StringProcessing
0x18de09170  __TEXT,__text  (extension in _StringProcessing):Swift.Collection< where A.Element: Swift.Equatable>._ranges<A where A1: Swift.Collection, A.Element == A1.Element>(of: A1) -> _StringProcessing.RangesSequence<_StringProcessing.ZSearcher<A>>
0x18de09c58  __TEXT,__text  _StringProcessing.RegexRangesSequence.Iterator.init(matchesBase: _StringProcessing.Executor<A>.Matches.Iterator) -> _StringProcessing.RegexRangesSequence<A>.Iterator
0x18de09cb0  __TEXT,__text  (extension in _StringProcessing):Swift.Collection< where A.SubSequence == Swift.Substring>._ranges<A where A1: _StringProcessing.RegexComponent>(of: A1) -> _StringProcessing.RegexRangesSequence<A1.RegexOutput>
0x18de09ec0  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.RegexRangesSequence
0x18de0a118  __TEXT,__text  assignWithCopy value witness for _StringProcessing.RegexRangesSequence
0x18de0a3b8  __TEXT,__text  initializeWithTake value witness for _StringProcessing.RegexRangesSequence
0x18de0a50c  __TEXT,__text  assignWithTake value witness for _StringProcessing.RegexRangesSequence
0x18de0a71c  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.RegexRangesSequence
0x18de0a730  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.RegexRangesSequence
0x18de0a744  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.RangesSequence
0x18de0a890  __TEXT,__text  assignWithCopy value witness for _StringProcessing.RangesSequence
0x18de0a950  __TEXT,__text  initializeWithTake value witness for _StringProcessing.RangesSequence
0x18de0aa10  __TEXT,__text  assignWithTake value witness for _StringProcessing.RangesSequence
0x18de0aad0  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.RangesSequence
0x18de0acd8  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.RangesSequence
0x18de0af64  __TEXT,__text  associated type witness table accessor for Swift.Sequence.Iterator : Swift.IteratorProtocol in _StringProcessing.RangesSequence<A> : Swift.Sequence in _StringProcessing
0x18de0af80  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.RangesSequence.Iterator
0x18de0b184  __TEXT,__text  destroy value witness for _StringProcessing.RangesSequence.Iterator
0x18de0b2a8  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.RangesSequence.Iterator
0x18de0b3e8  __TEXT,__text  assignWithCopy value witness for _StringProcessing.RangesSequence.Iterator
0x18de0b528  __TEXT,__text  initializeWithTake value witness for _StringProcessing.RangesSequence.Iterator
0x18de0b668  __TEXT,__text  assignWithTake value witness for _StringProcessing.RangesSequence.Iterator
0x18de0b7a8  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.RangesSequence.Iterator
0x18de0ba84  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.RangesSequence.Iterator
0x18de0be68  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.RegexRangesSequence.Iterator
0x18de0c1ec  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.RegexRangesSequence.Iterator
0x18de0c554  __TEXT,__text  assignWithCopy value witness for _StringProcessing.RegexRangesSequence.Iterator
0x18de0c97c  __TEXT,__text  initializeWithTake value witness for _StringProcessing.RegexRangesSequence.Iterator
0x18de0caf4  __TEXT,__text  assignWithTake value witness for _StringProcessing.RegexRangesSequence.Iterator
0x18de0ce10  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.RegexRangesSequence.Iterator
0x18de0ce24  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.RegexRangesSequence.Iterator
0x18de0ce38  __TEXT,__text  protocol witness for Swift.Sequence._copyContents(initializing: Swift.UnsafeMutableBufferPointer<A.Element>) -> (A.Iterator, Swift.Int) in conformance _StringProcessing.RegexRangesSequence<A> : Swift.Sequence in _StringProcessing
0x18de0ce38  __TEXT,__text  protocol witness for Swift.Sequence._copyContents(initializing: Swift.UnsafeMutableBufferPointer<A.Element>) -> (A.Iterator, Swift.Int) in conformance _StringProcessing.RegexRangesSequence<A> : Swift.Sequence in _StringProcessing
0x18de0ce3c  __TEXT,__text  protocol witness for Swift.Sequence.withContiguousStorageIfAvailable<A>((Swift.UnsafeBufferPointer<A.Element>) throws -> A1) throws -> A1? in conformance _StringProcessing.RegexRangesSequence<A> : Swift.Sequence in _StringProcessing
0x18de0ce3c  __TEXT,__text  protocol witness for Swift.Sequence.withContiguousStorageIfAvailable<A>((Swift.UnsafeBufferPointer<A.Element>) throws -> A1) throws -> A1? in conformance _StringProcessing.RegexRangesSequence<A> : Swift.Sequence in _StringProcessing
0x18de0ce54  __TEXT,__text  protocol witness for Swift.Sequence._copyToContiguousArray() -> Swift.ContiguousArray<A.Element> in conformance _StringProcessing.RegexRangesSequence<A> : Swift.Sequence in _StringProcessing
0x18de0ce54  __TEXT,__text  protocol witness for Swift.Sequence._copyToContiguousArray() -> Swift.ContiguousArray<A.Element> in conformance _StringProcessing.RegexRangesSequence<A> : Swift.Sequence in _StringProcessing
0x18de0ce58  __TEXT,__text  assignWithCopy value witness for _StringProcessing.SubstringSearcher
0x18de0cf18  __TEXT,__text  ___swift_memcpy89_8
0x18de0cf3c  __TEXT,__text  assignWithTake value witness for _StringProcessing.SubstringSearcher
0x18de0cfb4  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.SubstringSearcher
0x18de0cff8  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.SubstringSearcher
0x18de0d050  __TEXT,__text  generic specialization <_StringProcessing.SubstringSearcher> of (extension in Swift):Swift.Sequence._copyContents(initializing: Swift.UnsafeMutableBufferPointer<A.Element>) -> (A.Iterator, Swift.Int)
0x18de0d164  __TEXT,__text  protocol witness for Swift.Sequence.makeIterator() -> A.Iterator in conformance _StringProcessing.SubstringSearcher : Swift.Sequence in _StringProcessing
0x18de0d188  __TEXT,__text  protocol witness for Swift.Sequence._copyToContiguousArray() -> Swift.ContiguousArray<A.Element> in conformance _StringProcessing.SubstringSearcher : Swift.Sequence in _StringProcessing
0x18de0d1e4  __TEXT,__text  protocol witness for Swift.Sequence._copyContents(initializing: Swift.UnsafeMutableBufferPointer<A.Element>) -> (A.Iterator, Swift.Int) in conformance _StringProcessing.SubstringSearcher : Swift.Sequence in _StringProcessing
0x18de0d230  __TEXT,__text  protocol witness for Swift.IteratorProtocol.next() -> A.Element? in conformance _StringProcessing.SubstringSearcher : Swift.IteratorProtocol in _StringProcessing
0x18de0d2d0  __TEXT,__text  associated type witness table accessor for Swift.Sequence.Iterator : Swift.IteratorProtocol in _StringProcessing.SubstringSearcher : Swift.Sequence in _StringProcessing
0x18de0d2d4  __TEXT,__text  lazy protocol witness table accessor for type _StringProcessing.SubstringSearcher and conformance _StringProcessing.SubstringSearcher : Swift.IteratorProtocol in _StringProcessing
0x18de0d328  __TEXT,__text  protocol witness for _StringProcessing.CollectionSearcher.state(for: A.Searched, in: Swift.Range<A.Searched.Index>) -> A.State in conformance _StringProcessing.SubstringSearcher : _StringProcessing.CollectionSearcher in _StringProcessing
0x18de0d3cc  __TEXT,__text  protocol witness for _StringProcessing.CollectionSearcher.search(A.Searched, inout A.State) -> Swift.Range<A.Searched.Index>? in conformance _StringProcessing.SubstringSearcher : _StringProcessing.CollectionSearcher in _StringProcessing
0x18de0d44c  __TEXT,__text  generic specialization <_StringProcessing.ReferenceID> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(A) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x18de0d4ac  __TEXT,__text  generic specialization <_StringProcessing.ReferenceID> of Swift.__RawDictionaryStorage.find<A where A: Swift.Hashable>(_: A, hashValue: Swift.Int) -> (bucket: Swift._HashTable.Bucket, found: Swift.Bool)
0x18de0d518  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.SubstringSearcher.State
0x18de0d558  __TEXT,__text  assignWithCopy value witness for _StringProcessing.SubstringSearcher.State
0x18de0d5b8  __TEXT,__text  ___swift_memcpy25_8
0x18de0d5cc  __TEXT,__text  assignWithTake value witness for _StringProcessing.SubstringSearcher.State
0x18de0d614  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.SubstringSearcher.State
0x18de0d658  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.SubstringSearcher.State
0x18de0d69c  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.SubstringSearcher
0x18de0d69c  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.SubstringSearcher
0x18de0d69c  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.SubstringSearcher
0x18de0d69c  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.SubstringSearcher
0x18de0d6a0  __TEXT,__text  dispatch thunk of _StringProcessing.CollectionSearcher.state(for: A.Searched, in: Swift.Range<A.Searched.Index>) -> A.State
0x18de0d6b4  __TEXT,__text  dispatch thunk of _StringProcessing.CollectionSearcher.search(A.Searched, inout A.State) -> Swift.Range<A.Searched.Index>?
0x18de0d6c8  __TEXT,__text  dispatch thunk of _StringProcessing.StatelessCollectionSearcher.search(_: A.Searched, in: Swift.Range<A.Searched.Index>) -> Swift.Range<A.Searched.Index>?
0x18de0d6dc  __TEXT,__text  type metadata completion function for _StringProcessing.DefaultSearcherState
0x18de0d7a8  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.DefaultSearcherState
0x18de0d92c  __TEXT,__text  destroy value witness for _StringProcessing.DefaultSearcherState
0x18de0da00  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.DefaultSearcherState
0x18de0db40  __TEXT,__text  assignWithCopy value witness for _StringProcessing.DefaultSearcherState
0x18de0dce8  __TEXT,__text  initializeWithTake value witness for _StringProcessing.DefaultSearcherState
0x18de0de28  __TEXT,__text  assignWithTake value witness for _StringProcessing.DefaultSearcherState
0x18de0dfd0  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.DefaultSearcherState
0x18de0e194  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.DefaultSearcherState
0x18de0e3d0  __TEXT,__text  type metadata completion function for _StringProcessing.DefaultSearcherState.Position
0x18de0e448  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.DefaultSearcherState.Position
0x18de0e59c  __TEXT,__text  destroy value witness for _StringProcessing.DefaultSearcherState.Position
0x18de0e64c  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.DefaultSearcherState.Position
0x18de0e740  __TEXT,__text  assignWithCopy value witness for _StringProcessing.DefaultSearcherState.Position
0x18de0e8b4  __TEXT,__text  initializeWithTake value witness for _StringProcessing.DefaultSearcherState.Position
0x18de0e9a8  __TEXT,__text  assignWithTake value witness for _StringProcessing.DefaultSearcherState.Position
0x18de0eb1c  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.DefaultSearcherState.Position
0x18de0ec9c  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.DefaultSearcherState.Position
0x18de0eeb0  __TEXT,__text  getEnumTag value witness for _StringProcessing.DefaultSearcherState.Position
0x18de0ef1c  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing.DefaultSearcherState.Position
0x18de0ef8c  __TEXT,__text  assignWithCopy value witness for _StringProcessing.ZSearcher
0x18de0f004  __TEXT,__text  assignWithTake value witness for _StringProcessing.ZSearcher
0x18de0f054  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.ZSearcher
0x18de0f098  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.ZSearcher
0x18de0f0d8  __TEXT,__text  instantiation function for generic protocol witness table for _StringProcessing.ZSearcher<A> : _StringProcessing.StatelessCollectionSearcher in _StringProcessing
0x18de0f114  __TEXT,__text  associated type witness table accessor for _StringProcessing.CollectionSearcher.Searched : Swift.Collection in _StringProcessing.ZSearcher<A> : _StringProcessing.CollectionSearcher in _StringProcessing
0x18de0f11c  __TEXT,__text  function signature specialization <Arg[4] = Stack Promoted from Box, Arg[5] = Stack Promoted from Box, Arg[6] = Stack Promoted from Box> of compare #1 <A>(start: Swift.Int, minLength: Swift.Int) -> () in _StringProcessing.zAlgorithm<A>(_: [A], by: (A, A) -> Swift.Bool) -> [Swift.Int]
0x18de0f374  __TEXT,__text  dispatch thunk of _StringProcessing.CollectionConsumer.consuming(_: A.Consumed, in: Swift.Range<A.Consumed.Index>) -> A.Consumed.Index?
0x18de0f388  __TEXT,__text  (extension in _StringProcessing):_StringProcessing.CollectionConsumer.consume< where A.Consumed == A.Consumed.SubSequence>(inout A.Consumed) -> Swift.Bool
0x18de0f77c  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for _StringProcessing.FixedPatternConsumer
0x18de0f820  __TEXT,__text  initializeWithCopy value witness for _StringProcessing.FixedPatternConsumer
0x18de0f868  __TEXT,__text  assignWithCopy value witness for _StringProcessing.FixedPatternConsumer
0x18de0f8b0  __TEXT,__text  initializeWithTake value witness for _StringProcessing.FixedPatternConsumer
0x18de0f8f8  __TEXT,__text  assignWithTake value witness for _StringProcessing.FixedPatternConsumer
0x18de0f940  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.FixedPatternConsumer
0x18de0fa64  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.FixedPatternConsumer
0x18de10314  __TEXT,__text  merged _StringProcessing.RegexSemanticLevel.hashValue.getter : Swift.Int
0x18de10314  __TEXT,__text  merged _StringProcessing.RegexSemanticLevel.hashValue.getter : Swift.Int
0x18de10314  __TEXT,__text  merged _StringProcessing.RegexSemanticLevel.hashValue.getter : Swift.Int
0x18de10314  __TEXT,__text  merged _StringProcessing.RegexSemanticLevel.hashValue.getter : Swift.Int
0x18de1035c  __TEXT,__text  merged protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance _StringProcessing.RegexSemanticLevel.Representation : Swift.Hashable in _StringProcessing
0x18de1035c  __TEXT,__text  merged protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance _StringProcessing.RegexSemanticLevel.Representation : Swift.Hashable in _StringProcessing
0x18de1035c  __TEXT,__text  merged protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance _StringProcessing.RegexSemanticLevel.Representation : Swift.Hashable in _StringProcessing
0x18de103a0  __TEXT,__text  base witness table accessor for Swift.Equatable in _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de103a4  __TEXT,__text  lazy protocol witness table accessor for type _StringProcessing.RegexSemanticLevel and conformance _StringProcessing.RegexSemanticLevel : Swift.Equatable in _StringProcessing
0x18de103f8  __TEXT,__text  base witness table accessor for Swift.Equatable in _StringProcessing.RegexWordBoundaryKind : Swift.Hashable in _StringProcessing
0x18de103fc  __TEXT,__text  lazy protocol witness table accessor for type _StringProcessing.RegexWordBoundaryKind and conformance _StringProcessing.RegexWordBoundaryKind : Swift.Equatable in _StringProcessing
0x18de10450  __TEXT,__text  base witness table accessor for Swift.Equatable in _StringProcessing.RegexRepetitionBehavior : Swift.Hashable in _StringProcessing
0x18de10454  __TEXT,__text  lazy protocol witness table accessor for type _StringProcessing.RegexRepetitionBehavior and conformance _StringProcessing.RegexRepetitionBehavior : Swift.Equatable in _StringProcessing
0x18de104c8  __TEXT,__text  merged getEnumTagSinglePayload value witness for _StringProcessing.RegexRepetitionBehavior
0x18de104c8  __TEXT,__text  merged getEnumTagSinglePayload value witness for _StringProcessing.RegexRepetitionBehavior
0x18de10558  __TEXT,__text  type metadata accessor for _StringProcessing.RegexRepetitionBehavior.Kind
0x18de10568  __TEXT,__text  type metadata accessor for _StringProcessing.RegexWordBoundaryKind.Representation
0x18de10578  __TEXT,__text  merged getEnumTagSinglePayload value witness for _StringProcessing.RegexSemanticLevel
0x18de10578  __TEXT,__text  merged getEnumTagSinglePayload value witness for _StringProcessing.RegexSemanticLevel
0x18de10578  __TEXT,__text  merged getEnumTagSinglePayload value witness for _StringProcessing.RegexSemanticLevel
0x18de10608  __TEXT,__text  merged storeEnumTagSinglePayload value witness for _StringProcessing.RegexSemanticLevel
0x18de10608  __TEXT,__text  merged storeEnumTagSinglePayload value witness for _StringProcessing.RegexSemanticLevel
0x18de10608  __TEXT,__text  merged storeEnumTagSinglePayload value witness for _StringProcessing.RegexSemanticLevel
0x18de106b8  __TEXT,__text  type metadata accessor for _StringProcessing.RegexSemanticLevel.Representation
0x18de106c8  __TEXT,__text  base witness table accessor for Swift.Equatable in _StringProcessing.RegexSemanticLevel.Representation : Swift.Hashable in _StringProcessing
0x18de106cc  __TEXT,__text  lazy protocol witness table accessor for type _StringProcessing.RegexSemanticLevel.Representation and conformance _StringProcessing.RegexSemanticLevel.Representation : Swift.Equatable in _StringProcessing
0x18de10720  __TEXT,__text  base witness table accessor for Swift.Equatable in _StringProcessing.RegexWordBoundaryKind.Representation : Swift.Hashable in _StringProcessing
0x18de10724  __TEXT,__text  lazy protocol witness table accessor for type _StringProcessing.RegexWordBoundaryKind.Representation and conformance _StringProcessing.RegexWordBoundaryKind.Representation : Swift.Equatable in _StringProcessing
0x18de10778  __TEXT,__text  base witness table accessor for Swift.Equatable in _StringProcessing.RegexRepetitionBehavior.Kind : Swift.Hashable in _StringProcessing
0x18de1077c  __TEXT,__text  lazy protocol witness table accessor for type _StringProcessing.RegexRepetitionBehavior.Kind and conformance _StringProcessing.RegexRepetitionBehavior.Kind : Swift.Equatable in _StringProcessing
0x18de107d0  __TEXT,__text  getEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18de107d0  __TEXT,__text  getEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18de107d0  __TEXT,__text  getEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18de107d0  __TEXT,__text  getEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18de107d0  __TEXT,__text  getEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18de107d0  __TEXT,__text  getEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18de107d0  __TEXT,__text  getEnumTag value witness for _StringProcessing.RegexRepetitionBehavior.Kind
0x18de107d4  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing.RegexSemanticLevel : Swift.Equatable in _StringProcessing
0x18de107d4  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing.RegexSemanticLevel : Swift.Equatable in _StringProcessing
0x18de107d4  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing.RegexSemanticLevel : Swift.Equatable in _StringProcessing
0x18de107d4  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing.RegexSemanticLevel : Swift.Equatable in _StringProcessing
0x18de107d4  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing.RegexSemanticLevel : Swift.Equatable in _StringProcessing
0x18de107d4  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing.RegexSemanticLevel : Swift.Equatable in _StringProcessing
0x18de107d4  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing.RegexSemanticLevel : Swift.Equatable in _StringProcessing
0x18de107d4  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing.RegexSemanticLevel : Swift.Equatable in _StringProcessing
0x18de107d4  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing.RegexSemanticLevel : Swift.Equatable in _StringProcessing
0x18de107d4  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance _StringProcessing.RegexSemanticLevel : Swift.Equatable in _StringProcessing
0x18de107d8  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107d8  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107d8  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107d8  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107d8  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107d8  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107dc  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.RegexWordBoundaryKind
0x18de107dc  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.RegexWordBoundaryKind
0x18de107dc  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.RegexWordBoundaryKind
0x18de107dc  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.RegexWordBoundaryKind
0x18de107e8  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107e8  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107e8  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107e8  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107e8  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107e8  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107fc  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107fc  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107fc  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107fc  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107fc  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de107fc  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance _StringProcessing.RegexSemanticLevel : Swift.Hashable in _StringProcessing
0x18de10800  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.RegexWordBoundaryKind
0x18de10800  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.RegexWordBoundaryKind
0x18de10800  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.RegexWordBoundaryKind
0x18de10800  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.RegexWordBoundaryKind
0x18de10804  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.RegexRepetitionBehavior
0x18de10804  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.RegexRepetitionBehavior
0x18de10878  __TEXT,__text  merged (extension in _StringProcessing):Swift.BidirectionalCollection< where A.SubSequence == Swift.Substring>.wholeMatch<A where A1: _StringProcessing.RegexComponent>(of: A1) -> _StringProcessing.Regex<A1.RegexOutput>.Match?
0x18de109b0  __TEXT,__text  generic specialization <Swift.String> of Swift.ContiguousArray._createNewBuffer(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> ()
0x18de109d0  __TEXT,__text  ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
0x18de10a2c  __TEXT,__text  generic specialization <Swift.String> of Swift._ContiguousArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ContiguousArrayBuffer<A>
0x18de10b2c  __TEXT,__text  assignWithCopy value witness for _StringProcessing.Regex.Match
0x18de10ba4  __TEXT,__text  assignWithTake value witness for _StringProcessing.Regex.Match
0x18de10c1c  __TEXT,__text  _StringProcessing.Regex.Program.__allocating_init(ast: _RegexParser.AST) -> _StringProcessing.Regex<A>.Program
0x18de10dd4  __TEXT,__text  _StringProcessing.Regex.Program.(ProgramBox in _45BE7334FC47A99CAE19728A97C42F4D).__allocating_init(_StringProcessing.MEProgram) -> _StringProcessing.Regex<A>.Program.(ProgramBox in _45BE7334FC47A99CAE19728A97C42F4D)
0x18de10e20  __TEXT,__text  _StringProcessing.Regex.Program.__allocating_init(list: _StringProcessing.DSLList) -> _StringProcessing.Regex<A>.Program
0x18de10e68  __TEXT,__text  _StringProcessing.Regex.Program.init(list: _StringProcessing.DSLList) -> _StringProcessing.Regex<A>.Program
0x18de10e7c  __TEXT,__text  _StringProcessing.Regex.Program.deinit
0x18de10fc0  __TEXT,__text  ___swift_assignWithCopy_strong
0x18de10ff8  __TEXT,__text  ___swift_assignWithTake_strong
0x18de1102c  __TEXT,__text  getEnumTagSinglePayload value witness for _StringProcessing.Regex._RegexInternalAction
0x18de1104c  __TEXT,__text  storeEnumTagSinglePayload value witness for _StringProcessing.Regex._RegexInternalAction
0x18de1107c  __TEXT,__text  getEnumTag value witness for _StringProcessing.Regex._RegexInternalAction
0x18de11098  __TEXT,__text  destructiveInjectEnumTag value witness for _StringProcessing.Regex._RegexInternalAction
0x18de110d0  __TEXT,__text  generic specialization <Swift.String.Index> of Swift._ArrayBuffer._consumeAndCreateNew() -> Swift._ArrayBuffer<A>
0x18de110e4  __TEXT,__text  generic specialization <_StringProcessing.Processor.SavePoint> of Swift._ArrayBuffer._consumeAndCreateNew() -> Swift._ArrayBuffer<A>
0x18de110f8  __TEXT,__text  generic specialization <_StringProcessing.TypedInt<_StringProcessing._InstructionAddress>?> of Swift._ArrayBuffer._consumeAndCreateNew() -> Swift._ArrayBuffer<A>
0x18de1110c  __TEXT,__text  flatten #1 (_RegexParser.AST.Node) -> [_RegexParser.AST.Node] in (extension in _StringProcessing):_RegexParser.AST.Node.(coalescedChildrenWithDisplay in _82B5E4654D7C852D8E64E11200486B92).getter : [(extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E112004
0x18de11498  __TEXT,__text  generic specialization <_StringProcessing.AnyRegexOutput> of (extension in Swift):Swift.RandomAccessCollection.index(_: A.Index, offsetBy: Swift.Int, limitedBy: A.Index) -> A.Index?
0x18de11504  __TEXT,__text  lazy protocol witness table accessor for type Swift.UInt32 and conformance Swift.UInt32 : Swift.BinaryInteger in Swift
0x18de11558  __TEXT,__text  ___swift__destructor.18
0x18de1158c  __TEXT,__text  initializeBufferWithCopyOfBuffer value witness for (extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)
0x18de1167c  __TEXT,__text  initializeWithCopy value witness for (extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)
0x18de1172c  __TEXT,__text  assignWithCopy value witness for (extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)
0x18de117fc  __TEXT,__text  outlined destroy of (extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)
0x18de11850  __TEXT,__text  initializeWithTake value witness for (extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)
0x18de1190c  __TEXT,__text  assignWithTake value witness for (extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)
0x18de119d8  __TEXT,__text  getEnumTagSinglePayload value witness for (extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)
0x18de119d8  __TEXT,__text  getEnumTagSinglePayload value witness for (extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)
0x18de119f8  __TEXT,__text  storeEnumTagSinglePayload value witness for (extension in _StringProcessing):_RegexParser.AST.Node.(CoalescedChild in _82B5E4654D7C852D8E64E11200486B92)
```
First 1,000 of 1,990.

