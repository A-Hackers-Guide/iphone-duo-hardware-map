# Symbols: `/usr/lib/swift/libswiftos.dylib`

Symbol table of this image in the iOS 27.2 dyld shared cache (`ipsw dyld macho -n --demangle`). The class-level view is on the [image page](../userland/usr__lib__swift__libswiftos.dylib.md). **[DSC]**

748 public symbols, 737 private symbols, 0 undefined (imported).

## Public (external)

```
0x19e6c7b80  __TEXT,__text  os.os_log(_: __C.os_log_type_t, log: __C.OS_os_log, _: os.OSLogMessage) -> ()
0x19e6b867c  __TEXT,__text  os.os_log(_: Swift.StaticString, dso: Swift.UnsafeRawPointer?, log: __C.OS_os_log, type: __C.os_log_type_t, _: Swift.CVarArg...) -> ()
0x19e6b9c00  __TEXT,__text  os.os_log(_: __C.os_log_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, _: Swift.StaticString, _: Swift.CVarArg...) -> ()
0x19e6be978  __TEXT,__text  os.os_signpost(_: os.OSSignpostAnimationBegin, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name: Swift.StaticString, signpostID: os.OSSignpostID, _: os.AnimationFormatString.OSLogMessage, _: Swift.CVarArg...) -> ()
0x19e6b8134  __TEXT,__text  os.os_signpost(_: __C.os_signpost_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name: Swift.StaticString, signpostID: os.OSSignpostID, _: Swift.StaticString, _: Swift.CVarArg...) -> ()
0x19e6be9a0  __TEXT,__text  os.os_signpost(_: os.OSSignpostAnimationBegin, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name: Swift.StaticString, signpostID: os.OSSignpostID) -> ()
0x19e6ba21c  __TEXT,__text  os.os_signpost(_: __C.os_signpost_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name: Swift.StaticString, signpostID: os.OSSignpostID) -> ()
0x19e6c3830  __TEXT,__text  os.OSLogMessage.bufferSize.getter : Swift.Int
0x19e6ceed0  __TEXT,__const  property descriptor for os.OSLogMessage.bufferSize : Swift.Int
0x19e6c373c  __TEXT,__text  os.OSLogMessage.interpolation.getter : os.OSLogInterpolation
0x19e6ceee8  __TEXT,__const  property descriptor for os.OSLogMessage.interpolation : os.OSLogInterpolation
0x19e6c3748  __TEXT,__text  os.OSLogMessage.init(stringLiteral: Swift.String) -> os.OSLogMessage
0x19e6c2f20  __TEXT,__text  os.OSLogMessage.init(stringInterpolation: os.OSLogInterpolation) -> os.OSLogMessage
0x19e6c3f50  __TEXT,__text  type metadata accessor for os.OSLogMessage
0x19e6d09c0  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogMessage
0x1e4202278  __AUTH_CONST,__const  type metadata for os.OSLogMessage
0x19e6cee10  __TEXT,__const  protocol conformance descriptor for os.OSLogMessage : Swift.ExpressibleByStringLiteral in os
0x19e6cedd0  __TEXT,__const  protocol conformance descriptor for os.OSLogMessage : Swift.ExpressibleByStringInterpolation in os
0x19e6cee90  __TEXT,__const  protocol conformance descriptor for os.OSLogMessage : Swift.ExpressibleByUnicodeScalarLiteral in os
0x19e6cee50  __TEXT,__const  protocol conformance descriptor for os.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6c5490  __TEXT,__text  os.OSLogPrivacy.needsPrivacySpecifier.getter : Swift.Bool
0x19e6cf1b8  __TEXT,__const  property descriptor for os.OSLogPrivacy.needsPrivacySpecifier : Swift.Bool
0x19e6c589c  __TEXT,__text  static os.OSLogPrivacy.PrivacyOption.== infix(os.OSLogPrivacy.PrivacyOption, os.OSLogPrivacy.PrivacyOption) -> Swift.Bool
0x19e6cf20c  __TEXT,__const  enum case for os.OSLogPrivacy.PrivacyOption.auto(os.OSLogPrivacy.PrivacyOption.Type) -> os.OSLogPrivacy.PrivacyOption
0x19e6c58b0  __TEXT,__text  os.OSLogPrivacy.PrivacyOption.hash(into: inout Swift.Hasher) -> ()
0x19e6cf204  __TEXT,__const  enum case for os.OSLogPrivacy.PrivacyOption.public(os.OSLogPrivacy.PrivacyOption.Type) -> os.OSLogPrivacy.PrivacyOption
0x19e6cf200  __TEXT,__const  enum case for os.OSLogPrivacy.PrivacyOption.private(os.OSLogPrivacy.PrivacyOption.Type) -> os.OSLogPrivacy.PrivacyOption
0x19e6c58dc  __TEXT,__text  os.OSLogPrivacy.PrivacyOption.hashValue.getter : Swift.Int
0x19e6cf1b8  __TEXT,__const  property descriptor for os.OSLogPrivacy.PrivacyOption.hashValue : Swift.Int
0x19e6cf208  __TEXT,__const  enum case for os.OSLogPrivacy.PrivacyOption.sensitive(os.OSLogPrivacy.PrivacyOption.Type) -> os.OSLogPrivacy.PrivacyOption
0x19e6c5f04  __TEXT,__text  type metadata accessor for os.OSLogPrivacy.PrivacyOption
0x19e6d0a30  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogPrivacy.PrivacyOption
0x1e4202200  __AUTH_CONST,__const  type metadata for os.OSLogPrivacy.PrivacyOption
0x19e6cf0a8  __TEXT,__const  protocol conformance descriptor for os.OSLogPrivacy.PrivacyOption : Swift.Hashable in os
0x19e6cf080  __TEXT,__const  protocol conformance descriptor for os.OSLogPrivacy.PrivacyOption : Swift.Equatable in os
0x19e6c53e8  __TEXT,__text  os.OSLogPrivacy.argumentFlag.getter : Swift.UInt8
0x19e6cf1b8  __TEXT,__const  property descriptor for os.OSLogPrivacy.argumentFlag : Swift.UInt8
0x19e6c5b54  __TEXT,__text  os.OSLogPrivacy.maskSpecifier.getter : Swift.String
0x19e6cf1b8  __TEXT,__const  property descriptor for os.OSLogPrivacy.maskSpecifier : Swift.String
0x19e6c5444  __TEXT,__text  os.OSLogPrivacy.isAtleastPrivate.getter : Swift.Bool
0x19e6cf1b8  __TEXT,__const  property descriptor for os.OSLogPrivacy.isAtleastPrivate : Swift.Bool
0x19e6c54e0  __TEXT,__text  os.OSLogPrivacy.privacySpecifier.getter : Swift.String?
0x19e6cf1b8  __TEXT,__const  property descriptor for os.OSLogPrivacy.privacySpecifier : Swift.String?
0x19e6cf230  __TEXT,__const  enum case for os.OSLogPrivacy.Mask._mailAccount(os.OSLogPrivacy.Mask.Type) -> os.OSLogPrivacy.Mask
0x19e6cf224  __TEXT,__const  enum case for os.OSLogPrivacy.Mask._mailAddress(os.OSLogPrivacy.Mask.Type) -> os.OSLogPrivacy.Mask
0x19e6cf228  __TEXT,__const  enum case for os.OSLogPrivacy.Mask._mailSubject(os.OSLogPrivacy.Mask.Type) -> os.OSLogPrivacy.Mask
0x19e6cf22c  __TEXT,__const  enum case for os.OSLogPrivacy.Mask._mailSummary(os.OSLogPrivacy.Mask.Type) -> os.OSLogPrivacy.Mask
0x19e6cf238  __TEXT,__const  enum case for os.OSLogPrivacy.Mask._mailboxPath(os.OSLogPrivacy.Mask.Type) -> os.OSLogPrivacy.Mask
0x19e6cf23c  __TEXT,__const  enum case for os.OSLogPrivacy.Mask._mailAttachmentFileName(os.OSLogPrivacy.Mask.Type) -> os.OSLogPrivacy.Mask
0x19e6c61c4  __TEXT,__text  static os.OSLogPrivacy.Mask.== infix(os.OSLogPrivacy.Mask, os.OSLogPrivacy.Mask) -> Swift.Bool
0x19e6c61b4  __TEXT,__text  os.OSLogPrivacy.Mask.hash(into: inout Swift.Hasher) -> ()
0x19e6cf218  __TEXT,__const  enum case for os.OSLogPrivacy.Mask.hash(os.OSLogPrivacy.Mask.Type) -> os.OSLogPrivacy.Mask
0x19e6cf21c  __TEXT,__const  enum case for os.OSLogPrivacy.Mask.none(os.OSLogPrivacy.Mask.Type) -> os.OSLogPrivacy.Mask
0x19e6cf234  __TEXT,__const  enum case for os.OSLogPrivacy.Mask._mailbox(os.OSLogPrivacy.Mask.Type) -> os.OSLogPrivacy.Mask
0x19e6cf220  __TEXT,__const  enum case for os.OSLogPrivacy.Mask._mailName(os.OSLogPrivacy.Mask.Type) -> os.OSLogPrivacy.Mask
0x19e6c61bc  __TEXT,__text  os.OSLogPrivacy.Mask.hashValue.getter : Swift.Int
0x19e6cf1b8  __TEXT,__const  property descriptor for os.OSLogPrivacy.Mask.hashValue : Swift.Int
0x19e6c6054  __TEXT,__text  type metadata accessor for os.OSLogPrivacy.Mask
0x19e6d0a4c  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogPrivacy.Mask
0x1e4202170  __AUTH_CONST,__const  type metadata for os.OSLogPrivacy.Mask
0x19e6cf110  __TEXT,__const  protocol conformance descriptor for os.OSLogPrivacy.Mask : Swift.Hashable in os
0x19e6cf0e8  __TEXT,__const  protocol conformance descriptor for os.OSLogPrivacy.Mask : Swift.Equatable in os
0x19e6c5b04  __TEXT,__text  static os.OSLogPrivacy.auto(mask: os.OSLogPrivacy.Mask) -> os.OSLogPrivacy
0x19e6ba7c8  __TEXT,__text  static os.OSLogPrivacy.auto.getter : os.OSLogPrivacy
0x19e6cf1b8  __TEXT,__const  property descriptor for static os.OSLogPrivacy.auto : os.OSLogPrivacy
0x19e6c597c  __TEXT,__text  static os.OSLogPrivacy.mail(os.OSLogPrivacy._MailMask) -> os.OSLogPrivacy
0x19e6c5930  __TEXT,__text  os.OSLogPrivacy.mask.modify : os.OSLogPrivacy.Mask
0x19e6c5918  __TEXT,__text  os.OSLogPrivacy.mask.getter : os.OSLogPrivacy.Mask
0x19e6cf1c0  __TEXT,__const  property descriptor for os.OSLogPrivacy.mask : os.OSLogPrivacy.Mask
0x19e6c5924  __TEXT,__text  os.OSLogPrivacy.mask.setter : os.OSLogPrivacy.Mask
0x19e6ba76c  __TEXT,__text  static os.OSLogPrivacy.public.getter : os.OSLogPrivacy
0x19e6cf1b8  __TEXT,__const  property descriptor for static os.OSLogPrivacy.public : os.OSLogPrivacy
0x19e6c53a4  __TEXT,__text  os.OSLogPrivacy.hasMask.getter : Swift.Bool
0x19e6cf1b8  __TEXT,__const  property descriptor for os.OSLogPrivacy.hasMask : Swift.Bool
0x19e6c5950  __TEXT,__text  os.OSLogPrivacy.init(privacy: os.OSLogPrivacy.PrivacyOption, mask: os.OSLogPrivacy.Mask) -> os.OSLogPrivacy
0x19e6c58f8  __TEXT,__text  os.OSLogPrivacy.privacy.modify : os.OSLogPrivacy.PrivacyOption
0x19e6c58e0  __TEXT,__text  os.OSLogPrivacy.privacy.getter : os.OSLogPrivacy.PrivacyOption
0x19e6cf1bc  __TEXT,__const  property descriptor for os.OSLogPrivacy.privacy : os.OSLogPrivacy.PrivacyOption
0x19e6c58ec  __TEXT,__text  os.OSLogPrivacy.privacy.setter : os.OSLogPrivacy.PrivacyOption
0x19e6c596c  __TEXT,__text  static os.OSLogPrivacy.private(mask: os.OSLogPrivacy.Mask) -> os.OSLogPrivacy
0x19e6c5964  __TEXT,__text  static os.OSLogPrivacy.private.getter : os.OSLogPrivacy
0x19e6cf1b8  __TEXT,__const  property descriptor for static os.OSLogPrivacy.private : os.OSLogPrivacy
0x19e6cf264  __TEXT,__const  enum case for os.OSLogPrivacy._MailMask.mailboxPath(os.OSLogPrivacy._MailMask.Type) -> os.OSLogPrivacy._MailMask
0x19e6cf268  __TEXT,__const  enum case for os.OSLogPrivacy._MailMask.attachmentFileName(os.OSLogPrivacy._MailMask.Type) -> os.OSLogPrivacy._MailMask
0x19e6c61c8  __TEXT,__text  static os.OSLogPrivacy._MailMask.== infix(os.OSLogPrivacy._MailMask, os.OSLogPrivacy._MailMask) -> Swift.Bool
0x19e6c61b8  __TEXT,__text  os.OSLogPrivacy._MailMask.hash(into: inout Swift.Hasher) -> ()
0x19e6cf24c  __TEXT,__const  enum case for os.OSLogPrivacy._MailMask.name(os.OSLogPrivacy._MailMask.Type) -> os.OSLogPrivacy._MailMask
0x19e6cf25c  __TEXT,__const  enum case for os.OSLogPrivacy._MailMask.account(os.OSLogPrivacy._MailMask.Type) -> os.OSLogPrivacy._MailMask
0x19e6cf250  __TEXT,__const  enum case for os.OSLogPrivacy._MailMask.address(os.OSLogPrivacy._MailMask.Type) -> os.OSLogPrivacy._MailMask
0x19e6cf260  __TEXT,__const  enum case for os.OSLogPrivacy._MailMask.mailbox(os.OSLogPrivacy._MailMask.Type) -> os.OSLogPrivacy._MailMask
0x19e6cf254  __TEXT,__const  enum case for os.OSLogPrivacy._MailMask.subject(os.OSLogPrivacy._MailMask.Type) -> os.OSLogPrivacy._MailMask
0x19e6cf258  __TEXT,__const  enum case for os.OSLogPrivacy._MailMask.summary(os.OSLogPrivacy._MailMask.Type) -> os.OSLogPrivacy._MailMask
0x19e6c61c0  __TEXT,__text  os.OSLogPrivacy._MailMask.hashValue.getter : Swift.Int
0x19e6cf1b8  __TEXT,__const  property descriptor for os.OSLogPrivacy._MailMask.hashValue : Swift.Int
0x19e6c61a4  __TEXT,__text  type metadata accessor for os.OSLogPrivacy._MailMask
0x19e6d0a68  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogPrivacy._MailMask
0x1e42020e0  __AUTH_CONST,__const  type metadata for os.OSLogPrivacy._MailMask
0x19e6cf178  __TEXT,__const  protocol conformance descriptor for os.OSLogPrivacy._MailMask : Swift.Hashable in os
0x19e6cf150  __TEXT,__const  protocol conformance descriptor for os.OSLogPrivacy._MailMask : Swift.Equatable in os
0x19e6c53b4  __TEXT,__text  os.OSLogPrivacy.maskValue.getter : Swift.UInt64
0x19e6cf1b8  __TEXT,__const  property descriptor for os.OSLogPrivacy.maskValue : Swift.UInt64
0x19e6c5afc  __TEXT,__text  static os.OSLogPrivacy.sensitive(mask: os.OSLogPrivacy.Mask) -> os.OSLogPrivacy
0x19e6c5974  __TEXT,__text  static os.OSLogPrivacy.sensitive.getter : os.OSLogPrivacy
0x19e6cf1b8  __TEXT,__const  property descriptor for static os.OSLogPrivacy.sensitive : os.OSLogPrivacy
0x19e6c5ef4  __TEXT,__text  type metadata accessor for os.OSLogPrivacy
0x19e6d0a14  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogPrivacy
0x1e4202048  __AUTH_CONST,__const  type metadata for os.OSLogPrivacy
0x19e6bbc68  __TEXT,__text  static os.OSMetricType.== infix(os.OSMetricType, os.OSMetricType) -> Swift.Bool
0x19e6bbc7c  __TEXT,__text  os.OSMetricType.hash(into: inout Swift.Hasher) -> ()
0x19e6ce68c  __TEXT,__const  enum case for os.OSMetricType.gauge(os.OSMetricType.Type) -> os.OSMetricType
0x19e6ce688  __TEXT,__const  enum case for os.OSMetricType.counter(os.OSMetricType.Type) -> os.OSMetricType
0x19e6bbca8  __TEXT,__text  os.OSMetricType.hashValue.getter : Swift.Int
0x19e6ce5ec  __TEXT,__const  property descriptor for os.OSMetricType.hashValue : Swift.Int
0x19e6ce690  __TEXT,__const  enum case for os.OSMetricType.histogram(os.OSMetricType.Type) -> os.OSMetricType
0x19e6bd010  __TEXT,__text  type metadata accessor for os.OSMetricType
0x19e6d0718  __TEXT,__constg_swiftt  nominal type descriptor for os.OSMetricType
0x1e4201fd0  __AUTH_CONST,__const  type metadata for os.OSMetricType
0x19e6ce348  __TEXT,__const  protocol conformance descriptor for os.OSMetricType : Swift.Hashable in os
0x19e6ce320  __TEXT,__const  protocol conformance descriptor for os.OSMetricType : Swift.Equatable in os
0x19e6bd7bc  __TEXT,__text  static os.OSMetricUnit.== infix(os.OSMetricUnit, os.OSMetricUnit) -> Swift.Bool
0x19e6bd77c  __TEXT,__text  os.OSMetricUnit.hash(into: inout Swift.Hasher) -> ()
0x19e6ce6a4  __TEXT,__const  enum case for os.OSMetricUnit.none(os.OSMetricUnit.Type) -> os.OSMetricUnit
0x19e6ce6a8  __TEXT,__const  enum case for os.OSMetricUnit.bytes(os.OSMetricUnit.Type) -> os.OSMetricUnit
0x19e6ce6ac  __TEXT,__const  enum case for os.OSMetricUnit.seconds(os.OSMetricUnit.Type) -> os.OSMetricUnit
0x19e6bd7b0  __TEXT,__text  os.OSMetricUnit.hashValue.getter : Swift.Int
0x19e6ce5ec  __TEXT,__const  property descriptor for os.OSMetricUnit.hashValue : Swift.Int
0x19e6bd160  __TEXT,__text  type metadata accessor for os.OSMetricUnit
0x19e6d0734  __TEXT,__constg_swiftt  nominal type descriptor for os.OSMetricUnit
0x1e4201f40  __AUTH_CONST,__const  type metadata for os.OSMetricUnit
0x19e6ce3b0  __TEXT,__const  protocol conformance descriptor for os.OSMetricUnit : Swift.Hashable in os
0x19e6ce388  __TEXT,__const  protocol conformance descriptor for os.OSMetricUnit : Swift.Equatable in os
0x19e6be9f4  __TEXT,__text  static os.OSSignpostID.< infix(os.OSSignpostID, os.OSSignpostID) -> Swift.Bool
0x19e6bea08  __TEXT,__text  static os.OSSignpostID.== infix(os.OSSignpostID, os.OSSignpostID) -> Swift.Bool
0x19e6ba66c  __TEXT,__text  os.OSSignpostID.init(log: __C.OS_os_log, object: Swift.AnyObject) -> os.OSSignpostID
0x19e6ba8c8  __TEXT,__text  os.OSSignpostID.init(log: __C.OS_os_log) -> os.OSSignpostID
0x19e6be9d0  __TEXT,__text  static os.OSSignpostID.null.getter : os.OSSignpostID
0x19e6ceab4  __TEXT,__const  property descriptor for static os.OSSignpostID.null : os.OSSignpostID
0x19e6ba46c  __TEXT,__text  static os.OSSignpostID.invalid.getter : os.OSSignpostID
0x19e6ceab4  __TEXT,__const  property descriptor for static os.OSSignpostID.invalid : os.OSSignpostID
0x19e6ba8a4  __TEXT,__text  os.OSSignpostID.rawValue.getter : Swift.UInt64
0x19e6ceab8  __TEXT,__const  property descriptor for os.OSSignpostID.rawValue : Swift.UInt64
0x19e6ba104  __TEXT,__text  static os.OSSignpostID.exclusive.getter : os.OSSignpostID
0x19e6ceab4  __TEXT,__const  property descriptor for static os.OSSignpostID.exclusive : os.OSSignpostID
0x19e6b866c  __TEXT,__text  type metadata accessor for os.OSSignpostID
0x19e6d08f0  __TEXT,__constg_swiftt  nominal type descriptor for os.OSSignpostID
0x1e4201ea8  __AUTH_CONST,__const  type metadata for os.OSSignpostID
0x19e6cea40  __TEXT,__const  protocol conformance descriptor for os.OSSignpostID : Swift.Comparable in os
0x19e6cea88  __TEXT,__const  protocol conformance descriptor for os.OSSignpostID : Swift.Equatable in os
0x19e6b9b2c  __TEXT,__text  os.OSSignpostID.init(Swift.UInt64) -> os.OSSignpostID
0x19e6cb02c  __TEXT,__text  os.OSSignposter.endInterval(Swift.StaticString, os.OSSignpostIntervalState, os.OSLogMessage) -> ()
0x19e6cb4fc  __TEXT,__text  os.OSSignposter.endInterval(Swift.StaticString, os.OSSignpostIntervalState) -> ()
0x19e6ca598  __TEXT,__text  os.OSSignposter.beginInterval(_: Swift.StaticString, id: os.OSSignpostID) -> os.OSSignpostIntervalState
0x19e6ca078  __TEXT,__text  os.OSSignposter.beginInterval(_: Swift.StaticString, id: os.OSSignpostID, _: os.OSLogMessage) -> os.OSSignpostIntervalState
0x19e6cc5fc  __TEXT,__text  os.OSSignposter.makeSignpostID(from: Swift.AnyObject) -> os.OSSignpostID
0x19e6cc5d0  __TEXT,__text  os.OSSignposter.makeSignpostID() -> os.OSSignpostID
0x19e6cbf2c  __TEXT,__text  os.OSSignposter.withIntervalSignpost<A>(_: Swift.StaticString, id: os.OSSignpostID, around: () throws -> A) throws -> A
0x19e6cba98  __TEXT,__text  os.OSSignposter.withIntervalSignpost<A>(_: Swift.StaticString, id: os.OSSignpostID, _: os.OSLogMessage, around: () throws -> A) throws -> A
0x19e6ca5cc  __TEXT,__text  os.OSSignposter.beginAnimationInterval(_: Swift.StaticString, id: os.OSSignpostID) -> os.OSSignpostIntervalState
0x19e6caaf8  __TEXT,__text  os.OSSignposter.beginAnimationInterval(_: Swift.StaticString, id: os.OSSignpostID, _: os.OSLogMessage) -> os.OSSignpostIntervalState
0x19e6ba86c  __TEXT,__text  os.OSSignposter.init(logger: os.Logger) -> os.OSSignposter
0x19e6c963c  __TEXT,__text  static os.OSSignposter.disabled.getter : os.OSSignposter
0x19e6cf6ac  __TEXT,__const  property descriptor for static os.OSSignposter.disabled : os.OSSignposter
0x19e6c96dc  __TEXT,__text  os.OSSignposter.emitEvent(_: Swift.StaticString, id: os.OSSignpostID, _: os.OSLogMessage) -> ()
0x19e6c9b8c  __TEXT,__text  os.OSSignposter.emitEvent(_: Swift.StaticString, id: os.OSSignpostID) -> ()
0x19e6c9620  __TEXT,__text  os.OSSignposter.isEnabled.getter : Swift.Bool
0x19e6cf6ac  __TEXT,__const  property descriptor for os.OSSignposter.isEnabled : Swift.Bool
0x19e6ba850  __TEXT,__text  os.OSSignposter.init(logHandle: __C.OS_os_log) -> os.OSSignposter
0x19e6ba89c  __TEXT,__text  os.OSSignposter.logHandle.getter : __C.OS_os_log
0x19e6cf6a8  __TEXT,__const  property descriptor for os.OSSignposter.logHandle : __C.OS_os_log
0x19e6ba7d0  __TEXT,__text  os.OSSignposter.init(subsystem: Swift.String, category: Swift.String) -> os.OSSignposter
0x19e6c9660  __TEXT,__text  os.OSSignposter.init(subsystem: Swift.String, category: (extension in os):__C.OS_os_log.Category) -> os.OSSignposter
0x19e6ba5d4  __TEXT,__text  os.OSSignposter.init() -> os.OSSignposter
0x19e6ba6cc  __TEXT,__text  type metadata accessor for os.OSSignposter
0x19e6d0b2c  __TEXT,__constg_swiftt  nominal type descriptor for os.OSSignposter
0x1e4201e28  __AUTH_CONST,__const  type metadata for os.OSSignposter
0x19e6bbd74  __TEXT,__text  os.OSMetricFlags.init(rawValue: Swift.UInt8) -> os.OSMetricFlags
0x19e6bbd6c  __TEXT,__text  os.OSMetricFlags.rawValue.getter : Swift.UInt8
0x19e6ce5f0  __TEXT,__const  property descriptor for os.OSMetricFlags.rawValue : Swift.UInt8
0x19e6bd338  __TEXT,__text  type metadata accessor for os.OSMetricFlags
0x19e6d076c  __TEXT,__constg_swiftt  nominal type descriptor for os.OSMetricFlags
0x1e4201da8  __AUTH_CONST,__const  type metadata for os.OSMetricFlags
0x19e6ce528  __TEXT,__const  protocol conformance descriptor for os.OSMetricFlags : Swift.Equatable in os
0x19e6ce4f0  __TEXT,__const  protocol conformance descriptor for os.OSMetricFlags : Swift.RawRepresentable in os
0x19e6ce428  __TEXT,__const  protocol conformance descriptor for os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6ce550  __TEXT,__const  protocol conformance descriptor for os.OSMetricFlags : Swift.ExpressibleByArrayLiteral in os
0x19e6ce3f0  __TEXT,__const  protocol conformance descriptor for os.OSMetricFlags : Swift.OptionSet in os
0x19e6bc5b8  __TEXT,__text  os.OSMetricGauge.init<A where A == Swift.Double>(type: Swift.Double.Type, group: os.OSMetricGroup, label: Swift.String, extraDimensions: os.OSMetricDimensions, level: os.OSMetricStatisticalLevel, flags: os.OSMetricFlags) -> os.OSMetricGauge<Swift.Double>
0x19e6bc588  __TEXT,__text  os.OSMetricGauge.init<A where A == Swift.Int64>(type: Swift.Int64.Type, group: os.OSMetricGroup, label: Swift.String, extraDimensions: os.OSMetricDimensions, level: os.OSMetricStatisticalLevel, flags: os.OSMetricFlags) -> os.OSMetricGauge<Swift.Int64>
0x19e6bc5a0  __TEXT,__text  os.OSMetricGauge.init<A where A == Swift.UInt64>(type: Swift.UInt64.Type, group: os.OSMetricGroup, label: Swift.String, extraDimensions: os.OSMetricDimensions, level: os.OSMetricStatisticalLevel, flags: os.OSMetricFlags) -> os.OSMetricGauge<Swift.UInt64>
0x19e6bc568  __TEXT,__text  os.OSMetricGauge.bridge.modify : os.OSMetricBridge<A>
0x19e6bc52c  __TEXT,__text  os.OSMetricGauge.bridge.getter : os.OSMetricBridge<A>
0x19e6ce5f8  __TEXT,__const  property descriptor for os.OSMetricGauge.bridge : os.OSMetricBridge<A>
0x19e6bc538  __TEXT,__text  os.OSMetricGauge.bridge.setter : os.OSMetricBridge<A>
0x19e6bc720  __TEXT,__text  os.OSMetricGauge.setUnit(to: os.OSMetricUnit) -> ()
0x19e6bc71c  __TEXT,__text  os.OSMetricGauge.setScale(to: os.OSMetricScale) -> ()
0x19e6bd580  __TEXT,__text  type metadata accessor for os.OSMetricGauge
0x19e6d07f0  __TEXT,__constg_swiftt  nominal type descriptor for os.OSMetricGauge
0x19e6bc004  __TEXT,__text  static os.OSMetricGroup.default.getter : os.OSMetricGroup
0x19e6ce5ec  __TEXT,__const  property descriptor for static os.OSMetricGroup.default : os.OSMetricGroup
0x19e6bbf14  __TEXT,__text  os.OSMetricGroup.init(subsystem: Swift.String, category: Swift.String, dimensions: os.OSMetricDimensions) -> os.OSMetricGroup
0x19e6bbf94  __TEXT,__text  os.OSMetricGroup.init() -> os.OSMetricGroup
0x19e6bd558  __TEXT,__text  type metadata accessor for os.OSMetricGroup
0x19e6d07a4  __TEXT,__constg_swiftt  nominal type descriptor for os.OSMetricGroup
0x1e4201cc8  __AUTH_CONST,__const  type metadata for os.OSMetricGroup
0x19e6ce798  __TEXT,__const  enum case for os.OSMetricScale.giga(os.OSMetricScale.Type) -> os.OSMetricScale
0x19e6ce790  __TEXT,__const  enum case for os.OSMetricScale.kilo(os.OSMetricScale.Type) -> os.OSMetricScale
0x19e6ce794  __TEXT,__const  enum case for os.OSMetricScale.mega(os.OSMetricScale.Type) -> os.OSMetricScale
0x19e6ce784  __TEXT,__const  enum case for os.OSMetricScale.nano(os.OSMetricScale.Type) -> os.OSMetricScale
0x19e6ce7a0  __TEXT,__const  enum case for os.OSMetricScale.none(os.OSMetricScale.Type) -> os.OSMetricScale
0x19e6ce780  __TEXT,__const  enum case for os.OSMetricScale.pico(os.OSMetricScale.Type) -> os.OSMetricScale
0x19e6ce79c  __TEXT,__const  enum case for os.OSMetricScale.tera(os.OSMetricScale.Type) -> os.OSMetricScale
0x19e6ce788  __TEXT,__const  enum case for os.OSMetricScale.micro(os.OSMetricScale.Type) -> os.OSMetricScale
0x19e6ce78c  __TEXT,__const  enum case for os.OSMetricScale.milli(os.OSMetricScale.Type) -> os.OSMetricScale
0x19e6ce77c  __TEXT,__const  enum case for os.OSMetricScale.custom(os.OSMetricScale.Type) -> (Swift.Int8) -> os.OSMetricScale
0x19e6bd4a8  __TEXT,__text  type metadata accessor for os.OSMetricScale
0x19e6d0788  __TEXT,__constg_swiftt  nominal type descriptor for os.OSMetricScale
0x1e4201c50  __AUTH_CONST,__const  type metadata for os.OSMetricScale
0x19e6c3934  __TEXT,__text  os.OSLogArguments.argumentClosures.modify : [(inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> ()]
0x19e6c3904  __TEXT,__text  os.OSLogArguments.argumentClosures.getter : [(inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> ()]
0x19e6ceeec  __TEXT,__const  property descriptor for os.OSLogArguments.argumentClosures : [(inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> ()]
0x19e6c3908  __TEXT,__text  os.OSLogArguments.argumentClosures.setter : [(inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> ()]
0x19e6c87d8  __TEXT,__text  os.OSLogArguments.append(() -> Swift.String) -> ()
0x19e6c5134  __TEXT,__text  os.OSLogArguments.append(() -> Swift.UnsafeRawPointer) -> ()
0x19e6c03a4  __TEXT,__text  os.OSLogArguments.append(() -> Swift.Double) -> ()
0x19e6c44e4  __TEXT,__text  os.OSLogArguments.append(() -> __C.NSObject?) -> ()
0x19e6c3180  __TEXT,__text  os.OSLogArguments.append(Swift.UInt8) -> ()
0x19e6c24c8  __TEXT,__text  os.OSLogArguments.append<A where A: Swift.FixedWidthInteger>(() -> A) -> ()
0x19e6c3524  __TEXT,__text  os.OSLogArguments.init() -> os.OSLogArguments
0x19e6c3f60  __TEXT,__text  type metadata accessor for os.OSLogArguments
0x19e6d09dc  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogArguments
0x1e4201bb8  __AUTH_CONST,__const  type metadata for os.OSLogArguments
0x19e6bc508  __TEXT,__text  os.OSMetricBridge.emit<A where A == Swift.Double>(os.OSMetricOperation, Swift.Double, Swift.UnsafeRawPointer) -> ()
0x19e6bc4b8  __TEXT,__text  os.OSMetricBridge.emit<A where A == Swift.Int64>(os.OSMetricOperation, Swift.Int64, Swift.UnsafeRawPointer) -> ()
0x19e6bc4e0  __TEXT,__text  os.OSMetricBridge.emit<A where A == Swift.UInt64>(os.OSMetricOperation, Swift.UInt64, Swift.UnsafeRawPointer) -> ()
0x19e6bc2bc  __TEXT,__text  os.OSMetricBridge.init<A where A == Swift.Double>(group: os.OSMetricGroup, label: Swift.String, dimensions: os.OSMetricDimensions, type: os.OSMetricType, level: os.OSMetricStatisticalLevel, bins: Swift.UInt8, interval: Swift.UInt32, flags: Swift.UInt8) -> os.OSMetricBridge<Swift.Double>
0x19e6bc0c8  __TEXT,__text  os.OSMetricBridge.init<A where A == Swift.Int64>(group: os.OSMetricGroup, label: Swift.String, dimensions: os.OSMetricDimensions, type: os.OSMetricType, level: os.OSMetricStatisticalLevel, bins: Swift.UInt8, interval: Swift.UInt32, flags: Swift.UInt8) -> os.OSMetricBridge<Swift.Int64>
0x19e6bc11c  __TEXT,__text  os.OSMetricBridge.init<A where A == Swift.UInt64>(group: os.OSMetricGroup, label: Swift.String, dimensions: os.OSMetricDimensions, type: os.OSMetricType, level: os.OSMetricStatisticalLevel, bins: Swift.UInt8, interval: Swift.UInt32, flags: Swift.UInt8) -> os.OSMetricBridge<Swift.UInt64>
0x19e6bcac0  __TEXT,__text  os.OSMetricBridge.init<A where A == Swift.Double>(group: os.OSMetricGroup, label: Swift.String, dimensions: os.OSMetricDimensions, type: os.OSMetricType, level: os.OSMetricStatisticalLevel, bins: Swift.UInt8, intervals: [Swift.UInt64], flags: Swift.UInt8) -> os.OSMetricBridge<Swift.Double>
0x19e6bc778  __TEXT,__text  os.OSMetricBridge.init<A where A == Swift.Int64>(group: os.OSMetricGroup, label: Swift.String, dimensions: os.OSMetricDimensions, type: os.OSMetricType, level: os.OSMetricStatisticalLevel, bins: Swift.UInt8, intervals: [Swift.UInt64], flags: Swift.UInt8) -> os.OSMetricBridge<Swift.Int64>
0x19e6bc7e0  __TEXT,__text  os.OSMetricBridge.init<A where A == Swift.UInt64>(group: os.OSMetricGroup, label: Swift.String, dimensions: os.OSMetricDimensions, type: os.OSMetricType, level: os.OSMetricStatisticalLevel, bins: Swift.UInt8, intervals: [Swift.UInt64], flags: Swift.UInt8) -> os.OSMetricBridge<Swift.UInt64>
0x19e6bc498  __TEXT,__text  os.OSMetricBridge.setUnit(to: os.OSMetricUnit) -> ()
0x19e6bc458  __TEXT,__text  os.OSMetricBridge.setScale(to: os.OSMetricScale) -> ()
0x19e6bc480  __TEXT,__text  type metadata accessor for os.OSMetricBridge
0x19e6d086c  __TEXT,__constg_swiftt  nominal type descriptor for os.OSMetricBridge
0x19e6c61cc  __TEXT,__text  static os.OSLogBoolFormat.== infix(os.OSLogBoolFormat, os.OSLogBoolFormat) -> Swift.Bool
0x19e6c61e0  __TEXT,__text  os.OSLogBoolFormat.hash(into: inout Swift.Hasher) -> ()
0x19e6cf400  __TEXT,__const  enum case for os.OSLogBoolFormat.truth(os.OSLogBoolFormat.Type) -> os.OSLogBoolFormat
0x19e6cf404  __TEXT,__const  enum case for os.OSLogBoolFormat.answer(os.OSLogBoolFormat.Type) -> os.OSLogBoolFormat
0x19e6c620c  __TEXT,__text  os.OSLogBoolFormat.hashValue.getter : Swift.Int
0x19e6cf3e8  __TEXT,__const  property descriptor for os.OSLogBoolFormat.hashValue : Swift.Int
0x19e6c6c4c  __TEXT,__text  type metadata accessor for os.OSLogBoolFormat
0x19e6d0a84  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogBoolFormat
0x1e4201b40  __AUTH_CONST,__const  type metadata for os.OSLogBoolFormat
0x19e6cf2d8  __TEXT,__const  protocol conformance descriptor for os.OSLogBoolFormat : Swift.Hashable in os
0x19e6cf2b0  __TEXT,__const  protocol conformance descriptor for os.OSLogBoolFormat : Swift.Equatable in os
0x19e6ce73c  __TEXT,__const  enum case for os.OSMetricBinType.logarithmic(os.OSMetricBinType.Type) -> (Swift.UInt8) -> os.OSMetricBinType
0x19e6ce740  __TEXT,__const  enum case for os.OSMetricBinType.custom(os.OSMetricBinType.Type) -> ([Swift.UInt64]) -> os.OSMetricBinType
0x19e6ce738  __TEXT,__const  enum case for os.OSMetricBinType.interval(os.OSMetricBinType.Type) -> (Swift.UInt8, Swift.UInt32) -> os.OSMetricBinType
0x19e6bd224  __TEXT,__text  type metadata accessor for os.OSMetricBinType
0x19e6d0750  __TEXT,__constg_swiftt  nominal type descriptor for os.OSMetricBinType
0x1e4201ab0  __AUTH_CONST,__const  type metadata for os.OSMetricBinType
0x19e6bc158  __TEXT,__text  os.OSMetricCounter.init<A where A == Swift.Double>(type: Swift.Double.Type, group: os.OSMetricGroup, label: Swift.String, extraDimensions: os.OSMetricDimensions, flags: os.OSMetricFlags) -> os.OSMetricCounter<Swift.Double>
0x19e6bc0b0  __TEXT,__text  os.OSMetricCounter.init<A where A == Swift.Int64>(type: Swift.Int64.Type, group: os.OSMetricGroup, label: Swift.String, extraDimensions: os.OSMetricDimensions, flags: os.OSMetricFlags) -> os.OSMetricCounter<Swift.Int64>
0x19e6bc104  __TEXT,__text  os.OSMetricCounter.init<A where A == Swift.UInt64>(type: Swift.UInt64.Type, group: os.OSMetricGroup, label: Swift.String, extraDimensions: os.OSMetricDimensions, flags: os.OSMetricFlags) -> os.OSMetricCounter<Swift.UInt64>
0x19e6bc08c  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A>
0x19e6bd784  __TEXT,__text  os.OSMetricCounter.bridge.getter : os.OSMetricBridge<A>
0x19e6ce5f4  __TEXT,__const  property descriptor for os.OSMetricCounter.bridge : os.OSMetricBridge<A>
0x19e6bd790  __TEXT,__text  os.OSMetricCounter.bridge.setter : os.OSMetricBridge<A>
0x19e6bd750  __TEXT,__text  os.OSMetricCounter.setUnit(to: os.OSMetricUnit) -> ()
0x19e6bd79c  __TEXT,__text  os.OSMetricCounter.setScale(to: os.OSMetricScale) -> ()
0x19e6bd568  __TEXT,__text  type metadata accessor for os.OSMetricCounter
0x19e6d07c0  __TEXT,__constg_swiftt  nominal type descriptor for os.OSMetricCounter
0x19e6cf6ac  __TEXT,__const  property descriptor for static os.OSSignpostError.doubleEndErrorString : Swift.String
0x19e6cc62c  __TEXT,__text  static os.OSSignpostError.== infix(os.OSSignpostError, os.OSSignpostError) -> Swift.Bool
0x19e6cc640  __TEXT,__text  os.OSSignpostError.hash(into: inout Swift.Hasher) -> ()
0x19e6cf6fc  __TEXT,__const  enum case for os.OSSignpostError.none(os.OSSignpostError.Type) -> os.OSSignpostError
0x19e6cf6f8  __TEXT,__const  enum case for os.OSSignpostError.doubleEnd(os.OSSignpostError.Type) -> os.OSSignpostError
0x19e6cc66c  __TEXT,__text  os.OSSignpostError.hashValue.getter : Swift.Int
0x19e6cf6ac  __TEXT,__const  property descriptor for os.OSSignpostError.hashValue : Swift.Int
0x19e6ba6bc  __TEXT,__text  type metadata accessor for os.OSSignpostError
0x19e6d0b48  __TEXT,__constg_swiftt  nominal type descriptor for os.OSSignpostError
0x1e42019c8  __AUTH_CONST,__const  type metadata for os.OSSignpostError
0x19e6cf618  __TEXT,__const  protocol conformance descriptor for os.OSSignpostError : Swift.Hashable in os
0x19e6cf5f0  __TEXT,__const  protocol conformance descriptor for os.OSSignpostError : Swift.Equatable in os
0x19e6bb898  __TEXT,__text  os.OS_LOG_TYPE_INFO.getter : __C.os_log_type_t
0x19e6bc81c  __TEXT,__text  os.OSMetricHistogram.init<A where A == Swift.Double>(type: Swift.Double.Type, group: os.OSMetricGroup, label: Swift.String, extraDimensions: os.OSMetricDimensions, level: os.OSMetricStatisticalLevel, bins: os.OSMetricBinType, flags: os.OSMetricFlags) -> os.OSMetricHistogram<Swift.Double>
0x19e6bc760  __TEXT,__text  os.OSMetricHistogram.init<A where A == Swift.Int64>(type: Swift.Int64.Type, group: os.OSMetricGroup, label: Swift.String, extraDimensions: os.OSMetricDimensions, level: os.OSMetricStatisticalLevel, bins: os.OSMetricBinType, flags: os.OSMetricFlags) -> os.OSMetricHistogram<Swift.Int64>
0x19e6bc7c8  __TEXT,__text  os.OSMetricHistogram.init<A where A == Swift.UInt64>(type: Swift.UInt64.Type, group: os.OSMetricGroup, label: Swift.String, extraDimensions: os.OSMetricDimensions, level: os.OSMetricStatisticalLevel, bins: os.OSMetricBinType, flags: os.OSMetricFlags) -> os.OSMetricHistogram<Swift.UInt64>
0x19e6bc740  __TEXT,__text  os.OSMetricHistogram.bridge.modify : os.OSMetricBridge<A>
0x19e6bd788  __TEXT,__text  os.OSMetricHistogram.bridge.getter : os.OSMetricBridge<A>
0x19e6ce5fc  __TEXT,__const  property descriptor for os.OSMetricHistogram.bridge : os.OSMetricBridge<A>
0x19e6bd794  __TEXT,__text  os.OSMetricHistogram.bridge.setter : os.OSMetricBridge<A>
0x19e6bd754  __TEXT,__text  os.OSMetricHistogram.setUnit(to: os.OSMetricUnit) -> ()
0x19e6bd7a0  __TEXT,__text  os.OSMetricHistogram.setScale(to: os.OSMetricScale) -> ()
0x19e6bd598  __TEXT,__text  type metadata accessor for os.OSMetricHistogram
0x19e6d0820  __TEXT,__constg_swiftt  nominal type descriptor for os.OSMetricHistogram
0x19e6bd7c0  __TEXT,__text  static os.OSMetricOperation.== infix(os.OSMetricOperation, os.OSMetricOperation) -> Swift.Bool
0x19e6ce8b4  __TEXT,__const  enum case for os.OSMetricOperation.add(os.OSMetricOperation.Type) -> os.OSMetricOperation
0x19e6ce8bc  __TEXT,__const  enum case for os.OSMetricOperation.set(os.OSMetricOperation.Type) -> os.OSMetricOperation
0x19e6bd780  __TEXT,__text  os.OSMetricOperation.hash(into: inout Swift.Hasher) -> ()
0x19e6ce8c0  __TEXT,__const  enum case for os.OSMetricOperation.reset(os.OSMetricOperation.Type) -> os.OSMetricOperation
0x19e6ce8b8  __TEXT,__const  enum case for os.OSMetricOperation.subtract(os.OSMetricOperation.Type) -> os.OSMetricOperation
0x19e6bd7b4  __TEXT,__text  os.OSMetricOperation.hashValue.getter : Swift.Int
0x19e6ce5ec  __TEXT,__const  property descriptor for os.OSMetricOperation.hashValue : Swift.Int
0x19e6bd6f0  __TEXT,__text  type metadata accessor for os.OSMetricOperation
0x19e6d0850  __TEXT,__constg_swiftt  nominal type descriptor for os.OSMetricOperation
0x1e42018e0  __AUTH_CONST,__const  type metadata for os.OSMetricOperation
0x19e6ce5a8  __TEXT,__const  protocol conformance descriptor for os.OSMetricOperation : Swift.Hashable in os
0x19e6ce580  __TEXT,__const  protocol conformance descriptor for os.OSMetricOperation : Swift.Equatable in os
0x19e6bb8e4  __TEXT,__text  os.OS_LOG_TYPE_DEBUG.getter : __C.os_log_type_t
0x19e6bb930  __TEXT,__text  os.OS_LOG_TYPE_ERROR.getter : __C.os_log_type_t
0x19e6bb97c  __TEXT,__text  os.OS_LOG_TYPE_FAULT.getter : __C.os_log_type_t
0x19e6c81ec  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.String, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c9384  __TEXT,__text  os.OSLogInterpolation.appendInterpolation<A where A: Swift.CustomStringConvertible>(_: @autoclosure () -> A, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c9538  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Any.Type, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c4a14  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.UnsafeRawPointer, bytes: @autoclosure () -> Swift.Int, format: os.OSLogPointerFormat, privacy: os.OSLogPrivacy) -> ()
0x19e6bffd8  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Double, format: os.OSLogFloatFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6bfee4  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Float, format: os.OSLogFloatFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c1b48  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Int, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c1fb4  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.UInt, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c1e04  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Int8, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c1e64  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Int16, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c1ec4  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Int32, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c1f54  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Int64, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c2014  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.UInt8, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c2074  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.UInt16, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c20d4  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.UInt32, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c2134  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.UInt64, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c46bc  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.UnsafeRawBufferPointer, format: os.OSLogPointerFormat, privacy: os.OSLogPrivacy) -> ()
0x19e6c68dc  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Bool, format: os.OSLogBoolFormat, privacy: os.OSLogPrivacy) -> ()
0x19e6c6210  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Int32, format: os.OSLogInt32ExtendedFormat, privacy: os.OSLogPrivacy) -> ()
0x19e6c4158  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> __C.NSObject, privacy: os.OSLogPrivacy) -> ()
0x19e6c339c  __TEXT,__text  static os.OSLogInterpolation.ArgumentType.== infix(os.OSLogInterpolation.ArgumentType, os.OSLogInterpolation.ArgumentType) -> Swift.Bool
0x19e6c33b0  __TEXT,__text  os.OSLogInterpolation.ArgumentType.hash(into: inout Swift.Hasher) -> ()
0x19e6cef54  __TEXT,__const  enum case for os.OSLogInterpolation.ArgumentType.mask(os.OSLogInterpolation.ArgumentType.Type) -> os.OSLogInterpolation.ArgumentType
0x19e6cef44  __TEXT,__const  enum case for os.OSLogInterpolation.ArgumentType.count(os.OSLogInterpolation.ArgumentType.Type) -> os.OSLogInterpolation.ArgumentType
0x19e6cef50  __TEXT,__const  enum case for os.OSLogInterpolation.ArgumentType.object(os.OSLogInterpolation.ArgumentType.Type) -> os.OSLogInterpolation.ArgumentType
0x19e6cef40  __TEXT,__const  enum case for os.OSLogInterpolation.ArgumentType.scalar(os.OSLogInterpolation.ArgumentType.Type) -> os.OSLogInterpolation.ArgumentType
0x19e6cef48  __TEXT,__const  enum case for os.OSLogInterpolation.ArgumentType.string(os.OSLogInterpolation.ArgumentType.Type) -> os.OSLogInterpolation.ArgumentType
0x19e6cef4c  __TEXT,__const  enum case for os.OSLogInterpolation.ArgumentType.pointer(os.OSLogInterpolation.ArgumentType.Type) -> os.OSLogInterpolation.ArgumentType
0x19e6c3380  __TEXT,__text  os.OSLogInterpolation.ArgumentType.rawValue.getter : Swift.UInt8
0x19e6ceed0  __TEXT,__const  property descriptor for os.OSLogInterpolation.ArgumentType.rawValue : Swift.UInt8
0x19e6c33dc  __TEXT,__text  os.OSLogInterpolation.ArgumentType.hashValue.getter : Swift.Int
0x19e6ceed0  __TEXT,__const  property descriptor for os.OSLogInterpolation.ArgumentType.hashValue : Swift.Int
0x19e6c3eb0  __TEXT,__text  type metadata accessor for os.OSLogInterpolation.ArgumentType
0x19e6d09a4  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogInterpolation.ArgumentType
0x1e4201850  __AUTH_CONST,__const  type metadata for os.OSLogInterpolation.ArgumentType
0x19e6ced50  __TEXT,__const  protocol conformance descriptor for os.OSLogInterpolation.ArgumentType : Swift.Hashable in os
0x19e6ced28  __TEXT,__const  protocol conformance descriptor for os.OSLogInterpolation.ArgumentType : Swift.Equatable in os
0x19e6c330c  __TEXT,__text  os.OSLogInterpolation.formatString.modify : Swift.String
0x19e6c32a4  __TEXT,__text  os.OSLogInterpolation.formatString.getter : Swift.String
0x19e6ceec8  __TEXT,__const  property descriptor for os.OSLogInterpolation.formatString : Swift.String
0x19e6c32d4  __TEXT,__text  os.OSLogInterpolation.formatString.setter : Swift.String
0x19e6c22cc  __TEXT,__text  os.OSLogInterpolation.addIntHeaders(os.OSLogPrivacy, Swift.Int) -> ()
0x19e6ccf64  __TEXT,__text  os.OSLogInterpolation.appendInteger<A where A: Swift.FixedWidthInteger>(_: () -> A, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c3568  __TEXT,__text  os.OSLogInterpolation.appendLiteral(Swift.String) -> ()
0x19e6c3474  __TEXT,__text  os.OSLogInterpolation.argumentCount.modify : Swift.UInt8
0x19e6c3464  __TEXT,__text  os.OSLogInterpolation.argumentCount.getter : Swift.UInt8
0x19e6ceed8  __TEXT,__const  property descriptor for os.OSLogInterpolation.argumentCount : Swift.UInt8
0x19e6c346c  __TEXT,__text  os.OSLogInterpolation.argumentCount.setter : Swift.UInt8
0x19e6c3454  __TEXT,__text  os.OSLogInterpolation.privateBitMask.getter : Swift.UInt8
0x19e6ceed0  __TEXT,__const  property descriptor for os.OSLogInterpolation.privateBitMask : Swift.UInt8
0x19e6c2ea0  __TEXT,__text  os.OSLogInterpolation.init(literalCapacity: Swift.Int, interpolationCount: Swift.Int) -> os.OSLogInterpolation
0x19e6c0274  __TEXT,__text  os.OSLogInterpolation.addDoubleHeaders(os.OSLogPrivacy) -> ()
0x19e6c86a4  __TEXT,__text  os.OSLogInterpolation.addStringHeaders(os.OSLogPrivacy) -> ()
0x19e6c345c  __TEXT,__text  os.OSLogInterpolation.nonScalarBitMask.getter : Swift.UInt8
0x19e6ceed0  __TEXT,__const  property descriptor for os.OSLogInterpolation.nonScalarBitMask : Swift.UInt8
0x19e6c5000  __TEXT,__text  os.OSLogInterpolation.addPointerHeaders(os.OSLogPrivacy) -> ()
0x19e6c3140  __TEXT,__text  os.OSLogInterpolation.getArgumentHeader(privacy: os.OSLogPrivacy, type: os.OSLogInterpolation.ArgumentType) -> Swift.UInt8
0x19e6c43b0  __TEXT,__text  os.OSLogInterpolation.addNSObjectHeaders(os.OSLogPrivacy) -> ()
0x19e6c1688  __TEXT,__text  os.OSLogInterpolation.appendMaskArgument(os.OSLogPrivacy) -> ()
0x19e6c69cc  __TEXT,__text  os.OSLogInterpolation.getInt32BoolFormat(os.OSLogBoolFormat) -> os.OSLogInt32ExtendedFormat
0x19e6c31f8  __TEXT,__text  os.OSLogInterpolation.getUpdatedPreamble(privacy: os.OSLogPrivacy, isScalar: Swift.Bool) -> Swift.UInt8
0x19e6c3504  __TEXT,__text  os.OSLogInterpolation.objectArgumentCount.modify : Swift.Int
0x19e6c34f4  __TEXT,__text  os.OSLogInterpolation.objectArgumentCount.getter : Swift.Int
0x19e6ceee4  __TEXT,__const  property descriptor for os.OSLogInterpolation.objectArgumentCount : Swift.Int
0x19e6c34fc  __TEXT,__text  os.OSLogInterpolation.objectArgumentCount.setter : Swift.Int
0x19e6c34d4  __TEXT,__text  os.OSLogInterpolation.stringArgumentCount.modify : Swift.Int
0x19e6c34c4  __TEXT,__text  os.OSLogInterpolation.stringArgumentCount.getter : Swift.Int
0x19e6ceee0  __TEXT,__const  property descriptor for os.OSLogInterpolation.stringArgumentCount : Swift.Int
0x19e6c34cc  __TEXT,__text  os.OSLogInterpolation.stringArgumentCount.setter : Swift.Int
0x19e6c1664  __TEXT,__text  os.OSLogInterpolation.appendAlignmentArgument(() -> Swift.Int) -> ()
0x19e6c18ac  __TEXT,__text  os.OSLogInterpolation.appendPrecisionArgument(() -> Swift.Int) -> ()
0x19e6cd00c  __TEXT,__text  os.OSLogInterpolation.getStringFormatSpecifier(os.OSLogStringAlignment, os.OSLogPrivacy) -> Swift.String
0x19e6c256c  __TEXT,__text  os.OSLogInterpolation.appendPrecisionAlignCount(() -> Swift.Int, Swift.UInt8) -> ()
0x19e6ccff4  __TEXT,__text  os.OSLogInterpolation.getPointerFormatSpecifier(os.OSLogPointerFormat, os.OSLogPrivacy) -> Swift.String
0x19e6cd054  __TEXT,__text  os.OSLogInterpolation.getExtendedFormatSpecifier(os.OSLogInt32ExtendedFormat, os.OSLogPrivacy) -> Swift.String
0x19e6ccfc0  __TEXT,__text  os.OSLogInterpolation.getNSObjectFormatSpecifier(os.OSLogPrivacy) -> Swift.String
0x19e6c34a4  __TEXT,__text  os.OSLogInterpolation.totalBytesForSerializingArguments.modify : Swift.Int
0x19e6c3494  __TEXT,__text  os.OSLogInterpolation.totalBytesForSerializingArguments.getter : Swift.Int
0x19e6ceedc  __TEXT,__const  property descriptor for os.OSLogInterpolation.totalBytesForSerializingArguments : Swift.Int
0x19e6c349c  __TEXT,__text  os.OSLogInterpolation.totalBytesForSerializingArguments.setter : Swift.Int
0x19e6c3434  __TEXT,__text  os.OSLogInterpolation.preamble.modify : Swift.UInt8
0x19e6c3424  __TEXT,__text  os.OSLogInterpolation.preamble.getter : Swift.UInt8
0x19e6ceed4  __TEXT,__const  property descriptor for os.OSLogInterpolation.preamble : Swift.UInt8
0x19e6c342c  __TEXT,__text  os.OSLogInterpolation.preamble.setter : Swift.UInt8
0x19e6c3360  __TEXT,__text  os.OSLogInterpolation.arguments.modify : os.OSLogArguments
0x19e6c332c  __TEXT,__text  os.OSLogInterpolation.arguments.getter : os.OSLogArguments
0x19e6ceecc  __TEXT,__const  property descriptor for os.OSLogInterpolation.arguments : os.OSLogArguments
0x19e6c3334  __TEXT,__text  os.OSLogInterpolation.arguments.setter : os.OSLogArguments
0x19e6c3d60  __TEXT,__text  type metadata accessor for os.OSLogInterpolation
0x19e6d0988  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogInterpolation
0x1e42017a0  __AUTH_CONST,__const  type metadata for os.OSLogInterpolation
0x19e6ced90  __TEXT,__const  protocol conformance descriptor for os.OSLogInterpolation : Swift.StringInterpolationProtocol in os
0x19e6cf054  __TEXT,__const  enum case for os.OSLogPointerFormat.ipv6Address(os.OSLogPointerFormat.Type) -> os.OSLogPointerFormat
0x19e6c4634  __TEXT,__text  static os.OSLogPointerFormat.== infix(os.OSLogPointerFormat, os.OSLogPointerFormat) -> Swift.Bool
0x19e6c4648  __TEXT,__text  os.OSLogPointerFormat.hash(into: inout Swift.Hasher) -> ()
0x19e6cf068  __TEXT,__const  enum case for os.OSLogPointerFormat.none(os.OSLogPointerFormat.Type) -> os.OSLogPointerFormat
0x19e6cf060  __TEXT,__const  enum case for os.OSLogPointerFormat.uuid(os.OSLogPointerFormat.Type) -> os.OSLogPointerFormat
0x19e6cf058  __TEXT,__const  enum case for os.OSLogPointerFormat.timeval(os.OSLogPointerFormat.Type) -> os.OSLogPointerFormat
0x19e6cf064  __TEXT,__const  enum case for os.OSLogPointerFormat.sockaddr(os.OSLogPointerFormat.Type) -> os.OSLogPointerFormat
0x19e6cf05c  __TEXT,__const  enum case for os.OSLogPointerFormat.timespec(os.OSLogPointerFormat.Type) -> os.OSLogPointerFormat
0x19e6c4674  __TEXT,__text  os.OSLogPointerFormat.hashValue.getter : Swift.Int
0x19e6cf030  __TEXT,__const  property descriptor for os.OSLogPointerFormat.hashValue : Swift.Int
0x19e6c5270  __TEXT,__text  type metadata accessor for os.OSLogPointerFormat
0x19e6d09f8  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogPointerFormat
0x1e4201728  __AUTH_CONST,__const  type metadata for os.OSLogPointerFormat
0x19e6ceff0  __TEXT,__const  protocol conformance descriptor for os.OSLogPointerFormat : Swift.Hashable in os
0x19e6cefc8  __TEXT,__const  protocol conformance descriptor for os.OSLogPointerFormat : Swift.Equatable in os
0x19e6bbaf4  __TEXT,__text  os.OSMetricDimensions.init(dictionaryLiteral: (Swift.String, Swift.String)...) -> os.OSMetricDimensions
0x19e6bbafc  __TEXT,__text  static os.OSMetricDimensions.empty.getter : os.OSMetricDimensions
0x19e6ce5ec  __TEXT,__const  property descriptor for static os.OSMetricDimensions.empty : os.OSMetricDimensions
0x19e6bd75c  __TEXT,__text  os.OSMetricDimensions.init(values: [(Swift.String, Swift.String)]) -> os.OSMetricDimensions
0x19e6bbad8  __TEXT,__text  os.OSMetricDimensions.values.getter : [(Swift.String, Swift.String)]
0x19e6ce5e8  __TEXT,__const  property descriptor for os.OSMetricDimensions.values : [(Swift.String, Swift.String)]
0x19e6bcff0  __TEXT,__text  type metadata accessor for os.OSMetricDimensions
0x19e6d06e0  __TEXT,__constg_swiftt  nominal type descriptor for os.OSMetricDimensions
0x1e4201690  __AUTH_CONST,__const  type metadata for os.OSMetricDimensions
0x19e6ce280  __TEXT,__const  protocol conformance descriptor for os.OSMetricDimensions : Swift.ExpressibleByDictionaryLiteral in os
0x19e6bb84c  __TEXT,__text  os.OS_LOG_TYPE_DEFAULT.getter : __C.os_log_type_t
0x19e6c704c  __TEXT,__text  static os.OSLogCollectionBound.== infix(os.OSLogCollectionBound, os.OSLogCollectionBound) -> Swift.Bool
0x19e6cf52c  __TEXT,__const  enum case for os.OSLogCollectionBound.end(os.OSLogCollectionBound.Type) -> os.OSLogCollectionBound
0x19e6c7060  __TEXT,__text  os.OSLogCollectionBound.hash(into: inout Swift.Hasher) -> ()
0x19e6cf528  __TEXT,__const  enum case for os.OSLogCollectionBound.start(os.OSLogCollectionBound.Type) -> os.OSLogCollectionBound
0x19e6c708c  __TEXT,__text  os.OSLogCollectionBound.hashValue.getter : Swift.Int
0x19e6cf4f8  __TEXT,__const  property descriptor for os.OSLogCollectionBound.hashValue : Swift.Int
0x19e6c73bc  __TEXT,__text  type metadata accessor for os.OSLogCollectionBound
0x19e6d0ad8  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogCollectionBound
0x1e4201618  __AUTH_CONST,__const  type metadata for os.OSLogCollectionBound
0x19e6cf4b8  __TEXT,__const  protocol conformance descriptor for os.OSLogCollectionBound : Swift.Hashable in os
0x19e6cf490  __TEXT,__const  protocol conformance descriptor for os.OSLogCollectionBound : Swift.Equatable in os
0x19e6bf578  __TEXT,__text  static os.OSLogFloatFormatting.exponential(explicitPositiveSign: Swift.Bool, uppercase: Swift.Bool) -> os.OSLogFloatFormatting
0x19e6bf588  __TEXT,__text  static os.OSLogFloatFormatting.exponential(precision: @autoclosure () -> Swift.Int, explicitPositiveSign: Swift.Bool, uppercase: Swift.Bool) -> os.OSLogFloatFormatting
0x19e6bf538  __TEXT,__text  static os.OSLogFloatFormatting.exponential.getter : os.OSLogFloatFormatting
0x19e6cec00  __TEXT,__const  property descriptor for static os.OSLogFloatFormatting.exponential : os.OSLogFloatFormatting
0x19e6cd124  __TEXT,__text  os.OSLogFloatFormatting.formatSpecifier<A where A: Swift.FloatingPoint>(for: A.Type, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> Swift.String
0x19e6bf3ac  __TEXT,__text  os.OSLogFloatFormatting.init(explicitPositiveSign: Swift.Bool, uppercase: Swift.Bool, precision: (() -> Swift.Int)?, notation: os.OSLogFloatFormatting.Notation) -> os.OSLogFloatFormatting
0x19e6bf100  __TEXT,__text  os.OSLogFloatFormatting.explicitPositiveSign.modify : Swift.Bool
0x19e6bf0f0  __TEXT,__text  os.OSLogFloatFormatting.explicitPositiveSign.getter : Swift.Bool
0x19e6cebf8  __TEXT,__const  property descriptor for os.OSLogFloatFormatting.explicitPositiveSign : Swift.Bool
0x19e6bf0f8  __TEXT,__text  os.OSLogFloatFormatting.explicitPositiveSign.setter : Swift.Bool
0x19e6bf748  __TEXT,__text  static os.OSLogFloatFormatting._formatStringLengthModifier<A where A: Swift.FloatingPoint>(A.Type) -> Swift.String?
0x19e6bf528  __TEXT,__text  static os.OSLogFloatFormatting.hex(explicitPositiveSign: Swift.Bool, uppercase: Swift.Bool) -> os.OSLogFloatFormatting
0x19e6bf48c  __TEXT,__text  static os.OSLogFloatFormatting.hex.getter : os.OSLogFloatFormatting
0x19e6cec00  __TEXT,__const  property descriptor for static os.OSLogFloatFormatting.hex : os.OSLogFloatFormatting
0x19e6bf404  __TEXT,__text  static os.OSLogFloatFormatting.fixed(explicitPositiveSign: Swift.Bool, uppercase: Swift.Bool) -> os.OSLogFloatFormatting
0x19e6bf47c  __TEXT,__text  static os.OSLogFloatFormatting.fixed(precision: @autoclosure () -> Swift.Int, explicitPositiveSign: Swift.Bool, uppercase: Swift.Bool) -> os.OSLogFloatFormatting
0x19e6bf3c4  __TEXT,__text  static os.OSLogFloatFormatting.fixed.getter : os.OSLogFloatFormatting
0x19e6cec00  __TEXT,__const  property descriptor for static os.OSLogFloatFormatting.fixed : os.OSLogFloatFormatting
0x19e6bf5d8  __TEXT,__text  static os.OSLogFloatFormatting.hybrid(explicitPositiveSign: Swift.Bool, uppercase: Swift.Bool) -> os.OSLogFloatFormatting
0x19e6bf67c  __TEXT,__text  static os.OSLogFloatFormatting.hybrid(precision: @autoclosure () -> Swift.Int, explicitPositiveSign: Swift.Bool, uppercase: Swift.Bool) -> os.OSLogFloatFormatting
0x19e6bf598  __TEXT,__text  static os.OSLogFloatFormatting.hybrid.getter : os.OSLogFloatFormatting
0x19e6cec00  __TEXT,__const  property descriptor for static os.OSLogFloatFormatting.hybrid : os.OSLogFloatFormatting
0x19e6cec78  __TEXT,__const  enum case for os.OSLogFloatFormatting.Notation.exponential(os.OSLogFloatFormatting.Notation.Type) -> os.OSLogFloatFormatting.Notation
0x19e6bf2ec  __TEXT,__text  static os.OSLogFloatFormatting.Notation.== infix(os.OSLogFloatFormatting.Notation, os.OSLogFloatFormatting.Notation) -> Swift.Bool
0x19e6cec70  __TEXT,__const  enum case for os.OSLogFloatFormatting.Notation.hex(os.OSLogFloatFormatting.Notation.Type) -> os.OSLogFloatFormatting.Notation
0x19e6bf300  __TEXT,__text  os.OSLogFloatFormatting.Notation.hash(into: inout Swift.Hasher) -> ()
0x19e6cec74  __TEXT,__const  enum case for os.OSLogFloatFormatting.Notation.fixed(os.OSLogFloatFormatting.Notation.Type) -> os.OSLogFloatFormatting.Notation
0x19e6cec7c  __TEXT,__const  enum case for os.OSLogFloatFormatting.Notation.hybrid(os.OSLogFloatFormatting.Notation.Type) -> os.OSLogFloatFormatting.Notation
0x19e6bf32c  __TEXT,__text  os.OSLogFloatFormatting.Notation.hashValue.getter : Swift.Int
0x19e6cec00  __TEXT,__const  property descriptor for os.OSLogFloatFormatting.Notation.hashValue : Swift.Int
0x19e6bf900  __TEXT,__text  type metadata accessor for os.OSLogFloatFormatting.Notation
0x19e6d0950  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogFloatFormatting.Notation
0x1e4201588  __AUTH_CONST,__const  type metadata for os.OSLogFloatFormatting.Notation
0x19e6cebb8  __TEXT,__const  protocol conformance descriptor for os.OSLogFloatFormatting.Notation : Swift.Hashable in os
0x19e6ceb90  __TEXT,__const  protocol conformance descriptor for os.OSLogFloatFormatting.Notation : Swift.Equatable in os
0x19e6bf38c  __TEXT,__text  os.OSLogFloatFormatting.notation.modify : os.OSLogFloatFormatting.Notation
0x19e6bf374  __TEXT,__text  os.OSLogFloatFormatting.notation.getter : os.OSLogFloatFormatting.Notation
0x19e6cec04  __TEXT,__const  property descriptor for os.OSLogFloatFormatting.notation : os.OSLogFloatFormatting.Notation
0x19e6bf380  __TEXT,__text  os.OSLogFloatFormatting.notation.setter : os.OSLogFloatFormatting.Notation
0x19e6bf2cc  __TEXT,__text  os.OSLogFloatFormatting.precision.modify : (() -> Swift.Int)?
0x19e6bf260  __TEXT,__text  os.OSLogFloatFormatting.precision.getter : (() -> Swift.Int)?
0x1e0d81bc8  __DATA_CONST,__const  property descriptor for os.OSLogFloatFormatting.precision : (() -> Swift.Int)?
0x19e6bf294  __TEXT,__text  os.OSLogFloatFormatting.precision.setter : (() -> Swift.Int)?
0x19e6bf130  __TEXT,__text  os.OSLogFloatFormatting.uppercase.modify : Swift.Bool
0x19e6bf120  __TEXT,__text  os.OSLogFloatFormatting.uppercase.getter : Swift.Bool
0x19e6cebfc  __TEXT,__const  property descriptor for os.OSLogFloatFormatting.uppercase : Swift.Bool
0x19e6bf128  __TEXT,__text  os.OSLogFloatFormatting.uppercase.setter : Swift.Bool
0x19e6bf8f0  __TEXT,__text  type metadata accessor for os.OSLogFloatFormatting
0x19e6d0934  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogFloatFormatting
0x1e42014e8  __AUTH_CONST,__const  type metadata for os.OSLogFloatFormatting
0x19e6c72a8  __TEXT,__text  os.OSLogStringAlignment.init(minimumColumnWidth: (() -> Swift.Int)?, anchor: os.OSLogCollectionBound) -> os.OSLogStringAlignment
0x19e6c7250  __TEXT,__text  os.OSLogStringAlignment.minimumColumnWidth.modify : (() -> Swift.Int)?
0x19e6c71e4  __TEXT,__text  os.OSLogStringAlignment.minimumColumnWidth.getter : (() -> Swift.Int)?
0x1e0d81be8  __DATA_CONST,__const  property descriptor for os.OSLogStringAlignment.minimumColumnWidth : (() -> Swift.Int)?
0x19e6c7218  __TEXT,__text  os.OSLogStringAlignment.minimumColumnWidth.setter : (() -> Swift.Int)?
0x19e6c72c0  __TEXT,__text  static os.OSLogStringAlignment.left(columns: @autoclosure () -> Swift.Int) -> os.OSLogStringAlignment
0x19e6c6f5c  __TEXT,__text  static os.OSLogStringAlignment.none.getter : os.OSLogStringAlignment
0x19e6cf4f8  __TEXT,__const  property descriptor for static os.OSLogStringAlignment.none : os.OSLogStringAlignment
0x19e6c72b8  __TEXT,__text  static os.OSLogStringAlignment.right(columns: @autoclosure () -> Swift.Int) -> os.OSLogStringAlignment
0x19e6c7288  __TEXT,__text  os.OSLogStringAlignment.anchor.modify : os.OSLogCollectionBound
0x19e6c7270  __TEXT,__text  os.OSLogStringAlignment.anchor.getter : os.OSLogCollectionBound
0x19e6cf4fc  __TEXT,__const  property descriptor for os.OSLogStringAlignment.anchor : os.OSLogCollectionBound
0x19e6c727c  __TEXT,__text  os.OSLogStringAlignment.anchor.setter : os.OSLogCollectionBound
0x19e6c748c  __TEXT,__text  type metadata accessor for os.OSLogStringAlignment
0x19e6d0af4  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogStringAlignment
0x1e4201468  __AUTH_CONST,__const  type metadata for os.OSLogStringAlignment
0x19e6be06c  __TEXT,__text  os.AnimationFormatString.OSLogMessage.formatStringPointer.modify : Swift.UnsafePointer<Swift.Int8>
0x19e6be060  __TEXT,__text  os.AnimationFormatString.OSLogMessage.formatStringPointer.getter : Swift.UnsafePointer<Swift.Int8>
0x19e6ceab0  __TEXT,__const  property descriptor for os.AnimationFormatString.OSLogMessage.formatStringPointer : Swift.UnsafePointer<Swift.Int8>
0x19e6be064  __TEXT,__text  os.AnimationFormatString.OSLogMessage.formatStringPointer.setter : Swift.UnsafePointer<Swift.Int8>
0x19e6ce174  __TEXT,__text  os.AnimationFormatString.OSLogMessage.init(stringLiteral: Swift.String) -> os.AnimationFormatString.OSLogMessage
0x19e6bef24  __TEXT,__text  type metadata accessor for os.AnimationFormatString.OSLogMessage
0x19e6d08b8  __TEXT,__constg_swiftt  nominal type descriptor for os.AnimationFormatString.OSLogMessage
0x1e42013e8  __AUTH_CONST,__const  type metadata for os.AnimationFormatString.OSLogMessage
0x19e6ce920  __TEXT,__const  protocol conformance descriptor for os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByStringLiteral in os
0x19e6ce9a0  __TEXT,__const  protocol conformance descriptor for os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByUnicodeScalarLiteral in os
0x19e6ce960  __TEXT,__const  protocol conformance descriptor for os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6bdf74  __TEXT,__text  static os.AnimationFormatString.constructOSLogInterpolation(Swift.String) -> os.OSLogInterpolation
0x19e6bee94  __TEXT,__text  type metadata accessor for os.AnimationFormatString
0x19e6d089c  __TEXT,__constg_swiftt  nominal type descriptor for os.AnimationFormatString
0x1e4201370  __AUTH_CONST,__const  type metadata for os.AnimationFormatString
0x19e6cfa80  __TEXT,__const  property descriptor for os.OSAllocatedUnfairLock.__lock : Swift.ManagedBuffer<A, __C.os_unfair_lock_s>
0x19e6cde20  __TEXT,__text  static os.OSAllocatedUnfairLock.Ownership.== infix(os.OSAllocatedUnfairLock<A>.Ownership, os.OSAllocatedUnfairLock<A>.Ownership) -> Swift.Bool
0x19e6cde30  __TEXT,__text  os.OSAllocatedUnfairLock.Ownership.hash(into: inout Swift.Hasher) -> ()
0x19e6cde58  __TEXT,__text  os.OSAllocatedUnfairLock.Ownership.hashValue.getter : Swift.Int
0x19e6cfa7c  __TEXT,__const  property descriptor for os.OSAllocatedUnfairLock.Ownership.hashValue : Swift.Int
0x19e6ce090  __TEXT,__text  type metadata accessor for os.OSAllocatedUnfairLock.Ownership
0x19e6d0c60  __TEXT,__constg_swiftt  nominal type descriptor for os.OSAllocatedUnfairLock.Ownership
0x19e6cfa38  __TEXT,__const  protocol conformance descriptor for os.OSAllocatedUnfairLock<A>.Ownership : Swift.Hashable in os
0x19e6cfa10  __TEXT,__const  protocol conformance descriptor for os.OSAllocatedUnfairLock<A>.Ownership : Swift.Equatable in os
0x19e6ba6dc  __TEXT,__text  type metadata accessor for os.OSAllocatedUnfairLock
0x19e6d0c30  __TEXT,__constg_swiftt  nominal type descriptor for os.OSAllocatedUnfairLock
0x19e6c3138  __TEXT,__text  os.maxOSLogArgumentCount.getter : Swift.UInt8
0x19e6cf47c  __TEXT,__const  enum case for os.OSLogIntExtendedFormat.bitrateIEC(os.OSLogIntExtendedFormat.Type) -> os.OSLogIntExtendedFormat
0x19e6cf484  __TEXT,__const  enum case for os.OSLogIntExtendedFormat.byteCountIEC(os.OSLogIntExtendedFormat.Type) -> os.OSLogIntExtendedFormat
0x19e6cf488  __TEXT,__const  enum case for os.OSLogIntExtendedFormat.secondsSince1970(os.OSLogIntExtendedFormat.Type) -> os.OSLogIntExtendedFormat
0x19e6c6f20  __TEXT,__text  static os.OSLogIntExtendedFormat.== infix(os.OSLogIntExtendedFormat, os.OSLogIntExtendedFormat) -> Swift.Bool
0x19e6cf3e8  __TEXT,__const  property descriptor for os.OSLogIntExtendedFormat.tag : Swift.String
0x19e6c6f10  __TEXT,__text  os.OSLogIntExtendedFormat.hash(into: inout Swift.Hasher) -> ()
0x19e6cf478  __TEXT,__const  enum case for os.OSLogIntExtendedFormat.bitrate(os.OSLogIntExtendedFormat.Type) -> os.OSLogIntExtendedFormat
0x19e6cf480  __TEXT,__const  enum case for os.OSLogIntExtendedFormat.byteCount(os.OSLogIntExtendedFormat.Type) -> os.OSLogIntExtendedFormat
0x19e6c6f18  __TEXT,__text  os.OSLogIntExtendedFormat.hashValue.getter : Swift.Int
0x19e6cf3e8  __TEXT,__const  property descriptor for os.OSLogIntExtendedFormat.hashValue : Swift.Int
0x19e6c6eec  __TEXT,__text  type metadata accessor for os.OSLogIntExtendedFormat
0x19e6d0abc  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogIntExtendedFormat
0x1e4201270  __AUTH_CONST,__const  type metadata for os.OSLogIntExtendedFormat
0x19e6cf3a8  __TEXT,__const  protocol conformance descriptor for os.OSLogIntExtendedFormat : Swift.Hashable in os
0x19e6cf380  __TEXT,__const  protocol conformance descriptor for os.OSLogIntExtendedFormat : Swift.Equatable in os
0x19e6c05a4  __TEXT,__text  os.OSLogIntegerFormatting.includePrefix.modify : Swift.Bool
0x19e6c0594  __TEXT,__text  os.OSLogIntegerFormatting.includePrefix.getter : Swift.Bool
0x19e6cec98  __TEXT,__const  property descriptor for os.OSLogIntegerFormatting.includePrefix : Swift.Bool
0x19e6c059c  __TEXT,__text  os.OSLogIntegerFormatting.includePrefix.setter : Swift.Bool
0x19e6cd0b4  __TEXT,__text  os.OSLogIntegerFormatting.formatSpecifier<A where A: Swift.FixedWidthInteger>(for: A.Type, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> Swift.String
0x19e6c0574  __TEXT,__text  os.OSLogIntegerFormatting.explicitPositiveSign.modify : Swift.Bool
0x19e6c0564  __TEXT,__text  os.OSLogIntegerFormatting.explicitPositiveSign.getter : Swift.Bool
0x19e6cec94  __TEXT,__const  property descriptor for os.OSLogIntegerFormatting.explicitPositiveSign : Swift.Bool
0x19e6c056c  __TEXT,__text  os.OSLogIntegerFormatting.explicitPositiveSign.setter : Swift.Bool
0x19e6c0cb8  __TEXT,__text  static os.OSLogIntegerFormatting.formatSpecifierLengthModifier<A where A: Swift.FixedWidthInteger>(A.Type) -> Swift.String?
0x19e6c0884  __TEXT,__text  static os.OSLogIntegerFormatting.hex(explicitPositiveSign: Swift.Bool, includePrefix: Swift.Bool, uppercase: Swift.Bool, minDigits: @autoclosure () -> Swift.Int) -> os.OSLogIntegerFormatting
0x19e6c0898  __TEXT,__text  static os.OSLogIntegerFormatting.hex(explicitPositiveSign: Swift.Bool, includePrefix: Swift.Bool, uppercase: Swift.Bool) -> os.OSLogIntegerFormatting
0x19e6c08ac  __TEXT,__text  static os.OSLogIntegerFormatting.hex.getter : os.OSLogIntegerFormatting
0x19e6ceca0  __TEXT,__const  property descriptor for static os.OSLogIntegerFormatting.hex : os.OSLogIntegerFormatting
0x19e6c0900  __TEXT,__text  static os.OSLogIntegerFormatting.octal(explicitPositiveSign: Swift.Bool, includePrefix: Swift.Bool, uppercase: Swift.Bool, minDigits: @autoclosure () -> Swift.Int) -> os.OSLogIntegerFormatting
0x19e6c09f0  __TEXT,__text  static os.OSLogIntegerFormatting.octal(explicitPositiveSign: Swift.Bool, includePrefix: Swift.Bool, uppercase: Swift.Bool) -> os.OSLogIntegerFormatting
0x19e6c0ac0  __TEXT,__text  static os.OSLogIntegerFormatting.octal.getter : os.OSLogIntegerFormatting
0x19e6ceca0  __TEXT,__const  property descriptor for static os.OSLogIntegerFormatting.octal : os.OSLogIntegerFormatting
0x19e6c0794  __TEXT,__text  os.OSLogIntegerFormatting.init(radix: Swift.Int, explicitPositiveSign: Swift.Bool, includePrefix: Swift.Bool, uppercase: Swift.Bool, minDigits: (() -> Swift.Int)?) -> os.OSLogIntegerFormatting
0x19e6c0544  __TEXT,__text  os.OSLogIntegerFormatting.radix.modify : Swift.Int
0x19e6c0538  __TEXT,__text  os.OSLogIntegerFormatting.radix.getter : Swift.Int
0x19e6cec90  __TEXT,__const  property descriptor for os.OSLogIntegerFormatting.radix : Swift.Int
0x19e6c053c  __TEXT,__text  os.OSLogIntegerFormatting.radix.setter : Swift.Int
0x19e6c0bd4  __TEXT,__text  os.OSLogIntegerFormatting._prefix.getter : Swift.String
0x19e6ceca0  __TEXT,__const  property descriptor for os.OSLogIntegerFormatting._prefix : Swift.String
0x19e6c07c0  __TEXT,__text  static os.OSLogIntegerFormatting.decimal(explicitPositiveSign: Swift.Bool, minDigits: @autoclosure () -> Swift.Int) -> os.OSLogIntegerFormatting
0x19e6ba904  __TEXT,__text  static os.OSLogIntegerFormatting.decimal(explicitPositiveSign: Swift.Bool) -> os.OSLogIntegerFormatting
0x19e6ba9e0  __TEXT,__text  static os.OSLogIntegerFormatting.decimal.getter : os.OSLogIntegerFormatting
0x19e6ceca0  __TEXT,__const  property descriptor for static os.OSLogIntegerFormatting.decimal : os.OSLogIntegerFormatting
0x19e6c0774  __TEXT,__text  os.OSLogIntegerFormatting.minDigits.modify : (() -> Swift.Int)?
0x19e6c0704  __TEXT,__text  os.OSLogIntegerFormatting.minDigits.getter : (() -> Swift.Int)?
0x1e0d81bd8  __DATA_CONST,__const  property descriptor for os.OSLogIntegerFormatting.minDigits : (() -> Swift.Int)?
0x19e6c073c  __TEXT,__text  os.OSLogIntegerFormatting.minDigits.setter : (() -> Swift.Int)?
0x19e6c05d4  __TEXT,__text  os.OSLogIntegerFormatting.uppercase.modify : Swift.Bool
0x19e6c05c4  __TEXT,__text  os.OSLogIntegerFormatting.uppercase.getter : Swift.Bool
0x19e6cec9c  __TEXT,__const  property descriptor for os.OSLogIntegerFormatting.uppercase : Swift.Bool
0x19e6c05cc  __TEXT,__text  os.OSLogIntegerFormatting.uppercase.setter : Swift.Bool
0x19e6c0f7c  __TEXT,__text  type metadata accessor for os.OSLogIntegerFormatting
0x19e6d096c  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogIntegerFormatting
0x1e42011c8  __AUTH_CONST,__const  type metadata for os.OSLogIntegerFormatting
0x19e6cc6b4  __TEXT,__text  static os.OSSignpostIntervalState.beginState(id: os.OSSignpostID) -> os.OSSignpostIntervalState
0x19e6ba8ac  __TEXT,__text  os.OSSignpostIntervalState.signpostID.getter : os.OSSignpostID
0x19e6cf6b0  __TEXT,__const  property descriptor for os.OSSignpostIntervalState.signpostID : os.OSSignpostID
0x19e6ca550  __TEXT,__text  os.OSSignpostIntervalState.__allocating_init(id: os.OSSignpostID, isOpen: Swift.Bool) -> os.OSSignpostIntervalState
0x19e6ccd8c  __TEXT,__text  dispatch thunk of os.OSSignpostIntervalState.__allocating_init(id: os.OSSignpostID, isOpen: Swift.Bool) -> os.OSSignpostIntervalState
0x19e6d0bb0  __TEXT,__constg_swiftt  method descriptor for os.OSSignpostIntervalState.__allocating_init(id: os.OSSignpostID, isOpen: Swift.Bool) -> os.OSSignpostIntervalState
0x19e6ba858  __TEXT,__text  os.OSSignpostIntervalState.init(id: os.OSSignpostID, isOpen: Swift.Bool) -> os.OSSignpostIntervalState
0x19e6cc848  __TEXT,__text  os.OSSignpostIntervalState.__allocating_init(from: Swift.Decoder) throws -> os.OSSignpostIntervalState
0x19e6ccda0  __TEXT,__text  dispatch thunk of os.OSSignpostIntervalState.__allocating_init(from: Swift.Decoder) throws -> os.OSSignpostIntervalState
0x19e6d0bb8  __TEXT,__constg_swiftt  method descriptor for os.OSSignpostIntervalState.__allocating_init(from: Swift.Decoder) throws -> os.OSSignpostIntervalState
0x19e6cc894  __TEXT,__text  os.OSSignpostIntervalState.init(from: Swift.Decoder) throws -> os.OSSignpostIntervalState
0x19e6ccdc8  __TEXT,__text  dispatch thunk of os.OSSignpostIntervalState.encode(to: Swift.Encoder) throws -> ()
0x19e6d0bc0  __TEXT,__constg_swiftt  method descriptor for os.OSSignpostIntervalState.encode(to: Swift.Encoder) throws -> ()
0x19e6ccdf8  __TEXT,__text  dispatch thunk of os.OSSignpostIntervalState._hasValue(id: os.OSSignpostID, isOpen: Swift.Bool) -> Swift.Bool
0x19e6d0bc8  __TEXT,__constg_swiftt  method descriptor for os.OSSignpostIntervalState._hasValue(id: os.OSSignpostID, isOpen: Swift.Bool) -> Swift.Bool
0x19e6ba4c8  __TEXT,__text  type metadata accessor for os.OSSignpostIntervalState
0x1ee0070f0  __DATA_DIRTY,__data  metaclass for os.OSSignpostIntervalState
0x19e6d0b64  __TEXT,__constg_swiftt  nominal type descriptor for os.OSSignpostIntervalState
0x19e6cf728  __TEXT,__const  class metadata base offset for os.OSSignpostIntervalState
0x19e6ccd74  __TEXT,__text  method lookup function for os.OSSignpostIntervalState
0x1ee006f38  __DATA_DIRTY,__data  type metadata for os.OSSignpostIntervalState
0x19e6cf680  __TEXT,__const  protocol conformance descriptor for os.OSSignpostIntervalState : Swift.Encodable in os
0x19e6cf658  __TEXT,__const  protocol conformance descriptor for os.OSSignpostIntervalState : Swift.Decodable in os
0x19e6b8654  __TEXT,__text  os.OSSignpostIntervalState.__deallocating_deinit
0x19e6cca78  __TEXT,__text  os.OSSignpostIntervalState.deinit
0x19e6cf448  __TEXT,__const  enum case for os.OSLogInt32ExtendedFormat.bitrateIEC(os.OSLogInt32ExtendedFormat.Type) -> os.OSLogInt32ExtendedFormat
0x19e6cf438  __TEXT,__const  enum case for os.OSLogInt32ExtendedFormat.darwinMode(os.OSLogInt32ExtendedFormat.Type) -> os.OSLogInt32ExtendedFormat
0x19e6cf434  __TEXT,__const  enum case for os.OSLogInt32ExtendedFormat.darwinErrno(os.OSLogInt32ExtendedFormat.Type) -> os.OSLogInt32ExtendedFormat
0x19e6cf42c  __TEXT,__const  enum case for os.OSLogInt32ExtendedFormat.ipv4Address(os.OSLogInt32ExtendedFormat.Type) -> os.OSLogInt32ExtendedFormat
0x19e6cf450  __TEXT,__const  enum case for os.OSLogInt32ExtendedFormat.byteCountIEC(os.OSLogInt32ExtendedFormat.Type) -> os.OSLogInt32ExtendedFormat
0x19e6cf43c  __TEXT,__const  enum case for os.OSLogInt32ExtendedFormat.darwinSignal(os.OSLogInt32ExtendedFormat.Type) -> os.OSLogInt32ExtendedFormat
0x19e6cf430  __TEXT,__const  enum case for os.OSLogInt32ExtendedFormat.secondsSince1970(os.OSLogInt32ExtendedFormat.Type) -> os.OSLogInt32ExtendedFormat
0x19e6c6f1c  __TEXT,__text  static os.OSLogInt32ExtendedFormat.== infix(os.OSLogInt32ExtendedFormat, os.OSLogInt32ExtendedFormat) -> Swift.Bool
0x19e6c6f0c  __TEXT,__text  os.OSLogInt32ExtendedFormat.hash(into: inout Swift.Hasher) -> ()
0x19e6cf454  __TEXT,__const  enum case for os.OSLogInt32ExtendedFormat.truth(os.OSLogInt32ExtendedFormat.Type) -> os.OSLogInt32ExtendedFormat
0x19e6cf458  __TEXT,__const  enum case for os.OSLogInt32ExtendedFormat.answer(os.OSLogInt32ExtendedFormat.Type) -> os.OSLogInt32ExtendedFormat
0x19e6cf444  __TEXT,__const  enum case for os.OSLogInt32ExtendedFormat.bitrate(os.OSLogInt32ExtendedFormat.Type) -> os.OSLogInt32ExtendedFormat
0x19e6cf44c  __TEXT,__const  enum case for os.OSLogInt32ExtendedFormat.byteCount(os.OSLogInt32ExtendedFormat.Type) -> os.OSLogInt32ExtendedFormat
0x19e6c6f14  __TEXT,__text  os.OSLogInt32ExtendedFormat.hashValue.getter : Swift.Int
0x19e6cf3e8  __TEXT,__const  property descriptor for os.OSLogInt32ExtendedFormat.hashValue : Swift.Int
0x19e6cf440  __TEXT,__const  enum case for os.OSLogInt32ExtendedFormat.machErrno(os.OSLogInt32ExtendedFormat.Type) -> os.OSLogInt32ExtendedFormat
0x19e6c6d9c  __TEXT,__text  type metadata accessor for os.OSLogInt32ExtendedFormat
0x19e6d0aa0  __TEXT,__constg_swiftt  nominal type descriptor for os.OSLogInt32ExtendedFormat
0x1e42010c0  __AUTH_CONST,__const  type metadata for os.OSLogInt32ExtendedFormat
0x19e6cf340  __TEXT,__const  protocol conformance descriptor for os.OSLogInt32ExtendedFormat : Swift.Hashable in os
0x19e6cf318  __TEXT,__const  protocol conformance descriptor for os.OSLogInt32ExtendedFormat : Swift.Equatable in os
0x19e6bd7b8  __TEXT,__text  static os.OSMetricStatisticalLevel.== infix(os.OSMetricStatisticalLevel, os.OSMetricStatisticalLevel) -> Swift.Bool
0x19e6bd778  __TEXT,__text  os.OSMetricStatisticalLevel.hash(into: inout Swift.Hasher) -> ()
0x19e6ce66c  __TEXT,__const  enum case for os.OSMetricStatisticalLevel.none(os.OSMetricStatisticalLevel.Type) -> os.OSMetricStatisticalLevel
0x19e6ce670  __TEXT,__const  enum case for os.OSMetricStatisticalLevel.basic(os.OSMetricStatisticalLevel.Type) -> os.OSMetricStatisticalLevel
0x19e6ce674  __TEXT,__const  enum case for os.OSMetricStatisticalLevel.detail(os.OSMetricStatisticalLevel.Type) -> os.OSMetricStatisticalLevel
0x19e6bd7ac  __TEXT,__text  os.OSMetricStatisticalLevel.hashValue.getter : Swift.Int
0x19e6ce5ec  __TEXT,__const  property descriptor for os.OSMetricStatisticalLevel.hashValue : Swift.Int
0x19e6bd000  __TEXT,__text  type metadata accessor for os.OSMetricStatisticalLevel
0x19e6d06fc  __TEXT,__constg_swiftt  nominal type descriptor for os.OSMetricStatisticalLevel
0x1e4201030  __AUTH_CONST,__const  type metadata for os.OSMetricStatisticalLevel
0x19e6ce2e0  __TEXT,__const  protocol conformance descriptor for os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6ce2b8  __TEXT,__const  protocol conformance descriptor for os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6ceb2c  __TEXT,__const  enum case for os.OSSignpostAnimationBegin.animationBegin(os.OSSignpostAnimationBegin.Type) -> os.OSSignpostAnimationBegin
0x19e6be0dc  __TEXT,__text  static os.OSSignpostAnimationBegin.== infix(os.OSSignpostAnimationBegin, os.OSSignpostAnimationBegin) -> Swift.Bool
0x19e6be0e4  __TEXT,__text  os.OSSignpostAnimationBegin.hash(into: inout Swift.Hasher) -> ()
0x19e6be10c  __TEXT,__text  os.OSSignpostAnimationBegin.hashValue.getter : Swift.Int
0x19e6ceab4  __TEXT,__const  property descriptor for os.OSSignpostAnimationBegin.hashValue : Swift.Int
0x19e6bf000  __TEXT,__text  type metadata accessor for os.OSSignpostAnimationBegin
0x19e6d08d4  __TEXT,__constg_swiftt  nominal type descriptor for os.OSSignpostAnimationBegin
0x1e4200fa0  __AUTH_CONST,__const  type metadata for os.OSSignpostAnimationBegin
0x19e6cea00  __TEXT,__const  protocol conformance descriptor for os.OSSignpostAnimationBegin : Swift.Hashable in os
0x19e6ce9d8  __TEXT,__const  protocol conformance descriptor for os.OSSignpostAnimationBegin : Swift.Equatable in os
0x19e6cdc24  __TEXT,__text  static os.OSAllocatedUnfairLockFlags.adaptiveSpin.getter : os.OSAllocatedUnfairLockFlags
0x19e6cfa7c  __TEXT,__const  property descriptor for static os.OSAllocatedUnfairLockFlags.adaptiveSpin : os.OSAllocatedUnfairLockFlags
0x19e6cdc30  __TEXT,__text  os.OSAllocatedUnfairLockFlags._translatedValue.getter : __C.os_unfair_lock_flags_t
0x19e6cfa7c  __TEXT,__const  property descriptor for os.OSAllocatedUnfairLockFlags._translatedValue : __C.os_unfair_lock_flags_t
0x19e6cdc0c  __TEXT,__text  os.OSAllocatedUnfairLockFlags.init(rawValue: Swift.UInt32) -> os.OSAllocatedUnfairLockFlags
0x19e6cdc04  __TEXT,__text  os.OSAllocatedUnfairLockFlags.rawValue.getter : Swift.UInt32
0x19e6cfa78  __TEXT,__const  property descriptor for os.OSAllocatedUnfairLockFlags.rawValue : Swift.UInt32
0x19e6ce078  __TEXT,__text  type metadata accessor for os.OSAllocatedUnfairLockFlags
0x19e6d0c14  __TEXT,__constg_swiftt  nominal type descriptor for os.OSAllocatedUnfairLockFlags
0x1e4200f08  __AUTH_CONST,__const  type metadata for os.OSAllocatedUnfairLockFlags
0x19e6cf9b8  __TEXT,__const  protocol conformance descriptor for os.OSAllocatedUnfairLockFlags : Swift.Equatable in os
0x19e6cf8b8  __TEXT,__const  protocol conformance descriptor for os.OSAllocatedUnfairLockFlags : Swift.RawRepresentable in os
0x19e6cf8f0  __TEXT,__const  protocol conformance descriptor for os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cf9e0  __TEXT,__const  protocol conformance descriptor for os.OSAllocatedUnfairLockFlags : Swift.ExpressibleByArrayLiteral in os
0x19e6cf880  __TEXT,__const  protocol conformance descriptor for os.OSAllocatedUnfairLockFlags : Swift.OptionSet in os
0x19e6c7e44  __TEXT,__text  os._checkFormatStringAndBuffer(_: os.OSLogMessage, with: (Swift.String, Swift.UnsafeBufferPointer<Swift.UInt8>) -> ()) -> ()
0x19e6be204  __TEXT,__text  os.animationBeginSignpostHelper(dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name: Swift.StaticString, signpostID: os.OSSignpostID, formatStringPointer: Swift.UnsafePointer<Swift.Int8>, arguments: [Swift.CVarArg]) -> ()
0x19e6ba8b8  __TEXT,__text  os.checkForErrorAndConsumeState(state: os.OSSignpostIntervalState) -> os.OSSignpostError
0x19e6cd1f4  __TEXT,__text  os.getNullTerminatedUTF8Pointer(_: Swift.String, using: inout Swift.UnsafeMutablePointer<Any>?) -> Swift.UnsafeRawPointer
0x19e6c7640  __TEXT,__text  os.Logger.log(level: __C.os_log_type_t, _: os.OSLogMessage) -> ()
0x19e6c7528  __TEXT,__text  os.Logger.log(os.OSLogMessage) -> ()
0x19e6c78c0  __TEXT,__text  os.Logger.info(os.OSLogMessage) -> ()
0x19e6c78a8  __TEXT,__text  os.Logger.debug(os.OSLogMessage) -> ()
0x19e6c78d8  __TEXT,__text  os.Logger.error(os.OSLogMessage) -> ()
0x19e6c78f0  __TEXT,__text  os.Logger.fault(os.OSLogMessage) -> ()
0x19e6c81dc  __TEXT,__text  os.Logger.trace(os.OSLogMessage) -> ()
0x19e6c81e0  __TEXT,__text  os.Logger.notice(os.OSLogMessage) -> ()
0x19e6c81e4  __TEXT,__text  os.Logger.warning(os.OSLogMessage) -> ()
0x19e6c81e8  __TEXT,__text  os.Logger.critical(os.OSLogMessage) -> ()
0x19e6b8048  __TEXT,__text  static os.Logger.disabled.getter : os.Logger
0x19e6cf58c  __TEXT,__const  property descriptor for static os.Logger.disabled : os.Logger
0x19e6c7504  __TEXT,__text  os.Logger.isEnabled(type: __C.os_log_type_t) -> Swift.Bool
0x19e6b8030  __TEXT,__text  os.Logger.logObject.getter : __C.OS_os_log
0x19e6cf588  __TEXT,__const  property descriptor for os.Logger.logObject : __C.OS_os_log
0x19e6b9b78  __TEXT,__text  os.Logger.init(subsystem: Swift.String, category: Swift.String) -> os.Logger
0x19e6ba4a4  __TEXT,__text  os.Logger.init() -> os.Logger
0x19e6b8038  __TEXT,__text  type metadata accessor for os.Logger
0x19e6d0b10  __TEXT,__constg_swiftt  nominal type descriptor for os.Logger
0x1e4200e88  __AUTH_CONST,__const  type metadata for os.Logger
0x19e6ba6b4  __TEXT,__text  os.Logger.init(__C.OS_os_log) -> os.Logger
0x19e6cd1a0  __TEXT,__text  os.serialize(_: Swift.String, at: inout Swift.UnsafeMutablePointer<Swift.UInt8>, using: inout Swift.UnsafeMutablePointer<Any>?) -> ()
0x19e6c35a8  __TEXT,__text  (extension in os):Swift.String.percentEscapedString.getter : Swift.String
0x19e6ceed0  __TEXT,__const  property descriptor for (extension in os):Swift.String.percentEscapedString : Swift.String
0x19e6b8664  __TEXT,__text  static (extension in os):__C.os_log_type_t.info.getter : __C.os_log_type_t
0x19e6b80c8  __TEXT,__text  static (extension in os):__C.os_log_type_t.debug.getter : __C.os_log_type_t
0x19e6b9bf8  __TEXT,__text  static (extension in os):__C.os_log_type_t.error.getter : __C.os_log_type_t
0x19e6ba878  __TEXT,__text  static (extension in os):__C.os_log_type_t.fault.getter : __C.os_log_type_t
0x19e6b9aa4  __TEXT,__text  static (extension in os):__C.os_log_type_t.default.getter : __C.os_log_type_t
0x19e6cd544  __TEXT,__text  (extension in os):__C.OS_os_workgroup.isCancelled.getter : Swift.Bool
0x19e6cf850  __TEXT,__const  property descriptor for (extension in os):__C.OS_os_workgroup.isCancelled : Swift.Bool
0x19e6cd664  __TEXT,__text  (extension in os):__C.OS_os_workgroup.workingArena.getter : (Swift.UnsafeMutableRawPointer?, Swift.UInt32)
0x19e6cf850  __TEXT,__const  property descriptor for (extension in os):__C.OS_os_workgroup.workingArena : (Swift.UnsafeMutableRawPointer?, Swift.UInt32)
0x19e6cd7a4  __TEXT,__text  (extension in os):__C.OS_os_workgroup.updateDeadline(deadline: Swift.UInt64) -> ()
0x19e6cd584  __TEXT,__text  (extension in os):__C.OS_os_workgroup.setWorkingArena(arena: Swift.UnsafeMutableRawPointer?, max_workers: Swift.UInt32, destruct: @convention(c) (Swift.UnsafeMutableRawPointer?) -> ()) -> ()
0x19e6cd560  __TEXT,__text  (extension in os):__C.OS_os_workgroup.maxParallelThreads.getter : Swift.Int
0x19e6cf850  __TEXT,__const  property descriptor for (extension in os):__C.OS_os_workgroup.maxParallelThreads : Swift.Int
0x19e6cd388  __TEXT,__text  (extension in os):__C.OS_os_workgroup.copy(name: Swift.String?) -> __C.OS_os_workgroup?
0x19e6cd3f4  __TEXT,__text  (extension in os):__C.OS_os_workgroup.join() -> (extension in os):__C.OS_os_workgroup.JoinToken
0x19e6cd304  __TEXT,__text  (extension in os):__C.OS_os_workgroup.init(port: Swift.UInt32, name: Swift.String?) -> __C.OS_os_workgroup?
0x19e6cd4d8  __TEXT,__text  (extension in os):__C.OS_os_workgroup.leave(token: (extension in os):__C.OS_os_workgroup.JoinToken) -> ()
0x19e6cd6c0  __TEXT,__text  (extension in os):__C.OS_os_workgroup.start(at: Swift.UInt64, deadline: Swift.UInt64) -> ()
0x19e6cd53c  __TEXT,__text  (extension in os):__C.OS_os_workgroup.cancel() -> ()
0x19e6cd884  __TEXT,__text  (extension in os):__C.OS_os_workgroup.finish() -> ()
0x19e6cd1f8  __TEXT,__text  (extension in os):__C.OS_os_workgroup.copyPort() -> Swift.UInt32
0x19e6cda1c  __TEXT,__text  type metadata accessor for (extension in os):__C.OS_os_workgroup.JoinToken
0x19e6d0bf8  __TEXT,__constg_swiftt  nominal type descriptor for (extension in os):__C.OS_os_workgroup.JoinToken
0x1e4200e08  __AUTH_CONST,__const  type metadata for (extension in os):__C.OS_os_workgroup.JoinToken
0x19e6ba50c  __TEXT,__text  static (extension in os):__C.os_signpost_type_t.end.getter : __C.os_signpost_type_t
0x19e6b9b24  __TEXT,__text  static (extension in os):__C.os_signpost_type_t.begin.getter : __C.os_signpost_type_t
0x19e6ba514  __TEXT,__text  static (extension in os):__C.os_signpost_type_t.event.getter : __C.os_signpost_type_t
0x19e6cd960  __TEXT,__text  (extension in os):__C.OS_os_workgroup_parallel.init(name: Swift.String?) -> __C.OS_os_workgroup_parallel?
0x19e6ba880  __TEXT,__text  (extension in os):__C.OS_os_log.signpostsEnabled.getter : Swift.Bool
0x19e6ceab4  __TEXT,__const  property descriptor for (extension in os):__C.OS_os_log.signpostsEnabled : Swift.Bool
0x19e6ba048  __TEXT,__text  static (extension in os):__C.OS_os_log.default.getter : __C.OS_os_log
0x19e6beb4c  __TEXT,__text  static (extension in os):__C.OS_os_log.Category.dynamicTracing.getter : (extension in os):__C.OS_os_log.Category
0x19e6ba51c  __TEXT,__text  static (extension in os):__C.OS_os_log.Category.pointsOfInterest.getter : (extension in os):__C.OS_os_log.Category
0x19e6ceab4  __TEXT,__const  property descriptor for static (extension in os):__C.OS_os_log.Category.pointsOfInterest : (extension in os):__C.OS_os_log.Category
0x19e6beba0  __TEXT,__text  static (extension in os):__C.OS_os_log.Category.dynamicStackTracing.getter : (extension in os):__C.OS_os_log.Category
0x19e6bea80  __TEXT,__text  (extension in os):__C.OS_os_log.Category.rawValue.getter : Swift.String
0x19e6ceabc  __TEXT,__const  property descriptor for (extension in os):__C.OS_os_log.Category.rawValue : Swift.String
0x19e6bf09c  __TEXT,__text  type metadata accessor for (extension in os):__C.OS_os_log.Category
0x19e6d0918  __TEXT,__constg_swiftt  nominal type descriptor for (extension in os):__C.OS_os_log.Category
0x1e4200cb0  __AUTH_CONST,__const  type metadata for (extension in os):__C.OS_os_log.Category
0x19e6ba9bc  __TEXT,__text  static (extension in os):__C.OS_os_log.disabled.getter : __C.OS_os_log
0x19e6beab0  __TEXT,__text  (extension in os):__C.OS_os_log.init(subsystem: Swift.String, category: (extension in os):__C.OS_os_log.Category) -> __C.OS_os_log
0x19e6ba5f8  __TEXT,__text  (extension in os):__C.OS_os_log.init(subsystem: Swift.String, category: Swift.String) -> __C.OS_os_log
0x1ebbc3bd4  __DATA,__common  __swift_FORCE_LOAD_$_swiftos
0x19e6b8a90  __TEXT,__text  __swift_os_log
0x19e6b80e0  __TEXT,__text  __swift_os_log_return_address
0x19e6ba210  __TEXT,__text  __swift_os_signpost
0x19e6b9940  __TEXT,__text  __swift_os_signpost_with_format
```

## Private

```
0x19e6b806c  __TEXT,__text  merged static os.Logger.disabled.getter : os.Logger
0x19e6b806c  __TEXT,__text  merged static os.Logger.disabled.getter : os.Logger
0x19e6b80bc  __TEXT,__text  getEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6b80bc  __TEXT,__text  getEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6b80bc  __TEXT,__text  getEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6b80bc  __TEXT,__text  getEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6b80bc  __TEXT,__text  getEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6b80bc  __TEXT,__text  getEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6b80bc  __TEXT,__text  getEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6b80bc  __TEXT,__text  getEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6b80bc  __TEXT,__text  getEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6b80bc  __TEXT,__text  getEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6b80bc  __TEXT,__text  getEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6b80bc  __TEXT,__text  getEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6b80c0  __TEXT,__text  getEnumTag value witness for os.OSAllocatedUnfairLock.Ownership
0x19e6b80c0  __TEXT,__text  getEnumTag value witness for os.OSAllocatedUnfairLock.Ownership
0x19e6b80c0  __TEXT,__text  getEnumTag value witness for os.OSAllocatedUnfairLock.Ownership
0x19e6b80c0  __TEXT,__text  getEnumTag value witness for os.OSAllocatedUnfairLock.Ownership
0x19e6b80c0  __TEXT,__text  getEnumTag value witness for os.OSAllocatedUnfairLock.Ownership
0x19e6b80d0  __TEXT,__text  ___swift_memcpy8_8
0x19e6b80dc  __TEXT,__text  ___swift_noop_void_return
0x19e6b8104  __TEXT,__text  ___swift_project_boxed_opaque_existential_1
0x19e6b8bd0  __TEXT,__text  _OUTLINED_FUNCTION_2
0x19e6b8bf0  __TEXT,__text  __os_log_encode
0x19e6b9aac  __TEXT,__text  _OUTLINED_FUNCTION_7
0x19e6b9abc  __TEXT,__text  _OUTLINED_FUNCTION_0
0x19e6b9adc  __TEXT,__text  _OUTLINED_FUNCTION_1
0x19e6b9ae8  __TEXT,__text  _OUTLINED_FUNCTION_8
0x19e6b9af8  __TEXT,__text  _OUTLINED_FUNCTION_6
0x19e6b9b0c  __TEXT,__text  _OUTLINED_FUNCTION_3
0x19e6b9b34  __TEXT,__text  _OUTLINED_FUNCTION_4
0x19e6b9b50  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSSignpostID
0x19e6ba014  __TEXT,__text  one-time initialization function for default
0x19e6ba03c  __TEXT,__text  __swift_os_log_default
0x19e6ba06c  __TEXT,__text  merged static (extension in os):__C.OS_os_log.default.getter : __C.OS_os_log
0x19e6ba0b4  __TEXT,__text  merged static os.OSSignpostID.exclusive.getter : os.OSSignpostID
0x19e6ba128  __TEXT,__text  merged getEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6ba128  __TEXT,__text  merged getEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6ba128  __TEXT,__text  merged getEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6ba16c  __TEXT,__text  merged storeEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6ba16c  __TEXT,__text  merged storeEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6ba16c  __TEXT,__text  merged storeEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6ba1a8  __TEXT,__text  one-time initialization function for disabled
0x19e6ba1d0  __TEXT,__text  __swift_os_log_disabled
0x19e6ba1dc  __TEXT,__text  one-time initialization function for invalid
0x19e6ba1ec  __TEXT,__text  one-time initialization function for null
0x19e6ba1f8  __TEXT,__text  one-time initialization function for exclusive
0x19e6ba490  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSSignpostID : Swift.Equatable in os
0x19e6ba4ec  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSSignpostID
0x19e6ba544  __TEXT,__text  merged static (extension in os):__C.OS_os_log.Category.pointsOfInterest.getter : (extension in os):__C.OS_os_log.Category
0x19e6ba5a8  __TEXT,__text  one-time initialization function for pointsOfInterest
0x19e6ba6f4  __TEXT,__text  ___swift_instantiateGenericMetadata
0x19e6ba724  __TEXT,__text  type metadata instantiation function for os.OSAllocatedUnfairLock
0x19e6ba760  __TEXT,__text  type metadata completion function for os.OSMetricCounter
0x19e6ba760  __TEXT,__text  type metadata completion function for os.OSMetricCounter
0x19e6ba760  __TEXT,__text  type metadata completion function for os.OSMetricCounter
0x19e6ba760  __TEXT,__text  type metadata completion function for os.OSMetricCounter
0x19e6ba760  __TEXT,__text  type metadata completion function for os.OSMetricCounter
0x19e6ba774  __TEXT,__text  merged static os.OSLogPrivacy.auto.getter : os.OSLogPrivacy
0x19e6ba7bc  __TEXT,__text  ___swift_memcpy2_1
0x19e6ba9b0  __TEXT,__text  outlined copy of (@escaping @callee_guaranteed () -> (@unowned Swift.Int))?
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa58  __TEXT,__text  getEnumTag value witness for os.AnimationFormatString
0x19e6baa60  __TEXT,__text  outlined consume of (@escaping @callee_guaranteed () -> (@unowned Swift.Int))?
0x19e6baa6c  __TEXT,__text  outlined destroy of os.OSLogIntegerFormatting
0x19e6baa9c  __TEXT,__text  _get_enum_tag_for_layout_string SiIegd_Sg
0x19e6baab0  __TEXT,__text  type metadata accessor for __C.os_unfair_lock_s
0x19e6baac4  __TEXT,__text  merged type metadata accessor for __C.os_unfair_lock_s
0x19e6bab10  __TEXT,__text  _OUTLINED_FUNCTION_16
0x19e6bab20  __TEXT,__text  _OUTLINED_FUNCTION_5
0x19e6bab34  __TEXT,__text  _OUTLINED_FUNCTION_9
0x19e6bab44  __TEXT,__text  os.OSSignpostIntervalState.encode(to: Swift.Encoder) throws -> ()
0x19e6bacb0  __TEXT,__text  protocol witness for Swift.Encodable.encode(to: Swift.Encoder) throws -> () in conformance os.OSSignpostIntervalState : Swift.Encodable in os
0x19e6bacd4  __TEXT,__text  lazy protocol witness table accessor for type os.OSSignpostIntervalState.CodingKeys and conformance os.OSSignpostIntervalState.CodingKeys : Swift.CodingKey in os
0x19e6bad28  __TEXT,__text  ___swift_memcpy1_1
0x19e6bad34  __TEXT,__text  protocol witness for Swift.CodingKey.stringValue.getter : Swift.String in conformance os.OSSignpostIntervalState.CodingKeys : Swift.CodingKey in os
0x19e6bad70  __TEXT,__text  ___swift_destroy_boxed_opaque_existential_0
0x19e6bad70  __TEXT,__text  ___swift_destroy_boxed_opaque_existential_0
0x19e6bada0  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSLogCollectionBound : Swift.Equatable in os
0x19e6bada0  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSLogCollectionBound : Swift.Equatable in os
0x19e6bada0  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSLogCollectionBound : Swift.Equatable in os
0x19e6bada0  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSLogCollectionBound : Swift.Equatable in os
0x19e6badb8  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSLogCollectionBound : Swift.Hashable in os
0x19e6badb8  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSLogCollectionBound : Swift.Hashable in os
0x19e6badb8  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSLogCollectionBound : Swift.Hashable in os
0x19e6badb8  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSLogCollectionBound : Swift.Hashable in os
0x19e6bae04  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSAllocatedUnfairLock.Ownership
0x19e6bae04  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSAllocatedUnfairLock.Ownership
0x19e6bae04  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSAllocatedUnfairLock.Ownership
0x19e6bae04  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSAllocatedUnfairLock.Ownership
0x19e6bae04  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSAllocatedUnfairLock.Ownership
0x19e6baf6c  __TEXT,__text  _OUTLINED_FUNCTION_10
0x19e6baf78  __TEXT,__text  _OUTLINED_FUNCTION_11
0x19e6baf8c  __TEXT,__text  _OUTLINED_FUNCTION_12
0x19e6bafa0  __TEXT,__text  _OUTLINED_FUNCTION_13
0x19e6bafac  __TEXT,__text  _OUTLINED_FUNCTION_14
0x19e6bafbc  __TEXT,__text  _OUTLINED_FUNCTION_15
0x19e6bafcc  __TEXT,__text  _OUTLINED_FUNCTION_17
0x19e6bafdc  __TEXT,__text  _OUTLINED_FUNCTION_18
0x19e6bafe8  __TEXT,__text  _OUTLINED_FUNCTION_19
0x19e6baff4  __TEXT,__text  _os_trace_blob_destroy_slow
0x19e6bb010  __TEXT,__text  _os_trace_blob_detach
0x19e6bb088  __TEXT,__text  _os_trace_blob_grow
0x19e6bb16c  __TEXT,__text  __os_trace_malloc
0x19e6bb1a8  __TEXT,__text  __os_trace_temporary_resource_shortage
0x19e6bb1b0  __TEXT,__text  __swift_os_log_reportError
0x19e6bb1b4  __TEXT,__text  ___swift_memcpy4_4
0x19e6bb1c0  __TEXT,__text  getEnumTagSinglePayload value witness for __C.os_unfair_lock_s
0x19e6bb1c0  __TEXT,__text  getEnumTagSinglePayload value witness for __C.os_unfair_lock_s
0x19e6bb1e0  __TEXT,__text  storeEnumTagSinglePayload value witness for __C.os_unfair_lock_s
0x19e6bb1e0  __TEXT,__text  storeEnumTagSinglePayload value witness for __C.os_unfair_lock_s
0x19e6bb208  __TEXT,__text  ___swift_memcpy40_4
0x19e6bb21c  __TEXT,__text  getEnumTagSinglePayload value witness for __C.os_workgroup_join_token_opaque_s
0x19e6bb21c  __TEXT,__text  getEnumTagSinglePayload value witness for __C.os_workgroup_join_token_opaque_s
0x19e6bb23c  __TEXT,__text  storeEnumTagSinglePayload value witness for __C.os_workgroup_join_token_opaque_s
0x19e6bb23c  __TEXT,__text  storeEnumTagSinglePayload value witness for __C.os_workgroup_join_token_opaque_s
0x19e6bb270  __TEXT,__text  type metadata accessor for __C.os_workgroup_join_token_opaque_s
0x19e6bb284  __TEXT,__text  closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.os_log(_: __C.os_log_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, _: Swift.StaticString, _: Swift.CVarArg...) -> ()
0x19e6bb55c  __TEXT,__text  closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.os_log(_: Swift.StaticString, dso: Swift.UnsafeRawPointer?, log: __C.OS_os_log, type: __C.os_log_type_t, _: Swift.CVarArg...) -> ()
0x19e6bb834  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.os_log(_: __C.os_log_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, _: Swift.StaticString, _: Swift.CVarArg...) -> ()
0x19e6bb9c8  __TEXT,__text  function signature specialization <Arg[1] = [Closure Propagated : $ss12StaticStringV14withUTF8BufferyxxSRys5UInt8VGXElFxAFXEfU_yt_TG5, Argument Types : [@callee_guaranteed @substituted <A where A: ~Swift.Copyable, A: ~Swift.Escapable> (@unowned Swift.UnsafeBufferPointer<Swift.UInt8>) -> (@out A) for
0x19e6bbaa8  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.os_log(_: Swift.StaticString, dso: Swift.UnsafeRawPointer?, log: __C.OS_os_log, type: __C.os_log_type_t, _: Swift.CVarArg...) -> ()
0x19e6bbac0  __TEXT,__text  merged partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.os_log(_: __C.os_log_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, _: Swift.StaticString, _: Swift.CVarArg...) -> ()
0x19e6bbae0  __TEXT,__text  one-time initialization function for empty
0x19e6bbb60  __TEXT,__text  os.OSMetricDimensions.bridged.getter : __C.OS_os_metric_dimensions?
0x19e6bbc60  __TEXT,__text  protocol witness for Swift.ExpressibleByDictionaryLiteral.init(dictionaryLiteral: (A.Key, A.Value)...) -> A in conformance os.OSMetricDimensions : Swift.ExpressibleByDictionaryLiteral in os
0x19e6bbcac  __TEXT,__text  os.OSMetricBinType.bridged.getter : (count: Swift.UInt8, interval: Swift.UInt32, intervals: [Swift.UInt64]?)
0x19e6bbd7c  __TEXT,__text  protocol witness for Swift.OptionSet.init(rawValue: A.RawValue) -> A in conformance os.OSMetricFlags : Swift.OptionSet in os
0x19e6bbd88  __TEXT,__text  protocol witness for Swift.SetAlgebra.init() -> A in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbd90  __TEXT,__text  protocol witness for Swift.SetAlgebra.union(__owned A) -> A in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbda4  __TEXT,__text  protocol witness for Swift.SetAlgebra.intersection(A) -> A in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbdb8  __TEXT,__text  protocol witness for Swift.SetAlgebra.symmetricDifference(__owned A) -> A in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbdcc  __TEXT,__text  protocol witness for Swift.SetAlgebra.insert(__owned A.Element) -> (inserted: Swift.Bool, memberAfterInsert: A.Element) in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbdec  __TEXT,__text  protocol witness for Swift.SetAlgebra.remove(A.Element) -> A.Element? in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbe1c  __TEXT,__text  protocol witness for Swift.SetAlgebra.update(with: __owned A.Element) -> A.Element? in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbe40  __TEXT,__text  protocol witness for Swift.SetAlgebra.formUnion(__owned A) -> () in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbe54  __TEXT,__text  protocol witness for Swift.SetAlgebra.formIntersection(A) -> () in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbe68  __TEXT,__text  protocol witness for Swift.SetAlgebra.formSymmetricDifference(__owned A) -> () in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbe7c  __TEXT,__text  protocol witness for Swift.SetAlgebra.subtracting(A) -> A in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbe90  __TEXT,__text  protocol witness for Swift.SetAlgebra.isSubset(of: A) -> Swift.Bool in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbea4  __TEXT,__text  protocol witness for Swift.SetAlgebra.isDisjoint(with: A) -> Swift.Bool in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbeb8  __TEXT,__text  protocol witness for Swift.SetAlgebra.isEmpty.getter : Swift.Bool in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbec8  __TEXT,__text  protocol witness for Swift.SetAlgebra.init<A where A1: Swift.Sequence, A.Element == A1.Element>(__owned A1) -> A in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbec8  __TEXT,__text  protocol witness for Swift.SetAlgebra.init<A where A1: Swift.Sequence, A.Element == A1.Element>(__owned A1) -> A in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbee0  __TEXT,__text  protocol witness for Swift.SetAlgebra.subtract(A) -> () in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bbef4  __TEXT,__text  protocol witness for Swift.RawRepresentable.init(rawValue: A.RawValue) -> A? in conformance os.OSMetricFlags : Swift.RawRepresentable in os
0x19e6bbf04  __TEXT,__text  protocol witness for Swift.RawRepresentable.rawValue.getter : A.RawValue in conformance os.OSMetricFlags : Swift.RawRepresentable in os
0x19e6bbf10  __TEXT,__text  protocol witness for Swift.ExpressibleByArrayLiteral.init(arrayLiteral: A.ArrayLiteralElement...) -> A in conformance os.OSMetricFlags : Swift.ExpressibleByArrayLiteral in os
0x19e6bbf28  __TEXT,__text  one-time initialization function for default
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc0ac  __TEXT,__text  os.OSMetricCounter.bridge.modify : os.OSMetricBridge<A> with unmangled suffix ".resume.0"
0x19e6bc170  __TEXT,__text  merged os.OSMetricCounter.init<A where A == Swift.Int64>(type: Swift.Int64.Type, group: os.OSMetricGroup, label: Swift.String, extraDimensions: os.OSMetricDimensions, flags: os.OSMetricFlags) -> os.OSMetricCounter<Swift.Int64>
0x19e6bc2f8  __TEXT,__text  merged os.OSMetricBridge.init<A where A == Swift.Int64>(group: os.OSMetricGroup, label: Swift.String, dimensions: os.OSMetricDimensions, type: os.OSMetricType, level: os.OSMetricStatisticalLevel, bins: Swift.UInt8, interval: Swift.UInt32, flags: Swift.UInt8) -> os.OSMetricBridge<Swift.Int64>
0x19e6bc5d0  __TEXT,__text  merged os.OSMetricGauge.init<A where A == Swift.Int64>(type: Swift.Int64.Type, group: os.OSMetricGroup, label: Swift.String, extraDimensions: os.OSMetricDimensions, level: os.OSMetricStatisticalLevel, flags: os.OSMetricFlags) -> os.OSMetricGauge<Swift.Int64>
0x19e6bc7b4  __TEXT,__text  outlined consume of os.OSMetricBinType
0x19e6bc834  __TEXT,__text  merged os.OSMetricHistogram.init<A where A == Swift.Int64>(type: Swift.Int64.Type, group: os.OSMetricGroup, label: Swift.String, extraDimensions: os.OSMetricDimensions, level: os.OSMetricStatisticalLevel, bins: os.OSMetricBinType, flags: os.OSMetricFlags) -> os.OSMetricHistogram<Swift.Int64>
0x19e6bcafc  __TEXT,__text  merged os.OSMetricBridge.init<A where A == Swift.Int64>(group: os.OSMetricGroup, label: Swift.String, dimensions: os.OSMetricDimensions, type: os.OSMetricType, level: os.OSMetricStatisticalLevel, bins: Swift.UInt8, intervals: [Swift.UInt64], flags: Swift.UInt8) -> os.OSMetricBridge<Swift.Int64>
0x19e6bcc78  __TEXT,__text  merged os.OSMetricCounter.setScale(to: os.OSMetricScale) -> ()
0x19e6bcca4  __TEXT,__text  merged os.OSMetricStatisticalLevel.hashValue.getter : Swift.Int
0x19e6bcca4  __TEXT,__text  merged os.OSMetricStatisticalLevel.hashValue.getter : Swift.Int
0x19e6bcca4  __TEXT,__text  merged os.OSMetricStatisticalLevel.hashValue.getter : Swift.Int
0x19e6bcca4  __TEXT,__text  merged os.OSMetricStatisticalLevel.hashValue.getter : Swift.Int
0x19e6bcca4  __TEXT,__text  merged os.OSMetricStatisticalLevel.hashValue.getter : Swift.Int
0x19e6bcca4  __TEXT,__text  merged os.OSMetricStatisticalLevel.hashValue.getter : Swift.Int
0x19e6bcca4  __TEXT,__text  merged os.OSMetricStatisticalLevel.hashValue.getter : Swift.Int
0x19e6bcca4  __TEXT,__text  merged os.OSMetricStatisticalLevel.hashValue.getter : Swift.Int
0x19e6bcca4  __TEXT,__text  merged os.OSMetricStatisticalLevel.hashValue.getter : Swift.Int
0x19e6bcca4  __TEXT,__text  merged os.OSMetricStatisticalLevel.hashValue.getter : Swift.Int
0x19e6bcca4  __TEXT,__text  merged os.OSMetricStatisticalLevel.hashValue.getter : Swift.Int
0x19e6bccec  __TEXT,__text  merged protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bccec  __TEXT,__text  merged protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bccec  __TEXT,__text  merged protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bccec  __TEXT,__text  merged protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bccec  __TEXT,__text  merged protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bccec  __TEXT,__text  merged protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bccec  __TEXT,__text  merged protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bccec  __TEXT,__text  merged protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bcd30  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bcd34  __TEXT,__text  lazy protocol witness table accessor for type os.OSMetricStatisticalLevel and conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bcd88  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSMetricType : Swift.Hashable in os
0x19e6bcd8c  __TEXT,__text  lazy protocol witness table accessor for type os.OSMetricType and conformance os.OSMetricType : Swift.Equatable in os
0x19e6bcde0  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSMetricUnit : Swift.Hashable in os
0x19e6bcde4  __TEXT,__text  lazy protocol witness table accessor for type os.OSMetricUnit and conformance os.OSMetricUnit : Swift.Equatable in os
0x19e6bce38  __TEXT,__text  base witness table accessor for Swift.RawRepresentable in os.OSMetricFlags : Swift.OptionSet in os
0x19e6bce3c  __TEXT,__text  lazy protocol witness table accessor for type os.OSMetricFlags and conformance os.OSMetricFlags : Swift.RawRepresentable in os
0x19e6bce90  __TEXT,__text  base witness table accessor for Swift.SetAlgebra in os.OSMetricFlags : Swift.OptionSet in os
0x19e6bce94  __TEXT,__text  lazy protocol witness table accessor for type os.OSMetricFlags and conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bcee8  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bceec  __TEXT,__text  lazy protocol witness table accessor for type os.OSMetricFlags and conformance os.OSMetricFlags : Swift.Equatable in os
0x19e6bcf40  __TEXT,__text  base witness table accessor for Swift.ExpressibleByArrayLiteral in os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bcf44  __TEXT,__text  lazy protocol witness table accessor for type os.OSMetricFlags and conformance os.OSMetricFlags : Swift.ExpressibleByArrayLiteral in os
0x19e6bcf98  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSMetricOperation : Swift.Hashable in os
0x19e6bcf9c  __TEXT,__text  lazy protocol witness table accessor for type os.OSMetricOperation and conformance os.OSMetricOperation : Swift.Equatable in os
0x19e6bd020  __TEXT,__text  merged getEnumTagSinglePayload value witness for os.OSMetricStatisticalLevel
0x19e6bd0b0  __TEXT,__text  merged storeEnumTagSinglePayload value witness for os.OSMetricStatisticalLevel
0x19e6bd170  __TEXT,__text  _get_enum_tag_for_layout_string 2os15OSMetricBinTypeO
0x19e6bd17c  __TEXT,__text  ___swift_memcpy9_8
0x19e6bd190  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricBinType
0x19e6bd1d8  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricBinType
0x19e6bd21c  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricBinType
0x19e6bd234  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricFlags
0x19e6bd2a0  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricFlags
0x19e6bd348  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricScale
0x19e6bd3c8  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricScale
0x19e6bd464  __TEXT,__text  getEnumTag value witness for os.OSMetricScale
0x19e6bd484  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricScale
0x19e6bd4b8  __TEXT,__text  ___swift_memcpy40_8
0x19e6bd4cc  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricGroup
0x19e6bd510  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricGroup
0x19e6bd5b0  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricOperation
0x19e6bd5b0  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricOperation
0x19e6bd5b0  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricOperation
0x19e6bd640  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricOperation
0x19e6bd640  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricOperation
0x19e6bd640  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricOperation
0x19e6bd700  __TEXT,__text  type metadata instantiation function for os.OSMetricBridge
0x19e6bd73c  __TEXT,__text  outlined copy of os.OSMetricBinType
0x19e6bd758  __TEXT,__text  type metadata instantiation function for os.OSMetricCounter
0x19e6bd758  __TEXT,__text  type metadata instantiation function for os.OSMetricCounter
0x19e6bd758  __TEXT,__text  type metadata instantiation function for os.OSMetricCounter
0x19e6bd760  __TEXT,__text  protocol witness for Swift.SetAlgebra.contains(A.Element) -> Swift.Bool in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bd760  __TEXT,__text  protocol witness for Swift.SetAlgebra.contains(A.Element) -> Swift.Bool in conformance os.OSMetricFlags : Swift.SetAlgebra in os
0x19e6bd764  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bd764  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bd764  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bd764  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bd764  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bd764  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bd764  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bd764  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bd764  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bd764  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bd764  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bd764  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bd764  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSMetricStatisticalLevel : Swift.Equatable in os
0x19e6bd768  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd768  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd768  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd768  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd768  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd768  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd768  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd768  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd768  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd768  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd768  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd768  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd76c  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricStatisticalLevel
0x19e6bd76c  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricStatisticalLevel
0x19e6bd76c  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricStatisticalLevel
0x19e6bd770  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6bd770  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6bd770  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6bd770  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6bd770  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6bd774  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6bd774  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6bd774  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6bd774  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6bd774  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6bd774  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6bd774  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6bd774  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6bd774  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6bd774  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6bd774  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6bd774  __TEXT,__text  destructiveInjectEnumTag value witness for os.OSMetricStatisticalLevel
0x19e6bd78c  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd78c  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd78c  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd78c  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd78c  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd78c  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd78c  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd78c  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd78c  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd78c  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd78c  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd78c  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd798  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd798  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd798  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd798  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd798  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd798  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd798  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd798  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd798  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd798  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd798  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd798  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSMetricStatisticalLevel : Swift.Hashable in os
0x19e6bd7a4  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricStatisticalLevel
0x19e6bd7a4  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricStatisticalLevel
0x19e6bd7a4  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricStatisticalLevel
0x19e6bd7a8  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6bd7a8  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6bd7a8  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6bd7a8  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6bd7a8  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSMetricDimensions
0x19e6bd7c4  __TEXT,__text  closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.os_signpost(_: __C.os_signpost_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name: Swift.StaticString, signpostID: os.OSSignpostID) -> ()
0x19e6bd840  __TEXT,__text  closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.os_signpost(_: __C.os_signpost_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name: Swift.StaticString, signpostID: os.OSSignpostID, _: Swift.StaticString, _: Swift.CVarArg...) -> ()
0x19e6bdc8c  __TEXT,__text  closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in closure #1 (Swift.UnsafePointer<Swift.Int8>) -> () in closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.os_signpost(_: __C.os_signpost_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name: Swift.StaticString, signpos
0x19e6be08c  __TEXT,__text  merged protocol witness for Swift.ExpressibleByStringLiteral.init(stringLiteral: A.StringLiteralType) -> A in conformance os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByStringLiteral in os
0x19e6be150  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSSignpostAnimationBegin : Swift.Equatable in os
0x19e6be150  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSSignpostAnimationBegin : Swift.Equatable in os
0x19e6be158  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSSignpostAnimationBegin : Swift.Hashable in os
0x19e6be19c  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSSignpostAnimationBegin : Swift.Hashable in os
0x19e6be1c4  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSSignpostAnimationBegin : Swift.Hashable in os
0x19e6be6a0  __TEXT,__text  closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.animationBeginSignpostHelper(dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name: Swift.StaticString, signpostID: os.OSSignpostID, formatStringPointer: Swift.UnsafePointer<Swift.Int8>, arguments: [Swift.CVarArg]) -> ()
0x19e6bea1c  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.os_signpost(_: __C.os_signpost_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name: Swift.StaticString, signpostID: os.OSSignpostID) -> ()
0x19e6bea30  __TEXT,__text  protocol witness for static Swift.Comparable.< infix(A, A) -> Swift.Bool in conformance os.OSSignpostID : Swift.Comparable in os
0x19e6bea44  __TEXT,__text  protocol witness for static Swift.Comparable.<= infix(A, A) -> Swift.Bool in conformance os.OSSignpostID : Swift.Comparable in os
0x19e6bea58  __TEXT,__text  protocol witness for static Swift.Comparable.>= infix(A, A) -> Swift.Bool in conformance os.OSSignpostID : Swift.Comparable in os
0x19e6bea6c  __TEXT,__text  protocol witness for static Swift.Comparable.> infix(A, A) -> Swift.Bool in conformance os.OSSignpostID : Swift.Comparable in os
0x19e6beb20  __TEXT,__text  one-time initialization function for dynamicTracing
0x19e6beb74  __TEXT,__text  one-time initialization function for dynamicStackTracing
0x19e6bebc8  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.os_signpost(_: __C.os_signpost_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name: Swift.StaticString, signpostID: os.OSSignpostID, _: Swift.StaticString, _: Swift.CVarArg...) -> ()
0x19e6bec0c  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in closure #1 (Swift.UnsafePointer<Swift.Int8>) -> () in closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.os_signpost(_: __C.os_signpost_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name:
0x19e6bec10  __TEXT,__text  outlined init with copy of os.OSLogInterpolation
0x19e6bec64  __TEXT,__text  outlined destroy of os.OSLogInterpolation
0x19e6becb0  __TEXT,__text  outlined destroy of os.OSLogMessage
0x19e6becfc  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.animationBeginSignpostHelper(dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name: Swift.StaticString, signpostID: os.OSSignpostID, formatStringPointer: Swift.UnsafePointer<Swift.Int8>, arguments: [Swift.CVa
0x19e6bed0c  __TEXT,__text  base witness table accessor for Swift.ExpressibleByExtendedGraphemeClusterLiteral in os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByStringLiteral in os
0x19e6bed10  __TEXT,__text  lazy protocol witness table accessor for type os.AnimationFormatString.OSLogMessage and conformance os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6bed64  __TEXT,__text  associated type witness table accessor for Swift.ExpressibleByStringLiteral.StringLiteralType : Swift._ExpressibleByBuiltinStringLiteral in os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByStringLiteral in os
0x19e6bed64  __TEXT,__text  associated type witness table accessor for Swift.ExpressibleByStringLiteral.StringLiteralType : Swift._ExpressibleByBuiltinStringLiteral in os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByStringLiteral in os
0x19e6bed64  __TEXT,__text  associated type witness table accessor for Swift.ExpressibleByStringLiteral.StringLiteralType : Swift._ExpressibleByBuiltinStringLiteral in os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByStringLiteral in os
0x19e6bed70  __TEXT,__text  base witness table accessor for Swift.ExpressibleByUnicodeScalarLiteral in os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6bed74  __TEXT,__text  lazy protocol witness table accessor for type os.AnimationFormatString.OSLogMessage and conformance os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByUnicodeScalarLiteral in os
0x19e6bedc8  __TEXT,__text  associated type witness table accessor for Swift.ExpressibleByExtendedGraphemeClusterLiteral.ExtendedGraphemeClusterLiteralType : Swift._ExpressibleByBuiltinExtendedGraphemeClusterLiteral in os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6bedc8  __TEXT,__text  associated type witness table accessor for Swift.ExpressibleByExtendedGraphemeClusterLiteral.ExtendedGraphemeClusterLiteralType : Swift._ExpressibleByBuiltinExtendedGraphemeClusterLiteral in os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6bedd4  __TEXT,__text  associated type witness table accessor for Swift.ExpressibleByUnicodeScalarLiteral.UnicodeScalarLiteralType : Swift._ExpressibleByBuiltinUnicodeScalarLiteral in os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByUnicodeScalarLiteral in os
0x19e6bedd4  __TEXT,__text  associated type witness table accessor for Swift.ExpressibleByUnicodeScalarLiteral.UnicodeScalarLiteralType : Swift._ExpressibleByBuiltinUnicodeScalarLiteral in os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByUnicodeScalarLiteral in os
0x19e6bede0  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSSignpostAnimationBegin : Swift.Hashable in os
0x19e6bede4  __TEXT,__text  lazy protocol witness table accessor for type os.OSSignpostAnimationBegin and conformance os.OSSignpostAnimationBegin : Swift.Equatable in os
0x19e6bee38  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSSignpostID : Swift.Comparable in os
0x19e6bee3c  __TEXT,__text  lazy protocol witness table accessor for type os.OSSignpostID and conformance os.OSSignpostID : Swift.Equatable in os
0x19e6bee90  __TEXT,__text  ___swift_memcpy0_1
0x19e6beea4  __TEXT,__text  getEnumTagSinglePayload value witness for os.AnimationFormatString.OSLogMessage
0x19e6beee8  __TEXT,__text  storeEnumTagSinglePayload value witness for os.AnimationFormatString.OSLogMessage
0x19e6bef34  __TEXT,__text  merged getEnumTagSinglePayload value witness for os.AnimationFormatString
0x19e6bef84  __TEXT,__text  merged storeEnumTagSinglePayload value witness for os.AnimationFormatString
0x19e6bf010  __TEXT,__text  ___swift_memcpy16_8
0x19e6bf01c  __TEXT,__text  getEnumTagSinglePayload value witness for (extension in os):__C.OS_os_log.Category
0x19e6bf060  __TEXT,__text  storeEnumTagSinglePayload value witness for (extension in os):__C.OS_os_log.Category
0x19e6bf0ac  __TEXT,__text  merged partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in closure #1 (Swift.UnsafePointer<Swift.Int8>) -> () in closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.os_signpost(_: __C.os_signpost_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log
0x19e6bf0e0  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSSignpostAnimationBegin
0x19e6bf0e0  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSSignpostAnimationBegin
0x19e6bf0e4  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in closure #1 (Swift.UnsafePointer<Swift.Int8>) -> () in closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> () in os.os_signpost(_: __C.os_signpost_type_t, dso: Swift.UnsafeRawPointer, log: __C.OS_os_log, name:
0x19e6bf0e8  __TEXT,__text  protocol witness for Swift.ExpressibleByExtendedGraphemeClusterLiteral.init(extendedGraphemeClusterLiteral: A.ExtendedGraphemeClusterLiteralType) -> A in conformance os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6bf0e8  __TEXT,__text  protocol witness for Swift.ExpressibleByExtendedGraphemeClusterLiteral.init(extendedGraphemeClusterLiteral: A.ExtendedGraphemeClusterLiteralType) -> A in conformance os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6bf0e8  __TEXT,__text  protocol witness for Swift.ExpressibleByExtendedGraphemeClusterLiteral.init(extendedGraphemeClusterLiteral: A.ExtendedGraphemeClusterLiteralType) -> A in conformance os.AnimationFormatString.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6bf0ec  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSSignpostAnimationBegin
0x19e6bf0ec  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSSignpostAnimationBegin
0x19e6bf150  __TEXT,__text  key path getter for os.OSLogFloatFormatting.precision : (() -> Swift.Int)? : os.OSLogFloatFormatting
0x19e6bf1c4  __TEXT,__text  key path setter for os.OSLogFloatFormatting.precision : (() -> Swift.Int)? : os.OSLogFloatFormatting
0x19e6bf414  __TEXT,__text  outlined init with copy of os.OSLogFloatFormatting
0x19e6bf44c  __TEXT,__text  outlined destroy of os.OSLogFloatFormatting
0x19e6bf4cc  __TEXT,__text  merged static os.OSLogFloatFormatting.fixed.getter : os.OSLogFloatFormatting
0x19e6bf5e8  __TEXT,__text  merged static os.OSLogFloatFormatting.fixed(explicitPositiveSign: Swift.Bool, uppercase: Swift.Bool) -> os.OSLogFloatFormatting
0x19e6bf68c  __TEXT,__text  merged static os.OSLogFloatFormatting.fixed(precision: @autoclosure () -> Swift.Int, explicitPositiveSign: Swift.Bool, uppercase: Swift.Bool) -> os.OSLogFloatFormatting
0x19e6bf7d4  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSLogFloatFormatting.Notation : Swift.Hashable in os
0x19e6bf7d8  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogFloatFormatting.Notation and conformance os.OSLogFloatFormatting.Notation : Swift.Equatable in os
0x19e6bf82c  __TEXT,__text  ___swift_memcpy25_8
0x19e6bf840  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogFloatFormatting
0x19e6bf898  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogFloatFormatting
0x19e6bf910  __TEXT,__text  ___swift_closure_destructor
0x19e6bf93c  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@out Swift.Int) to @escaping @callee_guaranteed () -> (@unowned Swift.Int)
0x19e6bf944  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.Int) to @escaping @callee_guaranteed () -> (@out Swift.Int)
0x19e6bf94c  __TEXT,__text  os.OSLogFloatFormatting.formatSpecifier<A where A: Swift.FloatingPoint>(for: A.Type, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy, attributes: Swift.String) -> Swift.String
0x19e6bfe94  __TEXT,__text  outlined destroy of Swift.String
0x19e6bfee0  __TEXT,__text  ___swift_closure_destructor.7
0x19e6bff80  __TEXT,__text  ___swift_closure_destructor
0x19e6bffac  __TEXT,__text  partial apply forwarder for implicit closure #1 () -> Swift.Double in os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Float, format: os.OSLogFloatFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c00a0  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Double, format: os.OSLogFloatFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy, attributes: Swift.String) -> ()
0x19e6c024c  __TEXT,__text  partial apply forwarder for implicit closure #1 () -> Swift.Double in os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Double, format: os.OSLogFloatFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c0430  __TEXT,__text  partial apply forwarder for closure #1 (inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> () in os.OSLogArguments.append(() -> Swift.Double) -> ()
0x19e6c0488  __TEXT,__text  ___swift_instantiateConcreteTypeFromMangledNameV2
0x19e6c04dc  __TEXT,__text  lazy protocol witness table accessor for type Swift.Double and conformance Swift.Double : Swift.FloatingPoint in Swift
0x19e6c0530  __TEXT,__text  ___swift_closure_destructor.2
0x19e6c0534  __TEXT,__text  ___swift_closure_destructor.5
0x19e6c05f4  __TEXT,__text  key path getter for os.OSLogIntegerFormatting.minDigits : (() -> Swift.Int)? : os.OSLogIntegerFormatting
0x19e6c0668  __TEXT,__text  key path setter for os.OSLogIntegerFormatting.minDigits : (() -> Swift.Int)? : os.OSLogIntegerFormatting
0x19e6c0914  __TEXT,__text  merged static os.OSLogIntegerFormatting.hex(explicitPositiveSign: Swift.Bool, includePrefix: Swift.Bool, uppercase: Swift.Bool, minDigits: @autoclosure () -> Swift.Int) -> os.OSLogIntegerFormatting
0x19e6c0a04  __TEXT,__text  merged static os.OSLogIntegerFormatting.hex(explicitPositiveSign: Swift.Bool, includePrefix: Swift.Bool, uppercase: Swift.Bool) -> os.OSLogIntegerFormatting
0x19e6c0b14  __TEXT,__text  merged static os.OSLogIntegerFormatting.hex.getter : os.OSLogIntegerFormatting
0x19e6c0ec4  __TEXT,__text  ___swift_memcpy32_8
0x19e6c0ed0  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogIntegerFormatting
0x19e6c0f28  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogIntegerFormatting
0x19e6c0f8c  __TEXT,__text  ___swift_closure_destructor
0x19e6c0fb8  __TEXT,__text  os.OSLogIntegerFormatting.formatSpecifier<A where A: Swift.FixedWidthInteger>(for: A.Type, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy, attributes: Swift.String) -> Swift.String
0x19e6c1630  __TEXT,__text  ___swift_closure_destructor.4
0x19e6c1634  __TEXT,__text  reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.Int) to @escaping @callee_guaranteed () -> (@out Swift.Int)
0x19e6c18d0  __TEXT,__text  merged os.OSLogInterpolation.appendAlignmentArgument(() -> Swift.Int) -> ()
0x19e6c1a14  __TEXT,__text  Swift._withUnprotectedUnsafeBytes<A, B, C where B: Swift.Error, A: ~Swift.Copyable, C: ~Swift.Copyable>(of: A, _: (Swift.UnsafeRawBufferPointer) throws(B) -> C) throws(B) -> C
0x19e6c1ba8  __TEXT,__text  default argument 4 of os.OSLogInterpolation.appendInteger<A where A: Swift.FixedWidthInteger>(_: () -> A, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy, attributes: Swift.String) -> ()
0x19e6c1bd0  __TEXT,__text  os.OSLogInterpolation.appendInteger<A where A: Swift.FixedWidthInteger>(_: () -> A, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy, attributes: Swift.String) -> ()
0x19e6c1f24  __TEXT,__text  reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.Int32) to @escaping @callee_guaranteed () -> (@out Swift.Int32)
0x19e6c2194  __TEXT,__text  merged os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Int, format: os.OSLogIntegerFormatting, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c2640  __TEXT,__text  closure #1 () -> Swift.Int32 in os.OSLogInterpolation.appendPrecisionAlignCount(() -> Swift.Int, Swift.UInt8) -> ()
0x19e6c2714  __TEXT,__text  ___swift_closure_destructor
0x19e6c2740  __TEXT,__text  partial apply forwarder for closure #1 () -> Swift.Int32 in os.OSLogInterpolation.appendPrecisionAlignCount(() -> Swift.Int, Swift.UInt8) -> ()
0x19e6c2748  __TEXT,__text  lazy protocol witness table accessor for type Swift.Int32 and conformance Swift.Int32 : Swift.FixedWidthInteger in Swift
0x19e6c279c  __TEXT,__text  ___swift_closure_destructor.2
0x19e6c27ac  __TEXT,__text  partial apply forwarder for closure #1 () -> Swift.UInt64 in os.OSLogInterpolation.appendMaskArgument(os.OSLogPrivacy) -> ()
0x19e6c27b8  __TEXT,__text  lazy protocol witness table accessor for type Swift.UInt64 and conformance Swift.UInt64 : Swift.FixedWidthInteger in Swift
0x19e6c280c  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.Int) to @escaping @callee_guaranteed () -> (@out Swift.Int)
0x19e6c283c  __TEXT,__text  lazy protocol witness table accessor for type Swift.Int and conformance Swift.Int : Swift.FixedWidthInteger in Swift
0x19e6c2890  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.Int8) to @escaping @callee_guaranteed () -> (@out Swift.Int8)
0x19e6c28c0  __TEXT,__text  lazy protocol witness table accessor for type Swift.Int8 and conformance Swift.Int8 : Swift.FixedWidthInteger in Swift
0x19e6c2914  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.Int16) to @escaping @callee_guaranteed () -> (@out Swift.Int16)
0x19e6c2944  __TEXT,__text  lazy protocol witness table accessor for type Swift.Int16 and conformance Swift.Int16 : Swift.FixedWidthInteger in Swift
0x19e6c2998  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.Int32) to @escaping @callee_guaranteed () -> (@out Swift.Int32)
0x19e6c29c8  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.Int64) to @escaping @callee_guaranteed () -> (@out Swift.Int64)
0x19e6c29f8  __TEXT,__text  lazy protocol witness table accessor for type Swift.Int64 and conformance Swift.Int64 : Swift.FixedWidthInteger in Swift
0x19e6c2a4c  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.UInt) to @escaping @callee_guaranteed () -> (@out Swift.UInt)
0x19e6c2a7c  __TEXT,__text  lazy protocol witness table accessor for type Swift.UInt and conformance Swift.UInt : Swift.FixedWidthInteger in Swift
0x19e6c2ad0  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.UInt8) to @escaping @callee_guaranteed () -> (@out Swift.UInt8)
0x19e6c2b00  __TEXT,__text  lazy protocol witness table accessor for type Swift.UInt8 and conformance Swift.UInt8 : Swift.FixedWidthInteger in Swift
0x19e6c2b54  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.UInt16) to @escaping @callee_guaranteed () -> (@out Swift.UInt16)
0x19e6c2b84  __TEXT,__text  lazy protocol witness table accessor for type Swift.UInt16 and conformance Swift.UInt16 : Swift.FixedWidthInteger in Swift
0x19e6c2bd8  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.UInt32) to @escaping @callee_guaranteed () -> (@out Swift.UInt32)
0x19e6c2c08  __TEXT,__text  lazy protocol witness table accessor for type Swift.UInt32 and conformance Swift.UInt32 : Swift.FixedWidthInteger in Swift
0x19e6c2c5c  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.UInt64) to @escaping @callee_guaranteed () -> (@out Swift.UInt64)
0x19e6c2c8c  __TEXT,__text  closure #1 (inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> () in os.OSLogArguments.append<A where A: Swift.FixedWidthInteger>(() -> A) -> ()
0x19e6c2e08  __TEXT,__text  ___swift_closure_destructor.39
0x19e6c2e34  __TEXT,__text  partial apply forwarder for closure #1 (inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> () in os.OSLogArguments.append<A where A: Swift.FixedWidthInteger>(() -> A) -> ()
0x19e6c2e40  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeRawBufferPointer) -> () in os.serialize<A where A: Swift.FixedWidthInteger>(_: A, at: inout Swift.UnsafeMutablePointer<Swift.UInt8>) -> ()
0x19e6c2e6c  __TEXT,__text  ___swift_closure_destructor.5
0x19e6c2e70  __TEXT,__text  ___swift_closure_destructor.9
0x19e6c2e74  __TEXT,__text  ___swift_closure_destructor.12
0x19e6c2e78  __TEXT,__text  ___swift_closure_destructor.15
0x19e6c2e7c  __TEXT,__text  ___swift_closure_destructor.18
0x19e6c2e80  __TEXT,__text  ___swift_closure_destructor.21
0x19e6c2e84  __TEXT,__text  ___swift_closure_destructor.24
0x19e6c2e88  __TEXT,__text  ___swift_closure_destructor.27
0x19e6c2e8c  __TEXT,__text  ___swift_closure_destructor.30
0x19e6c2e90  __TEXT,__text  ___swift_closure_destructor.33
0x19e6c2e94  __TEXT,__text  ___swift_closure_destructor.36
0x19e6c2e98  __TEXT,__text  ___swift_closure_destructor.42
0x19e6c2e9c  __TEXT,__text  partial apply forwarder for closure #1 () -> Swift.Int32 in os.OSLogInterpolation.appendPrecisionAlignCount(() -> Swift.Int, Swift.UInt8) -> () with unmangled suffix ".7"
0x19e6c2e9c  __TEXT,__text  partial apply forwarder for closure #1 () -> Swift.Int32 in os.OSLogInterpolation.appendPrecisionAlignCount(() -> Swift.Int, Swift.UInt8) -> () with unmangled suffix ".7"
0x19e6c2f90  __TEXT,__text  os.concatPrivacyAndAttributes(privacy: os.OSLogPrivacy, attributes: Swift.String) -> Swift.String?
0x19e6c36dc  __TEXT,__text  protocol witness for Swift.StringInterpolationProtocol.init(literalCapacity: Swift.Int, interpolationCount: Swift.Int) -> A in conformance os.OSLogInterpolation : Swift.StringInterpolationProtocol in os
0x19e6c3728  __TEXT,__text  protocol witness for Swift.StringInterpolationProtocol.appendLiteral(A.StringLiteralType) -> () in conformance os.OSLogInterpolation : Swift.StringInterpolationProtocol in os
0x19e6c3734  __TEXT,__text  default argument 1 of (extension in Swift):Swift.Collection< where A.Element: Swift.Equatable>.split(separator: A.Element, maxSplits: Swift.Int, omittingEmptySubsequences: Swift.Bool) -> [A.SubSequence]
0x19e6c389c  __TEXT,__text  protocol witness for Swift.ExpressibleByStringInterpolation.init(stringInterpolation: A.StringInterpolation) -> A in conformance os.OSLogMessage : Swift.ExpressibleByStringInterpolation in os
0x19e6c3954  __TEXT,__text  ___swift_closure_destructor
0x19e6c3964  __TEXT,__text  partial apply forwarder for closure #1 (inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> () in os.OSLogArguments.append(Swift.UInt8) -> ()
0x19e6c3978  __TEXT,__text  lazy protocol witness table accessor for type Swift.String and conformance Swift.String : Swift.Collection in Swift
0x19e6c39cc  __TEXT,__text  outlined destroy of Swift.Character
0x19e6c3a18  __TEXT,__text  lazy protocol witness table accessor for type [Swift.Substring] and conformance [A] : Swift.Sequence in Swift
0x19e6c3a7c  __TEXT,__text  ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
0x19e6c3ad8  __TEXT,__text  lazy protocol witness table accessor for type Swift.Substring and conformance Swift.Substring : Swift.StringProtocol in Swift
0x19e6c3b2c  __TEXT,__text  outlined destroy of [Swift.Substring]
0x19e6c3b8c  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSLogInterpolation.ArgumentType : Swift.Hashable in os
0x19e6c3b90  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogInterpolation.ArgumentType and conformance os.OSLogInterpolation.ArgumentType : Swift.Equatable in os
0x19e6c3be4  __TEXT,__text  base witness table accessor for Swift.ExpressibleByStringLiteral in os.OSLogMessage : Swift.ExpressibleByStringInterpolation in os
0x19e6c3be8  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogMessage and conformance os.OSLogMessage : Swift.ExpressibleByStringLiteral in os
0x19e6c3c3c  __TEXT,__text  associated type witness table accessor for Swift.ExpressibleByStringInterpolation.StringInterpolation : Swift.StringInterpolationProtocol in os.OSLogMessage : Swift.ExpressibleByStringInterpolation in os
0x19e6c3c40  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogInterpolation and conformance os.OSLogInterpolation : Swift.StringInterpolationProtocol in os
0x19e6c3c94  __TEXT,__text  base witness table accessor for Swift.ExpressibleByExtendedGraphemeClusterLiteral in os.OSLogMessage : Swift.ExpressibleByStringLiteral in os
0x19e6c3c98  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogMessage and conformance os.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6c3cec  __TEXT,__text  base witness table accessor for Swift.ExpressibleByUnicodeScalarLiteral in os.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6c3cf0  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogMessage and conformance os.OSLogMessage : Swift.ExpressibleByUnicodeScalarLiteral in os
0x19e6c3d44  __TEXT,__text  ___swift_memcpy56_8
0x19e6c3d70  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogInterpolation.ArgumentType
0x19e6c3d70  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogInterpolation.ArgumentType
0x19e6c3e00  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogInterpolation.ArgumentType
0x19e6c3e00  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogInterpolation.ArgumentType
0x19e6c3ec0  __TEXT,__text  merged getEnumTagSinglePayload value witness for os.OSLogInterpolation
0x19e6c3f04  __TEXT,__text  merged storeEnumTagSinglePayload value witness for os.OSLogInterpolation
0x19e6c3f70  __TEXT,__text  os.serialize(_: Swift.UInt8, at: inout Swift.UnsafeMutablePointer<Swift.UInt8>) -> ()
0x19e6c3f80  __TEXT,__text  os.createStorage<A>(capacity: Swift.Int, type: A.Type) -> Swift.UnsafeMutablePointer<A>?
0x19e6c3fa4  __TEXT,__text  os.destroyStorage<A>(_: Swift.UnsafeMutablePointer<A>?, count: Swift.Int) -> ()
0x19e6c3fe8  __TEXT,__text  protocol witness for Swift.ExpressibleByExtendedGraphemeClusterLiteral.init(extendedGraphemeClusterLiteral: A.ExtendedGraphemeClusterLiteralType) -> A in conformance os.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6c3fe8  __TEXT,__text  protocol witness for Swift.ExpressibleByExtendedGraphemeClusterLiteral.init(extendedGraphemeClusterLiteral: A.ExtendedGraphemeClusterLiteralType) -> A in conformance os.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6c3fe8  __TEXT,__text  protocol witness for Swift.ExpressibleByExtendedGraphemeClusterLiteral.init(extendedGraphemeClusterLiteral: A.ExtendedGraphemeClusterLiteralType) -> A in conformance os.OSLogMessage : Swift.ExpressibleByExtendedGraphemeClusterLiteral in os
0x19e6c3fec  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogInterpolation
0x19e6c3fec  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogInterpolation
0x19e6c3ff0  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogInterpolation
0x19e6c3ff0  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogInterpolation
0x19e6c3ff4  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> __C.NSObject?, privacy: os.OSLogPrivacy, attributes: Swift.String) -> ()
0x19e6c4208  __TEXT,__text  ___swift_closure_destructor
0x19e6c4234  __TEXT,__text  partial apply forwarder for implicit closure #1 () -> __C.NSObject? in os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> __C.NSObject, privacy: os.OSLogPrivacy) -> ()
0x19e6c425c  __TEXT,__text  os.OSLogInterpolation.getNSObjectFormatSpecifier(os.OSLogPrivacy, Swift.String) -> Swift.String
0x19e6c4570  __TEXT,__text  closure #1 (inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> () in os.OSLogArguments.append(() -> __C.NSObject?) -> ()
0x19e6c4628  __TEXT,__text  partial apply forwarder for closure #1 (inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> () in os.OSLogArguments.append(() -> __C.NSObject?) -> ()
0x19e6c4630  __TEXT,__text  ___swift_closure_destructor.2
0x19e6c47c0  __TEXT,__text  implicit closure #1 () -> Swift.UnsafeRawPointer in os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.UnsafeRawBufferPointer, format: os.OSLogPointerFormat, privacy: os.OSLogPrivacy) -> ()
0x19e6c483c  __TEXT,__text  ___swift_closure_destructor
0x19e6c4868  __TEXT,__text  partial apply forwarder for implicit closure #1 () -> Swift.UnsafeRawPointer in os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.UnsafeRawBufferPointer, format: os.OSLogPointerFormat, privacy: os.OSLogPrivacy) -> ()
0x19e6c4870  __TEXT,__text  partial apply forwarder for implicit closure #2 () -> Swift.Int in os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.UnsafeRawBufferPointer, format: os.OSLogPointerFormat, privacy: os.OSLogPrivacy) -> ()
0x19e6c48a4  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.UnsafeRawPointer, bytes: @autoclosure () -> Swift.Int, format: os.OSLogPointerFormat, privacy: os.OSLogPrivacy, attributes: Swift.String) -> ()
0x19e6c4b20  __TEXT,__text  partial apply forwarder for implicit closure #1 () -> Swift.UnsafeRawPointer in os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.UnsafeRawPointer, bytes: @autoclosure () -> Swift.Int, format: os.OSLogPointerFormat, privacy: os.OSLogPrivacy) -> ()
0x19e6c4b48  __TEXT,__text  partial apply forwarder for implicit closure #2 () -> Swift.Int in os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.UnsafeRawPointer, bytes: @autoclosure () -> Swift.Int, format: os.OSLogPointerFormat, privacy: os.OSLogPrivacy) -> ()
0x19e6c4b70  __TEXT,__text  os.OSLogInterpolation.getPointerFormatSpecifier(os.OSLogPointerFormat, os.OSLogPrivacy, Swift.String) -> Swift.String
0x19e6c51c0  __TEXT,__text  partial apply forwarder for closure #1 (inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> () in os.OSLogArguments.append(() -> Swift.UnsafeRawPointer) -> ()
0x19e6c5218  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSLogPointerFormat : Swift.Hashable in os
0x19e6c521c  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogPointerFormat and conformance os.OSLogPointerFormat : Swift.Equatable in os
0x19e6c5280  __TEXT,__text  outlined init with copy of Swift.String?
0x19e6c52e8  __TEXT,__text  merged outlined destroy of (Swift.String?, Swift.String?)
0x19e6c5340  __TEXT,__text  outlined init with copy of Swift.String
0x19e6c5394  __TEXT,__text  ___swift_closure_destructor.2
0x19e6c5398  __TEXT,__text  ___swift_closure_destructor.5
0x19e6c539c  __TEXT,__text  ___swift_closure_destructor.8
0x19e6c53a0  __TEXT,__text  ___swift_closure_destructor.11
0x19e6c5b0c  __TEXT,__text  merged static os.OSLogPrivacy.private(mask: os.OSLogPrivacy.Mask) -> os.OSLogPrivacy
0x19e6c5cb0  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSLogPrivacy.PrivacyOption : Swift.Hashable in os
0x19e6c5cb4  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogPrivacy.PrivacyOption and conformance os.OSLogPrivacy.PrivacyOption : Swift.Equatable in os
0x19e6c5d08  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSLogPrivacy.Mask : Swift.Hashable in os
0x19e6c5d0c  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogPrivacy.Mask and conformance os.OSLogPrivacy.Mask : Swift.Equatable in os
0x19e6c5d60  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSLogPrivacy._MailMask : Swift.Hashable in os
0x19e6c5d64  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogPrivacy._MailMask and conformance os.OSLogPrivacy._MailMask : Swift.Equatable in os
0x19e6c5db8  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogPrivacy
0x19e6c5e48  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogPrivacy
0x19e6c5f14  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogPrivacy.Mask
0x19e6c5fa4  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogPrivacy.Mask
0x19e6c6064  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogPrivacy._MailMask
0x19e6c60f4  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogPrivacy._MailMask
0x19e6c62c8  __TEXT,__text  ___swift_closure_destructor
0x19e6c62f4  __TEXT,__text  partial apply forwarder for implicit closure #1 () -> Swift.Int32 in os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Int32, format: os.OSLogInt32ExtendedFormat, privacy: os.OSLogPrivacy) -> ()
0x19e6c631c  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Int32, format: os.OSLogInt32ExtendedFormat, privacy: os.OSLogPrivacy, attributes: Swift.String) -> ()
0x19e6c64b8  __TEXT,__text  os.OSLogInterpolation.getExtendedFormatSpecifier(os.OSLogInt32ExtendedFormat, os.OSLogPrivacy, Swift.String) -> Swift.String
0x19e6c69a0  __TEXT,__text  partial apply forwarder for implicit closure #1 () -> Swift.Int32 in os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.Bool, format: os.OSLogBoolFormat, privacy: os.OSLogPrivacy) -> ()
0x19e6c6a04  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSLogBoolFormat : Swift.Hashable in os
0x19e6c6a08  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogBoolFormat and conformance os.OSLogBoolFormat : Swift.Equatable in os
0x19e6c6a5c  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSLogInt32ExtendedFormat : Swift.Hashable in os
0x19e6c6a60  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogInt32ExtendedFormat and conformance os.OSLogInt32ExtendedFormat : Swift.Equatable in os
0x19e6c6ab4  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSLogIntExtendedFormat : Swift.Hashable in os
0x19e6c6ab8  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogIntExtendedFormat and conformance os.OSLogIntExtendedFormat : Swift.Equatable in os
0x19e6c6b0c  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogBoolFormat
0x19e6c6b0c  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogBoolFormat
0x19e6c6b0c  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogBoolFormat
0x19e6c6b0c  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogBoolFormat
0x19e6c6b9c  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogBoolFormat
0x19e6c6b9c  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogBoolFormat
0x19e6c6b9c  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogBoolFormat
0x19e6c6b9c  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogBoolFormat
0x19e6c6c5c  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogInt32ExtendedFormat
0x19e6c6cec  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogInt32ExtendedFormat
0x19e6c6dac  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogIntExtendedFormat
0x19e6c6e3c  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogIntExtendedFormat
0x19e6c6efc  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@unowned Swift.Int32) to @escaping @callee_guaranteed () -> (@out Swift.Int32)
0x19e6c6f04  __TEXT,__text  ___swift_closure_destructor.2
0x19e6c6f08  __TEXT,__text  ___swift_closure_destructor.21
0x19e6c6f24  __TEXT,__text  reabstraction thunk helper from @escaping @callee_guaranteed () -> (@out Swift.Int) to @escaping @callee_guaranteed () -> (@unowned Swift.Int)
0x19e6c6fe4  __TEXT,__text  outlined init with copy of os.OSLogStringAlignment
0x19e6c701c  __TEXT,__text  outlined destroy of os.OSLogStringAlignment
0x19e6c70d4  __TEXT,__text  key path getter for os.OSLogStringAlignment.minimumColumnWidth : (() -> Swift.Int)? : os.OSLogStringAlignment
0x19e6c7148  __TEXT,__text  key path setter for os.OSLogStringAlignment.minimumColumnWidth : (() -> Swift.Int)? : os.OSLogStringAlignment
0x19e6c72c8  __TEXT,__text  merged static os.OSLogStringAlignment.right(columns: @autoclosure () -> Swift.Int) -> os.OSLogStringAlignment
0x19e6c7364  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSLogCollectionBound : Swift.Hashable in os
0x19e6c7368  __TEXT,__text  lazy protocol witness table accessor for type os.OSLogCollectionBound and conformance os.OSLogCollectionBound : Swift.Equatable in os
0x19e6c73cc  __TEXT,__text  ___swift_memcpy17_8
0x19e6c73e0  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSLogStringAlignment
0x19e6c7438  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSLogStringAlignment
0x19e6c749c  __TEXT,__text  ___swift_closure_destructor
0x19e6c74c8  __TEXT,__text  partial apply forwarder for reabstraction thunk helper from @escaping @callee_guaranteed () -> (@out Swift.Int) to @escaping @callee_guaranteed () -> (@unowned Swift.Int)
0x19e6c7500  __TEXT,__text  ___swift_closure_destructor.6
0x19e6c7540  __TEXT,__text  outlined init with copy of os.OSLogArguments
0x19e6c7594  __TEXT,__text  outlined destroy of os.OSLogArguments
0x19e6c75e0  __TEXT,__text  outlined destroy of [(inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> ()]
0x19e6c7908  __TEXT,__text  merged os.Logger.log(os.OSLogMessage) -> ()
0x19e6c7de0  __TEXT,__text  lazy protocol witness table accessor for type [(inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> ()] and conformance [A] : Swift.Sequence in Swift
0x19e6c81a0  __TEXT,__text  partial apply forwarder for closure #1 ((inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> ()) -> () in os._checkFormatStringAndBuffer(_: os.OSLogMessage, with: (Swift.String, Swift.UnsafeBufferPointer<Swift.UI
0x19e6c81a0  __TEXT,__text  partial apply forwarder for closure #1 ((inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> ()) -> () in os._checkFormatStringAndBuffer(_: os.OSLogMessage, with: (Swift.String, Swift.UnsafeBufferPointer<Swift.UI
0x19e6c82a4  __TEXT,__text  ___swift_closure_destructor
0x19e6c82d0  __TEXT,__text  partial apply forwarder for implicit closure #1 () -> Swift.String in os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.String, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c82f8  __TEXT,__text  os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Swift.String, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy, attributes: Swift.String) -> ()
0x19e6c849c  __TEXT,__text  os.OSLogInterpolation.getStringFormatSpecifier(os.OSLogStringAlignment, os.OSLogPrivacy, Swift.String) -> Swift.String
0x19e6c8864  __TEXT,__text  closure #1 (inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> () in os.OSLogArguments.append(() -> Swift.String) -> ()
0x19e6c88dc  __TEXT,__text  partial apply forwarder for closure #1 (inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> () in os.OSLogArguments.append(() -> Swift.String) -> ()
0x19e6c88e4  __TEXT,__text  os.getNullTerminatedUTF8PointerImpl(_: Swift.String, storingStringOwnersIn: inout Swift.UnsafeMutablePointer<Any>?) -> Swift.UnsafeRawPointer
0x19e6c89b0  __TEXT,__text  generic specialization <serialized, Swift.UnsafeRawPointer> of Swift._StringGuts._deconstructUTF8<A where A: Swift._Pointer>(scratch: Swift.UnsafeMutableRawBufferPointer?) -> (owner: Swift.AnyObject?, A, length: Swift.Int, usesScratch: Swift.Bool, allocatedMemory: Swift.Bool)
0x19e6c8b1c  __TEXT,__text  outlined init with copy of Any
0x19e6c8b70  __TEXT,__text  Swift._StringGuts._allocateForDeconstruct() -> (owner: Swift.AnyObject, Swift.UnsafeRawPointer, length: Swift.Int)
0x19e6c8bbc  __TEXT,__text  generic specialization <serialized, Swift.UInt8> of Swift.UnsafeMutableRawPointer.initializeMemory<A>(as: A.Type, from: Swift.UnsafePointer<A>, count: Swift.Int) -> Swift.UnsafeMutablePointer<A>
0x19e6c8c8c  __TEXT,__text  generic specialization <serialized, Swift.String.UTF8View> of Swift._copyCollectionToContiguousArray<A where A: Swift.Collection>(A) -> Swift.ContiguousArray<A.Element>
0x19e6c8e78  __TEXT,__text  generic specialization <serialized, Swift.UInt8, [Swift.UInt8]> of Swift.Array.append<A where A == A1.Element, A1: Swift.Sequence>(contentsOf: __owned A1) -> ()
0x19e6c901c  __TEXT,__text  generic specialization <serialized, Swift.UInt8> of Swift._ContiguousArrayBuffer.init(_uninitializedCount: Swift.Int, minimumCapacity: Swift.Int) -> Swift._ContiguousArrayBuffer<A>
0x19e6c908c  __TEXT,__text  generic specialization <serialized, Swift.UInt8> of Swift.UnsafeMutablePointer.initialize(from: Swift.UnsafePointer<A>, count: Swift.Int) -> ()
0x19e6c915c  __TEXT,__text  generic specialization <serialized, Swift.UInt8> of Swift._ArrayBuffer._consumeAndCreateNew(bufferIsUnique: Swift.Bool, minimumCapacity: Swift.Int, growForAppend: Swift.Bool) -> Swift._ArrayBuffer<A>
0x19e6c920c  __TEXT,__text  generic specialization <serialized, Swift.UInt8> of Swift.UnsafeMutablePointer.moveInitialize(from: Swift.UnsafeMutablePointer<A>, count: Swift.Int) -> ()
0x19e6c9294  __TEXT,__text  function signature specialization <Arg[2] = Owned To Guaranteed> of generic specialization <serialized, Swift.UInt8> of Swift._ArrayBuffer._copyContents(subRange: Swift.Range<Swift.Int>, initializing: Swift.UnsafeMutablePointer<A>) -> Swift.UnsafeMutablePointer<A>
0x19e6c937c  __TEXT,__text  __swift_stdlib_malloc_size
0x19e6c9380  __TEXT,__text  ___swift_closure_destructor.2
0x19e6c9428  __TEXT,__text  implicit closure #1 () -> Swift.String in os.OSLogInterpolation.appendInterpolation<A where A: Swift.CustomStringConvertible>(_: @autoclosure () -> A, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c9500  __TEXT,__text  ___swift_closure_destructor
0x19e6c952c  __TEXT,__text  partial apply forwarder for implicit closure #1 () -> Swift.String in os.OSLogInterpolation.appendInterpolation<A where A: Swift.CustomStringConvertible>(_: @autoclosure () -> A, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6c95c4  __TEXT,__text  ___swift_closure_destructor.2
0x19e6c95f0  __TEXT,__text  partial apply forwarder for implicit closure #1 () -> Swift.String in os.OSLogInterpolation.appendInterpolation(_: @autoclosure () -> Any.Type, align: os.OSLogStringAlignment, privacy: os.OSLogPrivacy) -> ()
0x19e6ca600  __TEXT,__text  merged os.OSSignposter.beginInterval(_: Swift.StaticString, id: os.OSSignpostID) -> os.OSSignpostIntervalState
0x19e6cc508  __TEXT,__text  closure #1 (Swift.UnsafeMutablePointer<Swift.UInt8>, Swift.UInt32) throws -> A in os.OSSignposter.withIntervalSignpost<A>(_: Swift.StaticString, id: os.OSSignpostID, around: () throws -> A) throws -> A
0x19e6cc6f0  __TEXT,__text  protocol witness for Swift.CodingKey.init(stringValue: Swift.String) -> A? in conformance os.OSSignpostIntervalState.CodingKeys : Swift.CodingKey in os
0x19e6cc7d0  __TEXT,__text  protocol witness for Swift.CodingKey.intValue.getter : Swift.Int? in conformance os.OSSignpostIntervalState.CodingKeys : Swift.CodingKey in os
0x19e6cc7dc  __TEXT,__text  protocol witness for Swift.CodingKey.init(intValue: Swift.Int) -> A? in conformance os.OSSignpostIntervalState.CodingKeys : Swift.CodingKey in os
0x19e6cc7e8  __TEXT,__text  protocol witness for Swift.CustomStringConvertible.description.getter : Swift.String in conformance os.OSSignpostIntervalState.CodingKeys : Swift.CustomStringConvertible in os
0x19e6cc818  __TEXT,__text  protocol witness for Swift.CustomDebugStringConvertible.debugDescription.getter : Swift.String in conformance os.OSSignpostIntervalState.CodingKeys : Swift.CustomDebugStringConvertible in os
0x19e6cca4c  __TEXT,__text  os.OSSignpostIntervalState._hasValue(id: os.OSSignpostID, isOpen: Swift.Bool) -> Swift.Bool
0x19e6cca80  __TEXT,__text  protocol witness for Swift.Decodable.init(from: Swift.Decoder) throws -> A in conformance os.OSSignpostIntervalState : Swift.Decodable in os
0x19e6ccadc  __TEXT,__text  os.id(Swift.String) -> Swift.String
0x19e6ccb10  __TEXT,__text  closure #1 (Swift.UnsafeMutablePointer<Swift.UInt8>, Swift.UInt32) -> () in os.osSignpostWithoutMessage(log: __C.OS_os_log, name: Swift.StaticString, id: os.OSSignpostID, type: __C.os_signpost_type_t, state: os.OSSignpostIntervalState?, formatString: Swift.String) -> ()
0x19e6ccb68  __TEXT,__text  closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> Swift.UnsafePointer<Swift.Int8> in os._globalStringTablePointerOfStaticString(Swift.StaticString) -> Swift.UnsafePointer<Swift.Int8>
0x19e6ccbcc  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> A in Swift.StaticString.withUTF8Buffer<A>((Swift.UnsafeBufferPointer<Swift.UInt8>) -> A) -> A
0x19e6ccbfc  __TEXT,__text  generic partial specialization <serialized, Signature = @escaping @convention(thin) @convention(method) <A, B where B == Swift.Never> (@guaranteed @callee_guaranteed @substituted <A, B where A: ~Swift.Copyable, A: ~Swift.Escapable, B: ~Swift.Copyable, B: ~Swift.Escapable> (@unowned Swift.UnsafeBuffe
0x19e6cccd0  __TEXT,__text  partial apply forwarder for closure #1 ((inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> ()) -> () in os.emitSignpost<A>(preamble: Swift.UInt8, argumentCount: Swift.UInt8, bufferSize: Swift.Int, objectCount: 
0x19e6ccce8  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeMutablePointer<Swift.UInt8>, Swift.UInt32) throws -> A in os.OSSignposter.withIntervalSignpost<A>(_: Swift.StaticString, id: os.OSSignpostID, around: () throws -> A) throws -> A
0x19e6ccd1c  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSSignpostError : Swift.Hashable in os
0x19e6ccd20  __TEXT,__text  lazy protocol witness table accessor for type os.OSSignpostError and conformance os.OSSignpostError : Swift.Equatable in os
0x19e6cce14  __TEXT,__text  type metadata accessor for os.OSSignpostIntervalState.CodingKeys
0x19e6cce24  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSSignpostIntervalState.CodingKeys : Swift.Hashable in os
0x19e6cce28  __TEXT,__text  lazy protocol witness table accessor for type os.OSSignpostIntervalState.CodingKeys and conformance os.OSSignpostIntervalState.CodingKeys : Swift.Equatable in os
0x19e6cce7c  __TEXT,__text  base witness table accessor for Swift.CustomDebugStringConvertible in os.OSSignpostIntervalState.CodingKeys : Swift.CodingKey in os
0x19e6cce80  __TEXT,__text  lazy protocol witness table accessor for type os.OSSignpostIntervalState.CodingKeys and conformance os.OSSignpostIntervalState.CodingKeys : Swift.CustomDebugStringConvertible in os
0x19e6cced4  __TEXT,__text  base witness table accessor for Swift.CustomStringConvertible in os.OSSignpostIntervalState.CodingKeys : Swift.CodingKey in os
0x19e6cced8  __TEXT,__text  lazy protocol witness table accessor for type os.OSSignpostIntervalState.CodingKeys and conformance os.OSSignpostIntervalState.CodingKeys : Swift.CustomStringConvertible in os
0x19e6ccf2c  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> A in Swift.StaticString.withUTF8Buffer<A>((Swift.UnsafeBufferPointer<Swift.UInt8>) -> A) -> A with unmangled suffix ".1"
0x19e6ccf2c  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> A in Swift.StaticString.withUTF8Buffer<A>((Swift.UnsafeBufferPointer<Swift.UInt8>) -> A) -> A with unmangled suffix ".1"
0x19e6ccf2c  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> A in Swift.StaticString.withUTF8Buffer<A>((Swift.UnsafeBufferPointer<Swift.UInt8>) -> A) -> A with unmangled suffix ".1"
0x19e6ccf2c  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> A in Swift.StaticString.withUTF8Buffer<A>((Swift.UnsafeBufferPointer<Swift.UInt8>) -> A) -> A with unmangled suffix ".1"
0x19e6ccf2c  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> A in Swift.StaticString.withUTF8Buffer<A>((Swift.UnsafeBufferPointer<Swift.UInt8>) -> A) -> A with unmangled suffix ".1"
0x19e6ccf2c  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> A in Swift.StaticString.withUTF8Buffer<A>((Swift.UnsafeBufferPointer<Swift.UInt8>) -> A) -> A with unmangled suffix ".1"
0x19e6ccf2c  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> A in Swift.StaticString.withUTF8Buffer<A>((Swift.UnsafeBufferPointer<Swift.UInt8>) -> A) -> A with unmangled suffix ".1"
0x19e6ccf2c  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> A in Swift.StaticString.withUTF8Buffer<A>((Swift.UnsafeBufferPointer<Swift.UInt8>) -> A) -> A with unmangled suffix ".1"
0x19e6ccf2c  __TEXT,__text  partial apply forwarder for closure #1 (Swift.UnsafeBufferPointer<Swift.UInt8>) -> A in Swift.StaticString.withUTF8Buffer<A>((Swift.UnsafeBufferPointer<Swift.UInt8>) -> A) -> A with unmangled suffix ".1"
0x19e6ccf44  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSSignpostIntervalState.CodingKeys
0x19e6ccf44  __TEXT,__text  storeEnumTagSinglePayload value witness for os.OSSignpostIntervalState.CodingKeys
0x19e6ccf48  __TEXT,__text  partial apply forwarder for closure #1 ((inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> ()) -> () in os.emitSignpost<A>(preamble: Swift.UInt8, argumentCount: Swift.UInt8, bufferSize: Swift.Int, objectCount: 
0x19e6ccf48  __TEXT,__text  partial apply forwarder for closure #1 ((inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> ()) -> () in os.emitSignpost<A>(preamble: Swift.UInt8, argumentCount: Swift.UInt8, bufferSize: Swift.Int, objectCount: 
0x19e6ccf48  __TEXT,__text  partial apply forwarder for closure #1 ((inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> ()) -> () in os.emitSignpost<A>(preamble: Swift.UInt8, argumentCount: Swift.UInt8, bufferSize: Swift.Int, objectCount: 
0x19e6ccf48  __TEXT,__text  partial apply forwarder for closure #1 ((inout Swift.UnsafeMutablePointer<Swift.UInt8>, inout Swift.UnsafeMutablePointer<__C.NSObject?>?, inout Swift.UnsafeMutablePointer<Any>?) -> ()) -> () in os.emitSignpost<A>(preamble: Swift.UInt8, argumentCount: Swift.UInt8, bufferSize: Swift.Int, objectCount: 
0x19e6ccf60  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSSignpostIntervalState.CodingKeys
0x19e6ccf60  __TEXT,__text  getEnumTagSinglePayload value witness for os.OSSignpostIntervalState.CodingKeys
0x19e6cd06c  __TEXT,__text  merged os.OSLogInterpolation.getPointerFormatSpecifier(os.OSLogPointerFormat, os.OSLogPrivacy) -> Swift.String
0x19e6cd9cc  __TEXT,__text  function signature specialization <Arg[0] = [Closure Propagated : $sSo15OS_os_workgroupC0B0E4copy4nameABSgSSSg_tFAFSPys4Int8VGXEfU_, Argument Types : [__C.OS_os_workgroup]> of generic specialization <__C.OS_os_workgroup?, Swift.Never> of Swift._StringGuts._slowWithCString<A, B where B: Swift.Error>(
0x19e6cda2c  __TEXT,__text  generic specialization <os.OSMetricFlags> of (extension in Swift):Swift.SetAlgebra< where A.ArrayLiteralElement == A.Element>.init(arrayLiteral: A.ArrayLiteralElement...) -> A
0x19e6cdb4c  __TEXT,__text  generic specialization <os.OSAllocatedUnfairLockFlags> of (extension in Swift):Swift.SetAlgebra< where A.ArrayLiteralElement == A.Element>.init(arrayLiteral: A.ArrayLiteralElement...) -> A
0x19e6cdc14  __TEXT,__text  one-time initialization function for adaptiveSpin
0x19e6cdc8c  __TEXT,__text  protocol witness for Swift.OptionSet.init(rawValue: A.RawValue) -> A in conformance os.OSAllocatedUnfairLockFlags : Swift.OptionSet in os
0x19e6cdc98  __TEXT,__text  protocol witness for Swift.RawRepresentable.init(rawValue: A.RawValue) -> A? in conformance os.OSAllocatedUnfairLockFlags : Swift.RawRepresentable in os
0x19e6cdca8  __TEXT,__text  protocol witness for Swift.RawRepresentable.rawValue.getter : A.RawValue in conformance os.OSAllocatedUnfairLockFlags : Swift.RawRepresentable in os
0x19e6cdcb4  __TEXT,__text  protocol witness for Swift.SetAlgebra.init() -> A in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdcbc  __TEXT,__text  protocol witness for Swift.SetAlgebra.union(__owned A) -> A in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdcd0  __TEXT,__text  protocol witness for Swift.SetAlgebra.intersection(A) -> A in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdce4  __TEXT,__text  protocol witness for Swift.SetAlgebra.symmetricDifference(__owned A) -> A in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdcf8  __TEXT,__text  protocol witness for Swift.SetAlgebra.insert(__owned A.Element) -> (inserted: Swift.Bool, memberAfterInsert: A.Element) in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdd18  __TEXT,__text  protocol witness for Swift.SetAlgebra.remove(A.Element) -> A.Element? in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdd48  __TEXT,__text  protocol witness for Swift.SetAlgebra.update(with: __owned A.Element) -> A.Element? in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdd6c  __TEXT,__text  protocol witness for Swift.SetAlgebra.formUnion(__owned A) -> () in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdd80  __TEXT,__text  protocol witness for Swift.SetAlgebra.formIntersection(A) -> () in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdd94  __TEXT,__text  protocol witness for Swift.SetAlgebra.formSymmetricDifference(__owned A) -> () in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdda8  __TEXT,__text  protocol witness for Swift.SetAlgebra.subtracting(A) -> A in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cddbc  __TEXT,__text  protocol witness for Swift.SetAlgebra.isSubset(of: A) -> Swift.Bool in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cddd0  __TEXT,__text  protocol witness for Swift.SetAlgebra.isDisjoint(with: A) -> Swift.Bool in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdde4  __TEXT,__text  protocol witness for Swift.SetAlgebra.isEmpty.getter : Swift.Bool in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cddf4  __TEXT,__text  protocol witness for Swift.SetAlgebra.subtract(A) -> () in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cde08  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSAllocatedUnfairLockFlags : Swift.Equatable in os
0x19e6cde1c  __TEXT,__text  protocol witness for Swift.ExpressibleByArrayLiteral.init(arrayLiteral: A.ArrayLiteralElement...) -> A in conformance os.OSAllocatedUnfairLockFlags : Swift.ExpressibleByArrayLiteral in os
0x19e6cdea0  __TEXT,__text  base witness table accessor for Swift.RawRepresentable in os.OSAllocatedUnfairLockFlags : Swift.OptionSet in os
0x19e6cdea4  __TEXT,__text  lazy protocol witness table accessor for type os.OSAllocatedUnfairLockFlags and conformance os.OSAllocatedUnfairLockFlags : Swift.RawRepresentable in os
0x19e6cdef8  __TEXT,__text  base witness table accessor for Swift.SetAlgebra in os.OSAllocatedUnfairLockFlags : Swift.OptionSet in os
0x19e6cdefc  __TEXT,__text  lazy protocol witness table accessor for type os.OSAllocatedUnfairLockFlags and conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdf50  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdf54  __TEXT,__text  lazy protocol witness table accessor for type os.OSAllocatedUnfairLockFlags and conformance os.OSAllocatedUnfairLockFlags : Swift.Equatable in os
0x19e6cdfa8  __TEXT,__text  base witness table accessor for Swift.ExpressibleByArrayLiteral in os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6cdfac  __TEXT,__text  lazy protocol witness table accessor for type os.OSAllocatedUnfairLockFlags and conformance os.OSAllocatedUnfairLockFlags : Swift.ExpressibleByArrayLiteral in os
0x19e6ce000  __TEXT,__text  protocol witness for static Swift.Equatable.== infix(A, A) -> Swift.Bool in conformance os.OSAllocatedUnfairLock<A>.Ownership : Swift.Equatable in os
0x19e6ce00c  __TEXT,__text  base witness table accessor for Swift.Equatable in os.OSAllocatedUnfairLock<A>.Ownership : Swift.Hashable in os
0x19e6ce028  __TEXT,__text  protocol witness for Swift.Hashable.hashValue.getter : Swift.Int in conformance os.OSAllocatedUnfairLock<A>.Ownership : Swift.Hashable in os
0x19e6ce030  __TEXT,__text  protocol witness for Swift.Hashable.hash(into: inout Swift.Hasher) -> () in conformance os.OSAllocatedUnfairLock<A>.Ownership : Swift.Hashable in os
0x19e6ce038  __TEXT,__text  protocol witness for Swift.Hashable._rawHashValue(seed: Swift.Int) -> Swift.Int in conformance os.OSAllocatedUnfairLock<A>.Ownership : Swift.Hashable in os
0x19e6ce088  __TEXT,__text  type metadata instantiation function for os.OSAllocatedUnfairLock.Ownership
0x19e6ce0a8  __TEXT,__text  protocol witness for Swift.SetAlgebra.contains(A.Element) -> Swift.Bool in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6ce0a8  __TEXT,__text  protocol witness for Swift.SetAlgebra.contains(A.Element) -> Swift.Bool in conformance os.OSAllocatedUnfairLockFlags : Swift.SetAlgebra in os
0x19e6ce0ac  __TEXT,__text  _os_trace_blob_add_slow
```

