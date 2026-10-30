# Symbols: `/System/Library/Frameworks/CloudKit.framework/CloudKit`

Symbol table of this image in the iOS 27.2 dyld shared cache (`ipsw dyld macho -n --demangle`). The class-level view is on the [image page](../userland/System__Library__Frameworks__CloudKit.framework__CloudKit.md). **[DSC]**

4,503 public symbols, 0 private symbols, 0 undefined (imported).

## Public (external)

```
0x197ef3258  __TEXT,__const  protocol conformance descriptor for Foundation.Data : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca9688  __AUTH_CONST,__const  protocol witness table for Foundation.Data : CloudKit.CKRecordValueProtocol in CloudKit
0x197ec3c24  __TEXT,__text  (extension in CloudKit):Foundation.Data.ckHexString() -> Swift.String
0x197ec3acc  __TEXT,__text  (extension in CloudKit):Foundation.Data.ckBase64URLSafeString() -> Swift.String
0x197ec3bc8  __TEXT,__text  (extension in CloudKit):Foundation.Data.ckLowercaseHexStringWithoutSpaces() -> Swift.String
0x197ef3238  __TEXT,__const  protocol conformance descriptor for Foundation.Date : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca9660  __AUTH_CONST,__const  protocol witness table for Foundation.Date : CloudKit.CKRecordValueProtocol in CloudKit
0x197e2ca10  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.ContainerID.init(__C.CKContainerID) -> CloudCoreInternal.ContainerID
0x197e21420  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.AnonymousSession.publicCloudDatabase.getter : __C.CKDatabase
0x197ef5028  __TEXT,__const  property descriptor for (extension in CloudKit):CloudCoreInternal.AnonymousSession.publicCloudDatabase : __C.CKDatabase
0x197e20f08  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.AuthenticatedSession.accept([__C.CKShareMetadata]) async throws -> [__C.CKShareMetadata : Swift.Result<__C.CKShare, Swift.Error>]
0x197ef5010  __TEXT,__const  async function pointer to (extension in CloudKit):CloudCoreInternal.AuthenticatedSession.accept([__C.CKShareMetadata]) async throws -> [__C.CKShareMetadata : Swift.Result<__C.CKShare, Swift.Error>]
0x197e20c74  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.AuthenticatedSession.accept(__C.CKShareMetadata) async throws -> __C.CKShare
0x197ef5008  __TEXT,__const  async function pointer to (extension in CloudKit):CloudCoreInternal.AuthenticatedSession.accept(__C.CKShareMetadata) async throws -> __C.CKShare
0x197e21318  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.AuthenticatedSession.decline([__C.CKShareMetadata]) async throws -> [__C.CKShareMetadata : Swift.Result<(), Swift.Error>]
0x197ef5020  __TEXT,__const  async function pointer to (extension in CloudKit):CloudCoreInternal.AuthenticatedSession.decline([__C.CKShareMetadata]) async throws -> [__C.CKShareMetadata : Swift.Result<(), Swift.Error>]
0x197e2109c  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.AuthenticatedSession.decline(__C.CKShareMetadata) async throws -> ()
0x197ef5018  __TEXT,__const  async function pointer to (extension in CloudKit):CloudCoreInternal.AuthenticatedSession.decline(__C.CKShareMetadata) async throws -> ()
0x197e2145c  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.AuthenticatedSession.database(configuration: CloudKit.CKDatabaseConfiguration) -> __C.CKDatabase
0x197e1fac8  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.AuthenticatedSession.ResolvedUser.userRecordID.getter : __C.CKRecordID
0x197ef4f40  __TEXT,__const  property descriptor for (extension in CloudKit):CloudCoreInternal.AuthenticatedSession.ResolvedUser.userRecordID : __C.CKRecordID
0x197e32754  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.EntitlementsProtocol.ckCompatibilityOverlay(configuration: CloudCoreInternal.AnySessionConfiguration) -> [Swift.String : Swift.String]
0x197e1fc28  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.Session.codeService(configuration: CloudKit.CKCodeServiceConfiguration) throws -> __C.CKCodeService
0x197e207d8  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.Session.shareMetadata(for: Foundation.URL) async throws -> __C.CKShareMetadata
0x197ef4ff0  __TEXT,__const  async function pointer to (extension in CloudKit):CloudCoreInternal.Session.shareMetadata(for: Foundation.URL) async throws -> __C.CKShareMetadata
0x197e20bbc  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.Session.shareMetadatas(for: [Foundation.URL], invitationTokensByShareURL: [Foundation.URL : __C.CKDeviceToDeviceShareInvitationToken]) async throws -> [Foundation.URL : Swift.Result<__C.CKShareMetadata, Swift.Error>]
0x197ef5000  __TEXT,__const  async function pointer to (extension in CloudKit):CloudCoreInternal.Session.shareMetadatas(for: [Foundation.URL], invitationTokensByShareURL: [Foundation.URL : __C.CKDeviceToDeviceShareInvitationToken]) async throws -> [Foundation.URL : Swift.Result<__C.CKShareMetadata, Swift.Error>]
0x197e20b14  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.Session.shareMetadatas(for: [Foundation.URL]) async throws -> [Foundation.URL : Swift.Result<__C.CKShareMetadata, Swift.Error>]
0x197ef4ff8  __TEXT,__const  async function pointer to (extension in CloudKit):CloudCoreInternal.Session.shareMetadatas(for: [Foundation.URL]) async throws -> [Foundation.URL : Swift.Result<__C.CKShareMetadata, Swift.Error>]
0x197e20494  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.Session.shareParticipant(for: __C.CKUserIdentityLookupInfo) async throws -> __C.CKShareParticipant
0x197ef4fe0  __TEXT,__const  async function pointer to (extension in CloudKit):CloudCoreInternal.Session.shareParticipant(for: __C.CKUserIdentityLookupInfo) async throws -> __C.CKShareParticipant
0x197e20730  __TEXT,__text  (extension in CloudKit):CloudCoreInternal.Session.shareParticipants(for: [__C.CKUserIdentityLookupInfo]) async throws -> [__C.CKUserIdentityLookupInfo : Swift.Result<__C.CKShareParticipant, Swift.Error>]
0x197ef4fe8  __TEXT,__const  async function pointer to (extension in CloudKit):CloudCoreInternal.Session.shareParticipants(for: [__C.CKUserIdentityLookupInfo]) async throws -> [__C.CKUserIdentityLookupInfo : Swift.Result<__C.CKShareParticipant, Swift.Error>]
0x197ef59c0  __TEXT,__const  protocol conformance descriptor for CloudKit.CloudCoreEntryPoint : CloudCoreInternal.CKImplementingCC.EntryPointProtocol in CloudKit
0x197e34840  __TEXT,__text  CloudKit.CloudCoreEntryPoint.makeContainer<A where A: CloudCoreInternal.SessionConfiguration>(sessionID: CloudCoreInternal.SessionID, sessionConfiguration: A, anySessionAcquiredInfo: CloudCoreInternal.AnySessionAcquiredInfo) -> CloudCoreInternal.CKImplementingCC.ContainerProtocol
0x197e34864  __TEXT,__text  static CloudKit.CloudCoreEntryPoint.makeContainer<A where A: CloudCoreInternal.SessionConfiguration>(sessionID: CloudCoreInternal.SessionID, sessionConfiguration: A, anySessionAcquiredInfo: CloudCoreInternal.AnySessionAcquiredInfo, testDeviceReferenceProtocol: Swift.AnyObject?) -> CloudCoreInternal.
0x197e34bf8  __TEXT,__text  CloudKit.CloudCoreEntryPoint.isRunningInAdopterProcess.getter : Swift.Bool
0x197ef59f8  __TEXT,__const  property descriptor for CloudKit.CloudCoreEntryPoint.isRunningInAdopterProcess : Swift.Bool
0x197e34b2c  __TEXT,__text  CloudKit.CloudCoreEntryPoint.sessionAcquisitionManager.getter : CloudCoreInternal.CKImplementingCC.SessionAcquisitionManagerProtocol
0x197ef59f8  __TEXT,__const  property descriptor for CloudKit.CloudCoreEntryPoint.sessionAcquisitionManager : CloudCoreInternal.CKImplementingCC.SessionAcquisitionManagerProtocol
0x197e34c10  __TEXT,__text  CloudKit.CloudCoreEntryPoint.__allocating_init() -> CloudKit.CloudCoreEntryPoint
0x197e34c30  __TEXT,__text  CloudKit.CloudCoreEntryPoint.init() -> CloudKit.CloudCoreEntryPoint
0x197e34d1c  __TEXT,__text  type metadata accessor for CloudKit.CloudCoreEntryPoint
0x197f29058  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CloudCoreEntryPoint
0x197ef5a18  __TEXT,__const  class metadata base offset for CloudKit.CloudCoreEntryPoint
0x1ef67ac60  __AUTH,__objc_data  type metadata for CloudKit.CloudCoreEntryPoint
0x197e34c8c  __TEXT,__text  CloudKit.CloudCoreEntryPoint.__deallocating_deinit
0x197ec0624  __TEXT,__text  CloudKit.CKLogAsset.getter : os.Logger
0x197ec08ec  __TEXT,__text  CloudKit.CKLogEngine.getter : os.Logger
0x197ec0564  __TEXT,__text  CloudKit.CKLogStatus.getter : os.Logger
0x197e2b1c0  __TEXT,__text  CloudKit.CKSessionID.sessionID.modify : CloudCoreInternal.SessionID
0x197e2afb8  __TEXT,__text  CloudKit.CKSessionID.sessionID.getter : CloudCoreInternal.SessionID
0x1e0c41530  __DATA_CONST,__const  property descriptor for CloudKit.CKSessionID.sessionID : CloudCoreInternal.SessionID
0x197e2b100  __TEXT,__text  CloudKit.CKSessionID.sessionID.setter : CloudCoreInternal.SessionID
0x197ecbe58  __TEXT,__text  CloudKit.CKSessionID.__allocating_init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionID?
0x197ecbe88  __TEXT,__text  CloudKit.CKSessionID.init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionID?
0x197e2b524  __TEXT,__text  CloudKit.CKSessionID.__allocating_init(sqliteRepresentation: Swift.String) -> CloudKit.CKSessionID?
0x197e2b568  __TEXT,__text  CloudKit.CKSessionID.init(sqliteRepresentation: Swift.String) -> CloudKit.CKSessionID?
0x197e2b458  __TEXT,__text  static CloudKit.CKSessionID.supportsSecureCoding.getter : Swift.Bool
0x197ecbe28  __TEXT,__text  CloudKit.CKSessionID.__allocating_init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionID?
0x197ecbe98  __TEXT,__text  CloudKit.CKSessionID.init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionID?
0x197e2b460  __TEXT,__text  CloudKit.CKSessionID.__allocating_init(coder: __C.NSCoder) -> CloudKit.CKSessionID?
0x197e2b494  __TEXT,__text  CloudKit.CKSessionID.init(coder: __C.NSCoder) -> CloudKit.CKSessionID?
0x197ecbdf8  __TEXT,__text  CloudKit.CKSessionID.__allocating_init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSessionID
0x197ecbea8  __TEXT,__text  CloudKit.CKSessionID.init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSessionID
0x197e2b63c  __TEXT,__text  type metadata accessor for CloudKit.CKSessionID
0x197f28d74  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSessionID
0x197ef5728  __TEXT,__const  class metadata base offset for CloudKit.CKSessionID
0x197e2b660  __TEXT,__text  method lookup function for CloudKit.CKSessionID
0x1ef67aa18  __AUTH,__objc_data  type metadata for CloudKit.CKSessionID
0x197e2b604  __TEXT,__text  CloudKit.CKSessionID.__deallocating_deinit
0x197e2af84  __TEXT,__text  CloudKit.CKSessionID.__allocating_init(CloudCoreInternal.SessionID) -> CloudKit.CKSessionID
0x197e2b678  __TEXT,__text  dispatch thunk of CloudKit.CKSessionID.__allocating_init(CloudCoreInternal.SessionID) -> CloudKit.CKSessionID
0x197f28da8  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSessionID.__allocating_init(CloudCoreInternal.SessionID) -> CloudKit.CKSessionID
0x197e2b328  __TEXT,__text  CloudKit.CKSessionID.init(CloudCoreInternal.SessionID) -> CloudKit.CKSessionID
0x197e06030  __TEXT,__text  CloudKit.CKFeatureSet.description.getter : Swift.String
0x197ef27f4  __TEXT,__const  property descriptor for CloudKit.CKFeatureSet.description : Swift.String
0x197e06650  __TEXT,__text  CloudKit.CKFeatureSet.init(arrayLiteral: (name: Swift.String, value: Swift.String)...) -> CloudKit.CKFeatureSet<A>
0x197e063c4  __TEXT,__text  CloudKit.CKFeatureSet.makeIterator() -> CloudKit.CKFeatureSet<A>.Iterator
0x197e03598  __TEXT,__text  CloudKit.CKFeatureSet.valuesByName.getter : [Swift.String : some]
0x197ef27f4  __TEXT,__const  property descriptor for CloudKit.CKFeatureSet.valuesByName : [Swift.String : some]
0x197f28454  __TEXT,__constg_swiftt  opaque type descriptor for <<opaque return type of CloudKit.CKFeatureSet.valuesByName : [Swift.String : some]>>
0x197e06420  __TEXT,__text  CloudKit.CKFeatureSet.init(dictionaryLiteral: (Swift.String, [Swift.String])...) -> CloudKit.CKFeatureSet<A>
0x197e052f8  __TEXT,__text  static CloudKit.CKFeatureSet.== infix(CloudKit.CKFeatureSet<A>, CloudKit.CKFeatureSet<A>) -> Swift.Bool
0x197e05c00  __TEXT,__text  CloudKit.CKFeatureSet.hash(into: inout Swift.Hasher) -> ()
0x197e04b48  __TEXT,__text  CloudKit.CKFeatureSet.insert(name: Swift.String, value: Swift.String) -> ()
0x197e03134  __TEXT,__text  CloudKit.CKFeatureSet.insert<A where A == A1.Element, A1: Swift.Collection>(A1) -> ()
0x197e04804  __TEXT,__text  CloudKit.CKFeatureSet.insert(A) -> ()
0x197e04c4c  __TEXT,__text  CloudKit.CKFeatureSet.remove(name: Swift.String, value: Swift.String) -> A?
0x197e04d54  __TEXT,__text  CloudKit.CKFeatureSet.remove(A) -> A?
0x197e03f44  __TEXT,__text  CloudKit.CKFeatureSet.subscript.modify : (values: Swift.String) -> [Swift.String]
0x197e03be8  __TEXT,__text  CloudKit.CKFeatureSet.subscript.getter : (values: Swift.String) -> [Swift.String]
0x1e0c413ec  __DATA_CONST,__const  property descriptor for CloudKit.CKFeatureSet.subscript(values: Swift.String) -> [Swift.String]
0x197e03e18  __TEXT,__text  CloudKit.CKFeatureSet.subscript.setter : (values: Swift.String) -> [Swift.String]
0x197e038c4  __TEXT,__text  CloudKit.CKFeatureSet.isEmpty.getter : Swift.Bool
0x197ef27f4  __TEXT,__const  property descriptor for CloudKit.CKFeatureSet.isEmpty : Swift.Bool
0x197e04358  __TEXT,__text  static CloudKit.CKFeatureSet.isValid(A) -> Swift.Bool
0x197e062e4  __TEXT,__text  CloudKit.CKFeatureSet.Iterator.next() -> (Swift.String, [A])?
0x197e098bc  __TEXT,__text  type metadata accessor for CloudKit.CKFeatureSet.Iterator
0x197f283bc  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKFeatureSet.Iterator
0x197ef2664  __TEXT,__const  protocol conformance descriptor for CloudKit.CKFeatureSet<A>.Iterator : Swift.IteratorProtocol in CloudKit
0x197e041d8  __TEXT,__text  CloudKit.CKFeatureSet.contains(name: Swift.String, value: Swift.String) -> Swift.Bool
0x197e04070  __TEXT,__text  CloudKit.CKFeatureSet.contains(name: Swift.String) -> Swift.Bool
0x197e040f8  __TEXT,__text  CloudKit.CKFeatureSet.contains(A) -> Swift.Bool
0x197e03460  __TEXT,__text  CloudKit.CKFeatureSet.features.getter : some
0x197ef27f4  __TEXT,__const  property descriptor for CloudKit.CKFeatureSet.features : some
0x197f28414  __TEXT,__constg_swiftt  opaque type descriptor for <<opaque return type of CloudKit.CKFeatureSet.features : some>>
0x197e05f90  __TEXT,__text  CloudKit.CKFeatureSet.hashValue.getter : Swift.Int
0x197ef27f4  __TEXT,__const  property descriptor for CloudKit.CKFeatureSet.hashValue : Swift.Int
0x197e03a58  __TEXT,__text  CloudKit.CKFeatureSet.removeAll(for: Swift.String) -> some
0x197f284b4  __TEXT,__constg_swiftt  opaque type descriptor for <<opaque return type of CloudKit.CKFeatureSet.removeAll(for: Swift.String) -> some>>
0x197e03060  __TEXT,__text  CloudKit.CKFeatureSet.init() -> CloudKit.CKFeatureSet<A>
0x197e03448  __TEXT,__text  type metadata accessor for CloudKit.CKFeatureSet
0x197f28380  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKFeatureSet
0x197e030a4  __TEXT,__text  CloudKit.CKFeatureSet.init<A where A == A1.Element, A1: Swift.Collection>(A1) -> CloudKit.CKFeatureSet<A>
0x197e03b60  __TEXT,__text  CloudKit.CKFeatureSet.subscript.modify : (Swift.String) -> [A]
0x197e03900  __TEXT,__text  CloudKit.CKFeatureSet.subscript.getter : (Swift.String) -> [A]
0x1e0c413d0  __DATA_CONST,__const  property descriptor for CloudKit.CKFeatureSet.subscript(Swift.String) -> [A]
0x197e03958  __TEXT,__text  CloudKit.CKFeatureSet.subscript.setter : (Swift.String) -> [A]
0x197ef25fc  __TEXT,__const  protocol conformance descriptor for CloudKit.CKFeatureSet<A> : Swift.Hashable in CloudKit
0x197ef25d4  __TEXT,__const  protocol conformance descriptor for CloudKit.CKFeatureSet<A> : Swift.Equatable in CloudKit
0x197ef2694  __TEXT,__const  protocol conformance descriptor for CloudKit.CKFeatureSet<A> : Swift.Sequence in CloudKit
0x197ef263c  __TEXT,__const  protocol conformance descriptor for CloudKit.CKFeatureSet<A> : Swift.CustomStringConvertible in CloudKit
0x197ef2734  __TEXT,__const  protocol conformance descriptor for CloudKit.CKFeatureSet<A> : Swift.ExpressibleByArrayLiteral in CloudKit
0x197ef26fc  __TEXT,__const  protocol conformance descriptor for CloudKit.CKFeatureSet<A> : Swift.ExpressibleByDictionaryLiteral in CloudKit
0x197ec05a8  __TEXT,__text  CloudKit.CKLogRequest.getter : os.Logger
0x197ea04b0  __TEXT,__text  CloudKit.CKSyncEngine.SyncReason.description.getter : Swift.String
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.SyncReason.description : Swift.String
0x197e9fd84  __TEXT,__text  static CloudKit.CKSyncEngine.SyncReason.== infix(CloudKit.CKSyncEngine.SyncReason, CloudKit.CKSyncEngine.SyncReason) -> Swift.Bool
0x197e9fd98  __TEXT,__text  CloudKit.CKSyncEngine.SyncReason.hash(into: inout Swift.Hasher) -> ()
0x197efa4d4  __TEXT,__const  enum case for CloudKit.CKSyncEngine.SyncReason.manual(CloudKit.CKSyncEngine.SyncReason.Type) -> CloudKit.CKSyncEngine.SyncReason
0x197e9fdc4  __TEXT,__text  CloudKit.CKSyncEngine.SyncReason.hashValue.getter : Swift.Int
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.SyncReason.hashValue : Swift.Int
0x197efa4d0  __TEXT,__const  enum case for CloudKit.CKSyncEngine.SyncReason.scheduled(CloudKit.CKSyncEngine.SyncReason.Type) -> CloudKit.CKSyncEngine.SyncReason
0x197ea75d0  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.SyncReason
0x197f29cd8  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.SyncReason
0x1e3ca9100  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.SyncReason
0x197ef9db0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.SyncReason : Swift.Hashable in CloudKit
0x197ef9d88  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.SyncReason : Swift.Equatable in CloudKit
0x197ef9f08  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.SyncReason : Swift.CustomStringConvertible in CloudKit
0x197e8da44  __TEXT,__text  CloudKit.CKSyncEngine.description.getter : Swift.String
0x197ef7348  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.description : Swift.String
0x197e8d4ac  __TEXT,__text  CloudKit.CKSyncEngine.fetchAssets(_: CloudKit.CKSyncEngine.FetchAssetsOptions, subprogress: __owned Foundation.Subprogress?) -> any Swift.AsyncSequence<Self.Swift.AsyncSequence.Element == (assetID: (extension in CloudKit):__C.CKAsset.ID, result: Swift.Result<__C.CKAsset, Swift.Error>), Self.Swift.As
0x197e8d2cc  __TEXT,__text  CloudKit.CKSyncEngine.sendChanges(CloudKit.CKSyncEngine.SendChangesOptions) async throws -> ()
0x197ef7310  __TEXT,__const  async function pointer to CloudKit.CKSyncEngine.sendChanges(CloudKit.CKSyncEngine.SendChangesOptions) async throws -> ()
0x197e8d008  __TEXT,__text  CloudKit.CKSyncEngine.fetchChanges(CloudKit.CKSyncEngine.FetchChangesOptions) async throws -> ()
0x197ef7308  __TEXT,__const  async function pointer to CloudKit.CKSyncEngine.fetchChanges(CloudKit.CKSyncEngine.FetchChangesOptions) async throws -> ()
0x197e946b4  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.description.getter : Swift.String
0x197ef76a8  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Configuration.description : Swift.String
0x197e94370  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.subscriptionID.modify : Swift.String?
0x197e9430c  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.subscriptionID.getter : Swift.String?
0x197ef7690  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Configuration.subscriptionID : Swift.String?
0x197e9433c  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.subscriptionID.setter : Swift.String?
0x197e943ec  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.delegatePrivate.modify : CloudKit.CKSyncEngineDelegatePrivate?
0x197e94390  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.delegatePrivate.getter : CloudKit.CKSyncEngineDelegatePrivate?
0x197ef7694  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Configuration.delegatePrivate : CloudKit.CKSyncEngineDelegatePrivate?
0x197e943b8  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.delegatePrivate.setter : CloudKit.CKSyncEngineDelegatePrivate?
0x197e942ec  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.automaticallySync.modify : Swift.Bool
0x197e942e4  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.automaticallySync.getter : Swift.Bool
0x197ef768c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Configuration.automaticallySync : Swift.Bool
0x197c28d50  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.automaticallySync.setter : Swift.Bool
0x197e9443c  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.apsMachServiceName.modify : Swift.String?
0x197e9440c  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.apsMachServiceName.getter : Swift.String?
0x197ef7698  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Configuration.apsMachServiceName : Swift.String?
0x197c28d1c  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.apsMachServiceName.setter : Swift.String?
0x197e94248  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.stateSerialization.modify : CloudKit.CKSyncEngine.State.Serialization?
0x197e94208  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.stateSerialization.getter : CloudKit.CKSyncEngine.State.Serialization?
0x197ef7684  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Configuration.stateSerialization : CloudKit.CKSyncEngine.State.Serialization?
0x197e94214  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.stateSerialization.setter : CloudKit.CKSyncEngine.State.Serialization?
0x197e945f0  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.useOpportunisticPushTopic.modify : Swift.Bool
0x197e945e0  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.useOpportunisticPushTopic.getter : Swift.Bool
0x197ef769c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Configuration.useOpportunisticPushTopic : Swift.Bool
0x197e945e8  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.useOpportunisticPushTopic.setter : Swift.Bool
0x197e94694  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.assetDownloadStagingManager.modify : __C.CKAssetDownloadStagingManager?
0x197e94640  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.assetDownloadStagingManager.getter : __C.CKAssetDownloadStagingManager?
0x197ef76a4  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Configuration.assetDownloadStagingManager : __C.CKAssetDownloadStagingManager?
0x197e94668  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.assetDownloadStagingManager.setter : __C.CKAssetDownloadStagingManager?
0x197e944d4  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.xpcActivityCriteriaOverrides.modify : __C.OS_xpc_object?
0x197e9445c  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.xpcActivityCriteriaOverrides.getter : __C.OS_xpc_object?
0x1e0c41920  __DATA_CONST,__const  property descriptor for CloudKit.CKSyncEngine.Configuration.xpcActivityCriteriaOverrides : __C.OS_xpc_object?
0x197e944d0  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.xpcActivityCriteriaOverrides.setter : __C.OS_xpc_object?
0x197e94620  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.allowFetchAndModifyConcurrently.modify : Swift.Bool
0x197e94610  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.allowFetchAndModifyConcurrently.getter : Swift.Bool
0x197ef76a0  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Configuration.allowFetchAndModifyConcurrently : Swift.Bool
0x197e94618  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.allowFetchAndModifyConcurrently.setter : Swift.Bool
0x197c37830  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.init(database: __C.CKDatabase, stateSerialization: CloudKit.CKSyncEngine.State.Serialization?, delegate: CloudKit.CKSyncEngineDelegate) -> CloudKit.CKSyncEngine.Configuration
0x197e941e8  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.database.modify : __C.CKDatabase
0x197e941b4  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.database.getter : __C.CKDatabase
0x197ef7680  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Configuration.database : __C.CKDatabase
0x197e941bc  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.database.setter : __C.CKDatabase
0x197e942c4  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.delegate.modify : CloudKit.CKSyncEngineDelegate
0x197e94268  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.delegate.getter : CloudKit.CKSyncEngineDelegate
0x197ef7688  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Configuration.delegate : CloudKit.CKSyncEngineDelegate
0x197e94290  __TEXT,__text  CloudKit.CKSyncEngine.Configuration.delegate.setter : CloudKit.CKSyncEngineDelegate
0x197c39638  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Configuration
0x197f29754  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Configuration
0x1e3ca9030  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Configuration
0x197ef7658  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Configuration : Swift.CustomStringConvertible in CloudKit
0x197e9d6e8  __TEXT,__text  CloudKit.CKSyncEngine.PendingAssetSync.description.getter : Swift.String
0x197ef9720  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.PendingAssetSync.description : Swift.String
0x197e9d784  __TEXT,__text  static CloudKit.CKSyncEngine.PendingAssetSync.== infix(CloudKit.CKSyncEngine.PendingAssetSync, CloudKit.CKSyncEngine.PendingAssetSync) -> Swift.Bool
0x197e9d810  __TEXT,__text  CloudKit.CKSyncEngine.PendingAssetSync.hash(into: inout Swift.Hasher) -> ()
0x197ef9b54  __TEXT,__const  enum case for CloudKit.CKSyncEngine.PendingAssetSync.fetch(CloudKit.CKSyncEngine.PendingAssetSync.Type) -> ((extension in CloudKit):__C.CKAsset.ID) -> CloudKit.CKSyncEngine.PendingAssetSync
0x197e9d8e0  __TEXT,__text  CloudKit.CKSyncEngine.PendingAssetSync.hashValue.getter : Swift.Int
0x197ef9720  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.PendingAssetSync.hashValue : Swift.Int
0x197e9db9c  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.PendingAssetSync
0x197f29b80  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.PendingAssetSync
0x1e3ca8fb8  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.PendingAssetSync
0x197ef9690  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.PendingAssetSync : Swift.Hashable in CloudKit
0x197ef96f8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.PendingAssetSync : Swift.Equatable in CloudKit
0x197ef96d0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.PendingAssetSync : Swift.CustomStringConvertible in CloudKit
0x197e8d6dc  __TEXT,__text  CloudKit.CKSyncEngine.cancelOperations() async -> ()
0x197ef7318  __TEXT,__const  async function pointer to CloudKit.CKSyncEngine.cancelOperations() async -> ()
0x197f29d48  __TEXT,__constg_swiftt  protocol descriptor for CloudKit.CKSyncEngine.ProgressReporting
0x197ea77a4  __TEXT,__text  dispatch thunk of CloudKit.CKSyncEngine.ProgressReporting.progress.getter : __C.NSProgress
0x197f29d60  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSyncEngine.ProgressReporting.progress.getter : __C.NSProgress
0x197f29d58  __TEXT,__constg_swiftt  protocol requirements base descriptor for CloudKit.CKSyncEngine.ProgressReporting
0x197ea0a2c  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsContext.description.getter : Swift.String
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchAssetsContext.description : Swift.String
0x197ea0258  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsContext.reason.getter : CloudKit.CKSyncEngine.SyncReason
0x197efa080  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchAssetsContext.reason : CloudKit.CKSyncEngine.SyncReason
0x197ea025c  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsContext.options.getter : CloudKit.CKSyncEngine.FetchAssetsOptions
0x197efa084  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchAssetsContext.options : CloudKit.CKSyncEngine.FetchAssetsOptions
0x197ea7794  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.FetchAssetsContext
0x197f29d2c  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.FetchAssetsContext
0x1e3ca8f20  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.FetchAssetsContext
0x197efa020  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.FetchAssetsContext : Swift.CustomStringConvertible in CloudKit
0x197ea0524  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsOptions.description.getter : Swift.String
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchAssetsOptions.description : Swift.String
0x197ea0164  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsOptions.operationGroup.modify : __C.CKOperationGroup
0x197e9e518  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsOptions.operationGroup.getter : __C.CKOperationGroup
0x1e0c419d0  __DATA_CONST,__const  property descriptor for CloudKit.CKSyncEngine.FetchAssetsOptions.operationGroup : __C.CKOperationGroup
0x197ea011c  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsOptions.operationGroup.setter : __C.CKOperationGroup
0x197ea0620  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.description.getter : Swift.String
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.description : Swift.String
0x197efa674  __TEXT,__const  enum case for CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.allExcludingZoneIDs(CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.Type) -> ([__C.CKRecordZoneID]) -> CloudKit.CKSyncEngine.FetchAssetsOptions.Scope
0x197efa67c  __TEXT,__const  enum case for CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.allExcludingRecordIDs(CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.Type) -> ([__C.CKRecordID]) -> CloudKit.CKSyncEngine.FetchAssetsOptions.Scope
0x197efa684  __TEXT,__const  enum case for CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.all(CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.Type) -> CloudKit.CKSyncEngine.FetchAssetsOptions.Scope
0x197efa670  __TEXT,__const  enum case for CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.zoneIDs(CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.Type) -> ([__C.CKRecordZoneID]) -> CloudKit.CKSyncEngine.FetchAssetsOptions.Scope
0x197efa680  __TEXT,__const  enum case for CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.assetIDs(CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.Type) -> ([(extension in CloudKit):__C.CKAsset.ID]) -> CloudKit.CKSyncEngine.FetchAssetsOptions.Scope
0x197e9fe70  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.contains(__C.CKRecordID) -> Swift.Bool
0x197e9fe18  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.contains(__C.CKRecordZoneID) -> Swift.Bool
0x197e9e7bc  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.contains((extension in CloudKit):__C.CKAsset.ID) -> Swift.Bool
0x197efa678  __TEXT,__const  enum case for CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.recordIDs(CloudKit.CKSyncEngine.FetchAssetsOptions.Scope.Type) -> ([__C.CKRecordID]) -> CloudKit.CKSyncEngine.FetchAssetsOptions.Scope
0x197ea7708  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.FetchAssetsOptions.Scope
0x197f29d10  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.FetchAssetsOptions.Scope
0x1e3ca8ea8  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.FetchAssetsOptions.Scope
0x197ef9ff8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.FetchAssetsOptions.Scope : Swift.CustomStringConvertible in CloudKit
0x197e9eb40  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsOptions.init(scope: CloudKit.CKSyncEngine.FetchAssetsOptions.Scope, operationGroup: __C.CKOperationGroup?) -> CloudKit.CKSyncEngine.FetchAssetsOptions
0x197ea0030  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsOptions.scope.modify : CloudKit.CKSyncEngine.FetchAssetsOptions.Scope
0x197e9ff50  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsOptions.scope.getter : CloudKit.CKSyncEngine.FetchAssetsOptions.Scope
0x1e0c419c0  __DATA_CONST,__const  property descriptor for CloudKit.CKSyncEngine.FetchAssetsOptions.scope : CloudKit.CKSyncEngine.FetchAssetsOptions.Scope
0x197e9ffa4  __TEXT,__text  CloudKit.CKSyncEngine.FetchAssetsOptions.scope.setter : CloudKit.CKSyncEngine.FetchAssetsOptions.Scope
0x197ea765c  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.FetchAssetsOptions
0x197f29cf4  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.FetchAssetsOptions
0x1e3ca8e10  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.FetchAssetsOptions
0x197ef9fd0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.FetchAssetsOptions : Swift.CustomStringConvertible in CloudKit
0x197ba879c  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesContext.description.getter : Swift.String
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.SendChangesContext.description : Swift.String
0x197e9fc08  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesContext.invocationID.getter : Swift.String
0x197efa07c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.SendChangesContext.invocationID : Swift.String
0x197e9fbcc  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesContext.reason.getter : CloudKit.CKSyncEngine.SyncReason
0x197efa070  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.SendChangesContext.reason : CloudKit.CKSyncEngine.SyncReason
0x197e9fbd4  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesContext.options.getter : CloudKit.CKSyncEngine.SendChangesOptions
0x197efa078  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.SendChangesContext.options : CloudKit.CKSyncEngine.SendChangesOptions
0x197ea04f0  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesContext.SyncPhase.description.getter : Swift.String
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.SendChangesContext.SyncPhase.description : Swift.String
0x197e9fc60  __TEXT,__text  static CloudKit.CKSyncEngine.SendChangesContext.SyncPhase.databaseChangeBatch.getter : CloudKit.CKSyncEngine.SendChangesContext.SyncPhase
0x197efa06c  __TEXT,__const  property descriptor for static CloudKit.CKSyncEngine.SendChangesContext.SyncPhase.databaseChangeBatch : CloudKit.CKSyncEngine.SendChangesContext.SyncPhase
0x197e9fca4  __TEXT,__text  static CloudKit.CKSyncEngine.SendChangesContext.SyncPhase.recordZoneChangeBatch.getter : CloudKit.CKSyncEngine.SendChangesContext.SyncPhase
0x197efa06c  __TEXT,__const  property descriptor for static CloudKit.CKSyncEngine.SendChangesContext.SyncPhase.recordZoneChangeBatch : CloudKit.CKSyncEngine.SendChangesContext.SyncPhase
0x197e9fcbc  __TEXT,__text  static CloudKit.CKSyncEngine.SendChangesContext.SyncPhase.== infix(CloudKit.CKSyncEngine.SendChangesContext.SyncPhase, CloudKit.CKSyncEngine.SendChangesContext.SyncPhase) -> Swift.Bool
0x197e9fcec  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesContext.SyncPhase.hash(into: inout Swift.Hasher) -> ()
0x197e9fcf4  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesContext.SyncPhase.hashValue.getter : Swift.Int
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.SendChangesContext.SyncPhase.hashValue : Swift.Int
0x197ea74f4  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.SendChangesContext.SyncPhase
0x197f29cbc  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.SendChangesContext.SyncPhase
0x1e3ca8d90  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.SendChangesContext.SyncPhase
0x197ef9d48  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.SendChangesContext.SyncPhase : Swift.Hashable in CloudKit
0x197ef9d20  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.SendChangesContext.SyncPhase : Swift.Equatable in CloudKit
0x197ef9f58  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.SendChangesContext.SyncPhase : Swift.CustomStringConvertible in CloudKit
0x197e9fbd0  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesContext.syncPhase.getter : CloudKit.CKSyncEngine.SendChangesContext.SyncPhase?
0x197efa074  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.SendChangesContext.syncPhase : CloudKit.CKSyncEngine.SendChangesContext.SyncPhase?
0x197ea74e4  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.SendChangesContext
0x197f29ca0  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.SendChangesContext
0x1e3ca8d08  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.SendChangesContext
0x197ef9eb8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.SendChangesContext : Swift.CustomStringConvertible in CloudKit
0x197ba8938  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesOptions.description.getter : Swift.String
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.SendChangesOptions.description : Swift.String
0x197e9fa18  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesOptions.operationGroup.modify : __C.CKOperationGroup
0x197ea7b00  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesOptions.operationGroup.getter : __C.CKOperationGroup
0x1e0c419b0  __DATA_CONST,__const  property descriptor for CloudKit.CKSyncEngine.SendChangesOptions.operationGroup : __C.CKOperationGroup
0x197e9f9d0  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesOptions.operationGroup.setter : __C.CKOperationGroup
0x197ba8ac4  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesOptions.Scope.description.getter : Swift.String
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.SendChangesOptions.Scope.description : Swift.String
0x197efa400  __TEXT,__const  enum case for CloudKit.CKSyncEngine.SendChangesOptions.Scope.allExcluding(CloudKit.CKSyncEngine.SendChangesOptions.Scope.Type) -> ([__C.CKRecordZoneID]) -> CloudKit.CKSyncEngine.SendChangesOptions.Scope
0x197ea03c8  __TEXT,__text  static CloudKit.CKSyncEngine.SendChangesOptions.Scope.== infix(CloudKit.CKSyncEngine.SendChangesOptions.Scope, CloudKit.CKSyncEngine.SendChangesOptions.Scope) -> Swift.Bool
0x197efa40c  __TEXT,__const  enum case for CloudKit.CKSyncEngine.SendChangesOptions.Scope.all(CloudKit.CKSyncEngine.SendChangesOptions.Scope.Type) -> CloudKit.CKSyncEngine.SendChangesOptions.Scope
0x197efa404  __TEXT,__const  enum case for CloudKit.CKSyncEngine.SendChangesOptions.Scope.zoneIDs(CloudKit.CKSyncEngine.SendChangesOptions.Scope.Type) -> ([__C.CKRecordZoneID]) -> CloudKit.CKSyncEngine.SendChangesOptions.Scope
0x197e9fa70  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesOptions.Scope.contains(CloudKit.CKSyncEngine.PendingRecordZoneChange) -> Swift.Bool
0x197e9ec4c  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesOptions.Scope.contains(__C.CKRecordID) -> Swift.Bool
0x197efa408  __TEXT,__const  enum case for CloudKit.CKSyncEngine.SendChangesOptions.Scope.recordIDs(CloudKit.CKSyncEngine.SendChangesOptions.Scope.Type) -> ([__C.CKRecordID]) -> CloudKit.CKSyncEngine.SendChangesOptions.Scope
0x197ea7448  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.SendChangesOptions.Scope
0x197f29c84  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.SendChangesOptions.Scope
0x1e3ca8c90  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.SendChangesOptions.Scope
0x197ef9e90  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.SendChangesOptions.Scope : Swift.Equatable in CloudKit
0x197ef9f80  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.SendChangesOptions.Scope : Swift.CustomStringConvertible in CloudKit
0x197ba6760  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesOptions.init(scope: CloudKit.CKSyncEngine.SendChangesOptions.Scope, operationGroup: __C.CKOperationGroup?) -> CloudKit.CKSyncEngine.SendChangesOptions
0x197e9f934  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesOptions.scope.modify : CloudKit.CKSyncEngine.SendChangesOptions.Scope
0x197ea7afc  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesOptions.scope.getter : CloudKit.CKSyncEngine.SendChangesOptions.Scope
0x1e0c419a0  __DATA_CONST,__const  property descriptor for CloudKit.CKSyncEngine.SendChangesOptions.scope : CloudKit.CKSyncEngine.SendChangesOptions.Scope
0x197e9f904  __TEXT,__text  CloudKit.CKSyncEngine.SendChangesOptions.scope.setter : CloudKit.CKSyncEngine.SendChangesOptions.Scope
0x197ea739c  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.SendChangesOptions
0x197f29c68  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.SendChangesOptions
0x1e3ca8bf8  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.SendChangesOptions
0x197ef9e68  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.SendChangesOptions : Swift.CustomStringConvertible in CloudKit
0x197b98c84  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesContext.description.getter : Swift.String
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesContext.description : Swift.String
0x197e9f788  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesContext.invocationID.getter : Swift.String
0x197efa068  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesContext.invocationID : Swift.String
0x197e9f72c  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesContext.reason.getter : CloudKit.CKSyncEngine.SyncReason
0x197efa05c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesContext.reason : CloudKit.CKSyncEngine.SyncReason
0x197e9f734  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesContext.options.getter : CloudKit.CKSyncEngine.FetchChangesOptions
0x197efa064  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesContext.options : CloudKit.CKSyncEngine.FetchChangesOptions
0x197e9f8ec  __TEXT,__text  static CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase.recordZoneChanges.getter : CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase
0x197efa06c  __TEXT,__const  property descriptor for static CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase.recordZoneChanges : CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase
0x197e9f8bc  __TEXT,__text  static CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase.databaseChanges.getter : CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase
0x197efa06c  __TEXT,__const  property descriptor for static CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase.databaseChanges : CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase
0x197ea7af8  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase.description.getter : Swift.String
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase.description : Swift.String
0x197ea7b1c  __TEXT,__text  static CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase.== infix(CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase, CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase) -> Swift.Bool
0x197ea7b10  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase.hash(into: inout Swift.Hasher) -> ()
0x197ea7b30  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase.hashValue.getter : Swift.Int
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase.hashValue : Swift.Int
0x197ea738c  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase
0x197f29c4c  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase
0x1e3ca8b78  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase
0x197ef9ce0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase : Swift.Hashable in CloudKit
0x197ef9cb8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase : Swift.Equatable in CloudKit
0x197ef9f30  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase : Swift.CustomStringConvertible in CloudKit
0x197e9f730  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesContext.syncPhase.getter : CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase?
0x197efa060  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesContext.syncPhase : CloudKit.CKSyncEngine.FetchChangesContext.SyncPhase?
0x197ea737c  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.FetchChangesContext
0x197f29c30  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.FetchChangesContext
0x1e3ca8af0  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.FetchChangesContext
0x197ef9ee0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.FetchChangesContext : Swift.CustomStringConvertible in CloudKit
0x197e9f458  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.forceFetchChanges.modify : Swift.Bool
0x197e9f448  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.forceFetchChanges.getter : Swift.Bool
0x197efa058  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.forceFetchChanges : Swift.Bool
0x197e9f450  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.forceFetchChanges.setter : Swift.Bool
0x197b99cd0  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.description.getter : Swift.String
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.description : Swift.String
0x197e9f258  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.operationGroup.modify : __C.CKOperationGroup
0x197e9ea14  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.operationGroup.getter : __C.CKOperationGroup
0x1e0c41990  __DATA_CONST,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.operationGroup : __C.CKOperationGroup
0x197e9f214  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.operationGroup.setter : __C.CKOperationGroup
0x197e9eb34  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration.init(shouldFetchAssetContents: Swift.Bool, resultsLimit: Swift.Int) -> CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration
0x197e9f428  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration.shouldFetchAssetContents.modify : Swift.Bool
0x197e9f418  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration.shouldFetchAssetContents.getter : Swift.Bool
0x197efa054  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration.shouldFetchAssetContents : Swift.Bool
0x197e9f420  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration.shouldFetchAssetContents.setter : Swift.Bool
0x197ea033c  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration.description.getter : Swift.String
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration.description : Swift.String
0x197e9ed40  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration.init() -> CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration
0x197ea72ac  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration
0x197f29bf8  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration
0x1e3ca8a48  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration
0x197ef9e40  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration : Swift.CustomStringConvertible in CloudKit
0x197e9f35c  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.prioritizedZoneIDs.modify : [__C.CKRecordZoneID]
0x197e9f328  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.prioritizedZoneIDs.getter : [__C.CKRecordZoneID]
0x197efa048  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.prioritizedZoneIDs : [__C.CKRecordZoneID]
0x197e9f330  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.prioritizedZoneIDs.setter : [__C.CKRecordZoneID]
0x197e9f3b0  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.zoneConfigurations.modify : [__C.CKRecordZoneID : CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration]
0x197e9f37c  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.zoneConfigurations.getter : [__C.CKRecordZoneID : CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration]
0x197efa04c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.zoneConfigurations : [__C.CKRecordZoneID : CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration]
0x197e9f384  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.zoneConfigurations.setter : [__C.CKRecordZoneID : CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration]
0x197e9f3f8  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.defaultZoneConfiguration.modify : CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration
0x197e9f3d0  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.defaultZoneConfiguration.getter : CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration
0x197efa050  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.defaultZoneConfiguration : CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration
0x197e9f3e4  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.defaultZoneConfiguration.setter : CloudKit.CKSyncEngine.FetchChangesOptions.ZoneConfiguration
0x197b99a94  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.Scope.description.getter : Swift.String
0x197efa06c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.Scope.description : Swift.String
0x197efa1d0  __TEXT,__const  enum case for CloudKit.CKSyncEngine.FetchChangesOptions.Scope.allExcluding(CloudKit.CKSyncEngine.FetchChangesOptions.Scope.Type) -> ([__C.CKRecordZoneID]) -> CloudKit.CKSyncEngine.FetchChangesOptions.Scope
0x197ea0294  __TEXT,__text  static CloudKit.CKSyncEngine.FetchChangesOptions.Scope.== infix(CloudKit.CKSyncEngine.FetchChangesOptions.Scope, CloudKit.CKSyncEngine.FetchChangesOptions.Scope) -> Swift.Bool
0x197efa1d8  __TEXT,__const  enum case for CloudKit.CKSyncEngine.FetchChangesOptions.Scope.all(CloudKit.CKSyncEngine.FetchChangesOptions.Scope.Type) -> CloudKit.CKSyncEngine.FetchChangesOptions.Scope
0x197efa1d4  __TEXT,__const  enum case for CloudKit.CKSyncEngine.FetchChangesOptions.Scope.zoneIDs(CloudKit.CKSyncEngine.FetchChangesOptions.Scope.Type) -> ([__C.CKRecordZoneID]) -> CloudKit.CKSyncEngine.FetchChangesOptions.Scope
0x197e9ea18  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.Scope.contains(__C.CKRecordZoneID) -> Swift.Bool
0x197ea72d4  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.FetchChangesOptions.Scope
0x197f29c14  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.Scope
0x1e3ca89d0  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.FetchChangesOptions.Scope
0x197ef9e18  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.Scope : Swift.Equatable in CloudKit
0x197ef9fa8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.Scope : Swift.CustomStringConvertible in CloudKit
0x197e9e8d0  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.init(scope: CloudKit.CKSyncEngine.FetchChangesOptions.Scope, operationGroup: __C.CKOperationGroup?) -> CloudKit.CKSyncEngine.FetchChangesOptions
0x197e9f17c  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.scope.modify : CloudKit.CKSyncEngine.FetchChangesOptions.Scope
0x197e9f130  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.scope.getter : CloudKit.CKSyncEngine.FetchChangesOptions.Scope
0x1e0c41980  __DATA_CONST,__const  property descriptor for CloudKit.CKSyncEngine.FetchChangesOptions.scope : CloudKit.CKSyncEngine.FetchChangesOptions.Scope
0x197e9ed50  __TEXT,__text  CloudKit.CKSyncEngine.FetchChangesOptions.scope.setter : CloudKit.CKSyncEngine.FetchChangesOptions.Scope
0x197ea7210  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.FetchChangesOptions
0x197f29bdc  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.FetchChangesOptions
0x1e3ca8920  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.FetchChangesOptions
0x197ef9df0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.FetchChangesOptions : Swift.CustomStringConvertible in CloudKit
0x197ef98fc  __TEXT,__const  enum case for CloudKit.CKSyncEngine.PendingDatabaseChange.deleteZone(CloudKit.CKSyncEngine.PendingDatabaseChange.Type) -> (__C.CKRecordZoneID) -> CloudKit.CKSyncEngine.PendingDatabaseChange
0x197e9d510  __TEXT,__text  CloudKit.CKSyncEngine.PendingDatabaseChange.description.getter : Swift.String
0x197ef9720  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.PendingDatabaseChange.description : Swift.String
0x197e9d44c  __TEXT,__text  static CloudKit.CKSyncEngine.PendingDatabaseChange.== infix(CloudKit.CKSyncEngine.PendingDatabaseChange, CloudKit.CKSyncEngine.PendingDatabaseChange) -> Swift.Bool
0x197e9d5c4  __TEXT,__text  CloudKit.CKSyncEngine.PendingDatabaseChange.hash(into: inout Swift.Hasher) -> ()
0x197ef98f8  __TEXT,__const  enum case for CloudKit.CKSyncEngine.PendingDatabaseChange.saveZone(CloudKit.CKSyncEngine.PendingDatabaseChange.Type) -> (__C.CKRecordZone) -> CloudKit.CKSyncEngine.PendingDatabaseChange
0x197e9d614  __TEXT,__text  CloudKit.CKSyncEngine.PendingDatabaseChange.hashValue.getter : Swift.Int
0x197ef9720  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.PendingDatabaseChange.hashValue : Swift.Int
0x197e9db8c  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.PendingDatabaseChange
0x197f29b64  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.PendingDatabaseChange
0x1e3ca88a8  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.PendingDatabaseChange
0x197ef9600  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.PendingDatabaseChange : Swift.Hashable in CloudKit
0x197ef9668  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.PendingDatabaseChange : Swift.Equatable in CloudKit
0x197ef9640  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.PendingDatabaseChange : Swift.CustomStringConvertible in CloudKit
0x197e98ee0  __TEXT,__text  CloudKit.CKSyncEngine.RecordZoneChangeBatch.atomicByZone.modify : Swift.Bool
0x197e98ed0  __TEXT,__text  CloudKit.CKSyncEngine.RecordZoneChangeBatch.atomicByZone.getter : Swift.Bool
0x197ef94c0  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.RecordZoneChangeBatch.atomicByZone : Swift.Bool
0x197e98ed8  __TEXT,__text  CloudKit.CKSyncEngine.RecordZoneChangeBatch.atomicByZone.setter : Swift.Bool
0x197e9ad1c  __TEXT,__text  CloudKit.CKSyncEngine.RecordZoneChangeBatch.description.getter : Swift.String
0x197ef94c4  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.RecordZoneChangeBatch.description : Swift.String
0x197e99cb0  __TEXT,__text  CloudKit.CKSyncEngine.RecordZoneChangeBatch.init(recordsToSave: [__C.CKRecord], recordIDsToDelete: [__C.CKRecordID], atomicByZone: Swift.Bool) -> CloudKit.CKSyncEngine.RecordZoneChangeBatch
0x197e98e5c  __TEXT,__text  CloudKit.CKSyncEngine.RecordZoneChangeBatch.recordsToSave.modify : [__C.CKRecord]
0x197e98e28  __TEXT,__text  CloudKit.CKSyncEngine.RecordZoneChangeBatch.recordsToSave.getter : [__C.CKRecord]
0x197ef94b8  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.RecordZoneChangeBatch.recordsToSave : [__C.CKRecord]
0x197e98e30  __TEXT,__text  CloudKit.CKSyncEngine.RecordZoneChangeBatch.recordsToSave.setter : [__C.CKRecord]
0x197e9a668  __TEXT,__text  CloudKit.CKSyncEngine.RecordZoneChangeBatch.init(pendingChanges: [CloudKit.CKSyncEngine.PendingRecordZoneChange], synchronousRecordProvider: @Sendable (__C.CKRecordID) -> __C.CKRecord?) -> CloudKit.CKSyncEngine.RecordZoneChangeBatch?
0x197e98f00  __TEXT,__text  CloudKit.CKSyncEngine.RecordZoneChangeBatch.init(pendingChanges: [CloudKit.CKSyncEngine.PendingRecordZoneChange], recordProvider: @Sendable (__C.CKRecordID) async -> __C.CKRecord?) async -> CloudKit.CKSyncEngine.RecordZoneChangeBatch?
0x197ef9480  __TEXT,__const  async function pointer to CloudKit.CKSyncEngine.RecordZoneChangeBatch.init(pendingChanges: [CloudKit.CKSyncEngine.PendingRecordZoneChange], recordProvider: @Sendable (__C.CKRecordID) async -> __C.CKRecord?) async -> CloudKit.CKSyncEngine.RecordZoneChangeBatch?
0x197e98eb0  __TEXT,__text  CloudKit.CKSyncEngine.RecordZoneChangeBatch.recordIDsToDelete.modify : [__C.CKRecordID]
0x197e98e7c  __TEXT,__text  CloudKit.CKSyncEngine.RecordZoneChangeBatch.recordIDsToDelete.getter : [__C.CKRecordID]
0x197ef94bc  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.RecordZoneChangeBatch.recordIDsToDelete : [__C.CKRecordID]
0x197e98e84  __TEXT,__text  CloudKit.CKSyncEngine.RecordZoneChangeBatch.recordIDsToDelete.setter : [__C.CKRecordID]
0x197e9b224  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.RecordZoneChangeBatch
0x197f29ac4  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.RecordZoneChangeBatch
0x1e3ca8808  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.RecordZoneChangeBatch
0x197ef9490  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.RecordZoneChangeBatch : Swift.CustomStringConvertible in CloudKit
0x197e8d810  __TEXT,__text  CloudKit.CKSyncEngine.setNeedsToFetchChanges() -> ()
0x197ef9868  __TEXT,__const  enum case for CloudKit.CKSyncEngine.PendingRecordZoneChange.saveRecord(CloudKit.CKSyncEngine.PendingRecordZoneChange.Type) -> (__C.CKRecordID) -> CloudKit.CKSyncEngine.PendingRecordZoneChange
0x197ef986c  __TEXT,__const  enum case for CloudKit.CKSyncEngine.PendingRecordZoneChange.deleteRecord(CloudKit.CKSyncEngine.PendingRecordZoneChange.Type) -> (__C.CKRecordID) -> CloudKit.CKSyncEngine.PendingRecordZoneChange
0x197e9df74  __TEXT,__text  CloudKit.CKSyncEngine.PendingRecordZoneChange.description.getter : Swift.String
0x197ef9720  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.PendingRecordZoneChange.description : Swift.String
0x197e9d398  __TEXT,__text  static CloudKit.CKSyncEngine.PendingRecordZoneChange.== infix(CloudKit.CKSyncEngine.PendingRecordZoneChange, CloudKit.CKSyncEngine.PendingRecordZoneChange) -> Swift.Bool
0x197e9df6c  __TEXT,__text  CloudKit.CKSyncEngine.PendingRecordZoneChange.hash(into: inout Swift.Hasher) -> ()
0x197e9df78  __TEXT,__text  CloudKit.CKSyncEngine.PendingRecordZoneChange.hashValue.getter : Swift.Int
0x197ef9720  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.PendingRecordZoneChange.hashValue : Swift.Int
0x197e9db7c  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.PendingRecordZoneChange
0x197f29b48  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.PendingRecordZoneChange
0x1e3ca8488  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.PendingRecordZoneChange
0x197ef9570  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.PendingRecordZoneChange : Swift.Hashable in CloudKit
0x197ef95d8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.PendingRecordZoneChange : Swift.Equatable in CloudKit
0x197ef95b0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.PendingRecordZoneChange : Swift.CustomStringConvertible in CloudKit
0x197e8da2c  __TEXT,__text  CloudKit.CKSyncEngine.useOpportunisticPushTopic.getter : Swift.Bool
0x197ef7348  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.useOpportunisticPushTopic : Swift.Bool
0x197c2a228  __TEXT,__text  CloudKit.CKSyncEngine.Event.StateUpdate.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.StateUpdate.description : Swift.String
0x197e96264  __TEXT,__text  CloudKit.CKSyncEngine.Event.StateUpdate.stateSerialization.getter : CloudKit.CKSyncEngine.State.Serialization
0x197ef7d4c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.StateUpdate.stateSerialization : CloudKit.CKSyncEngine.State.Serialization
0x197e98174  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.StateUpdate
0x197f29894  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.StateUpdate
0x1e3ca83f0  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.StateUpdate
0x197ef7a2c  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.StateUpdate : Swift.CustomStringConvertible in CloudKit
0x197b9decc  __TEXT,__text  CloudKit.CKSyncEngine.Event.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.description : Swift.String
0x197ef8868  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.stateUpdate(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.StateUpdate) -> CloudKit.CKSyncEngine.Event
0x197e9741c  __TEXT,__text  CloudKit.CKSyncEngine.Event.FetchedAsset.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.FetchedAsset.description : Swift.String
0x197e96450  __TEXT,__text  CloudKit.CKSyncEngine.Event.FetchedAsset.asset.getter : __C.CKAsset
0x197ef7dc8  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.FetchedAsset.asset : __C.CKAsset
0x197e985c8  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.FetchedAsset
0x197f29a70  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.FetchedAsset
0x1e3ca8370  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.FetchedAsset
0x197ef7cd4  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.FetchedAsset : Swift.CustomStringConvertible in CloudKit
0x197ef88a0  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.fetchedAsset(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.FetchedAsset) -> CloudKit.CKSyncEngine.Event
0x197ef8a8c  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.AccountChange.ChangeType.switchAccounts(CloudKit.CKSyncEngine.Event.AccountChange.ChangeType.Type) -> (__C.CKRecordID, __C.CKRecordID) -> CloudKit.CKSyncEngine.Event.AccountChange.ChangeType
0x197e97640  __TEXT,__text  static CloudKit.CKSyncEngine.Event.AccountChange.ChangeType.== infix(CloudKit.CKSyncEngine.Event.AccountChange.ChangeType, CloudKit.CKSyncEngine.Event.AccountChange.ChangeType) -> Swift.Bool
0x197ef8a84  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.AccountChange.ChangeType.signIn(CloudKit.CKSyncEngine.Event.AccountChange.ChangeType.Type) -> (__C.CKRecordID) -> CloudKit.CKSyncEngine.Event.AccountChange.ChangeType
0x197ef8a88  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.AccountChange.ChangeType.signOut(CloudKit.CKSyncEngine.Event.AccountChange.ChangeType.Type) -> (__C.CKRecordID) -> CloudKit.CKSyncEngine.Event.AccountChange.ChangeType
0x197e98234  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.AccountChange.ChangeType
0x197f298cc  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.AccountChange.ChangeType
0x1e3ca82f8  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.AccountChange.ChangeType
0x197ef7a7c  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.AccountChange.ChangeType : Swift.Equatable in CloudKit
0x197e96270  __TEXT,__text  CloudKit.CKSyncEngine.Event.AccountChange.changeType.getter : CloudKit.CKSyncEngine.Event.AccountChange.ChangeType
0x197ef7d50  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.AccountChange.changeType : CloudKit.CKSyncEngine.Event.AccountChange.ChangeType
0x197e9658c  __TEXT,__text  CloudKit.CKSyncEngine.Event.AccountChange.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.AccountChange.description : Swift.String
0x197e98198  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.AccountChange
0x197f298b0  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.AccountChange
0x1e3ca8260  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.AccountChange
0x197ef7a54  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.AccountChange : Swift.CustomStringConvertible in CloudKit
0x197e97490  __TEXT,__text  CloudKit.CKSyncEngine.Event.DidFetchAsset.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.DidFetchAsset.description : Swift.String
0x197e96498  __TEXT,__text  CloudKit.CKSyncEngine.Event.DidFetchAsset.error.getter : __C_Synthesized.related decl 'e' for CKErrorCode?
0x197ef7dd0  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.DidFetchAsset.error : __C_Synthesized.related decl 'e' for CKErrorCode?
0x197e96454  __TEXT,__text  CloudKit.CKSyncEngine.Event.DidFetchAsset.assetID.getter : (extension in CloudKit):__C.CKAsset.ID
0x197ef7dcc  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.DidFetchAsset.assetID : (extension in CloudKit):__C.CKAsset.ID
0x197e98670  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.DidFetchAsset
0x197f29a8c  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.DidFetchAsset
0x1e3ca81e0  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.DidFetchAsset
0x197ef7cfc  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.DidFetchAsset : Swift.CustomStringConvertible in CloudKit
0x197ef886c  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.accountChange(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.AccountChange) -> CloudKit.CKSyncEngine.Event
0x197ef88a4  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.didFetchAsset(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.DidFetchAsset) -> CloudKit.CKSyncEngine.Event
0x197e97550  __TEXT,__text  CloudKit.CKSyncEngine.Event.DidFetchAssets.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.DidFetchAssets.description : Swift.String
0x197e96510  __TEXT,__text  CloudKit.CKSyncEngine.Event.DidFetchAssets.error.getter : __C_Synthesized.related decl 'e' for CKErrorCode?
0x197ef7dd8  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.DidFetchAssets.error : __C_Synthesized.related decl 'e' for CKErrorCode?
0x197e964c0  __TEXT,__text  CloudKit.CKSyncEngine.Event.DidFetchAssets.context.getter : CloudKit.CKSyncEngine.FetchAssetsContext
0x197ef7dd4  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.DidFetchAssets.context : CloudKit.CKSyncEngine.FetchAssetsContext
0x197e9870c  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.DidFetchAssets
0x197f29aa8  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.DidFetchAssets
0x1e3ca8160  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.DidFetchAssets
0x197ef7d24  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.DidFetchAssets : Swift.CustomStringConvertible in CloudKit
0x197e970a8  __TEXT,__text  CloudKit.CKSyncEngine.Event.DidSendChanges.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.DidSendChanges.description : Swift.String
0x197e96400  __TEXT,__text  CloudKit.CKSyncEngine.Event.DidSendChanges.context.getter : CloudKit.CKSyncEngine.SendChangesContext
0x197ef7db4  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.DidSendChanges.context : CloudKit.CKSyncEngine.SendChangesContext
0x197e98520  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.DidSendChanges
0x197f29a1c  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.DidSendChanges
0x1e3ca80e0  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.DidSendChanges
0x197ef7c5c  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.DidSendChanges : Swift.CustomStringConvertible in CloudKit
0x197e9729c  __TEXT,__text  CloudKit.CKSyncEngine.Event.WillFetchAsset.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.WillFetchAsset.description : Swift.String
0x197e96448  __TEXT,__text  CloudKit.CKSyncEngine.Event.WillFetchAsset.progressReporter.getter : Foundation.ProgressReporter
0x197ef7dc4  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.WillFetchAsset.progressReporter : Foundation.ProgressReporter
0x197e98d18  __TEXT,__text  CloudKit.CKSyncEngine.Event.WillFetchAsset.assetID.getter : (extension in CloudKit):__C.CKAsset.ID
0x197ef7dc0  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.WillFetchAsset.assetID : (extension in CloudKit):__C.CKAsset.ID
0x197e98540  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.WillFetchAsset
0x197f29a54  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.WillFetchAsset
0x1e3ca8060  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.WillFetchAsset
0x197ef7cac  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.WillFetchAsset : Swift.CustomStringConvertible in CloudKit
0x197ef88a8  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.didFetchAssets(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.DidFetchAssets) -> CloudKit.CKSyncEngine.Event
0x197ef8894  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.didSendChanges(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.DidSendChanges) -> CloudKit.CKSyncEngine.Event
0x197ef889c  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.willFetchAsset(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.WillFetchAsset) -> CloudKit.CKSyncEngine.Event
0x197e96ff0  __TEXT,__text  CloudKit.CKSyncEngine.Event.DidFetchChanges.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.DidFetchChanges.description : Swift.String
0x197e963ac  __TEXT,__text  CloudKit.CKSyncEngine.Event.DidFetchChanges.context.getter : CloudKit.CKSyncEngine.FetchChangesContext
0x197ef7dac  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.DidFetchChanges.context : CloudKit.CKSyncEngine.FetchChangesContext
0x197e98464  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.DidFetchChanges
0x197f299e4  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.DidFetchChanges
0x1e3ca7fe0  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.DidFetchChanges
0x197ef7c0c  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.DidFetchChanges : Swift.CustomStringConvertible in CloudKit
0x197e9710c  __TEXT,__text  CloudKit.CKSyncEngine.Event.WillFetchAssets.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.WillFetchAssets.description : Swift.String
0x197e96440  __TEXT,__text  CloudKit.CKSyncEngine.Event.WillFetchAssets.progressReporter.getter : Foundation.ProgressReporter
0x197ef7dbc  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.WillFetchAssets.progressReporter : Foundation.ProgressReporter
0x197e98d58  __TEXT,__text  CloudKit.CKSyncEngine.Event.WillFetchAssets.context.getter : CloudKit.CKSyncEngine.FetchAssetsContext
0x197ef7db8  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.WillFetchAssets.context : CloudKit.CKSyncEngine.FetchAssetsContext
0x197e98530  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.WillFetchAssets
0x197f29a38  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.WillFetchAssets
0x1e3ca7f60  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.WillFetchAssets
0x197ef7c84  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.WillFetchAssets : Swift.CustomStringConvertible in CloudKit
0x197e9704c  __TEXT,__text  CloudKit.CKSyncEngine.Event.WillSendChanges.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.WillSendChanges.description : Swift.String
0x197e98d14  __TEXT,__text  CloudKit.CKSyncEngine.Event.WillSendChanges.context.getter : CloudKit.CKSyncEngine.SendChangesContext
0x197ef7db0  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.WillSendChanges.context : CloudKit.CKSyncEngine.SendChangesContext
0x197e98488  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.WillSendChanges
0x197f29a00  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.WillSendChanges
0x1e3ca7ee0  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.WillSendChanges
0x197ef7c34  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.WillSendChanges : Swift.CustomStringConvertible in CloudKit
0x197ef888c  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.didFetchChanges(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.DidFetchChanges) -> CloudKit.CKSyncEngine.Event
0x197ef8898  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.willFetchAssets(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.WillFetchAssets) -> CloudKit.CKSyncEngine.Event
0x197ef8890  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.willSendChanges(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.WillSendChanges) -> CloudKit.CKSyncEngine.Event
0x197e96dd4  __TEXT,__text  CloudKit.CKSyncEngine.Event.WillFetchChanges.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.WillFetchChanges.description : Swift.String
0x197e98d10  __TEXT,__text  CloudKit.CKSyncEngine.Event.WillFetchChanges.context.getter : CloudKit.CKSyncEngine.FetchChangesContext
0x197ef7d9c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.WillFetchChanges.context : CloudKit.CKSyncEngine.FetchChangesContext
0x197e98328  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.WillFetchChanges
0x197f29990  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.WillFetchChanges
0x1e3ca7e60  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.WillFetchChanges
0x197ef7b94  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.WillFetchChanges : Swift.CustomStringConvertible in CloudKit
0x197ef8880  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.willFetchChanges(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.WillFetchChanges) -> CloudKit.CKSyncEngine.Event
0x197e96364  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentDatabaseChanges.savedZones.getter : [__C.CKRecordZone]
0x197ef7d6c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges.savedZones : [__C.CKRecordZone]
0x197e96938  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentDatabaseChanges.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges.description : Swift.String
0x197e977b8  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave.description : Swift.String
0x197e96378  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave.zone.getter : __C.CKRecordZone
0x197ef7d7c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave.zone : __C.CKRecordZone
0x197e9637c  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave.error.getter : __C_Synthesized.related decl 'e' for CKErrorCode
0x197ef7d80  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave.error : __C_Synthesized.related decl 'e' for CKErrorCode
0x197e98274  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave
0x197f2993c  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave
0x1e3ca7de0  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave
0x197ef7b1c  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave : Swift.CustomStringConvertible in CloudKit
0x197e9636c  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentDatabaseChanges.deletedZoneIDs.getter : [__C.CKRecordZoneID]
0x197ef7d74  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges.deletedZoneIDs : [__C.CKRecordZoneID]
0x197e96368  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentDatabaseChanges.failedZoneSaves.getter : [CloudKit.CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave]
0x197ef7d70  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges.failedZoneSaves : [CloudKit.CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave]
0x197e96370  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentDatabaseChanges.failedZoneDeletes.getter : [__C.CKRecordZoneID : __C_Synthesized.related decl 'e' for CKErrorCode]
0x197ef7d78  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges.failedZoneDeletes : [__C.CKRecordZoneID : __C_Synthesized.related decl 'e' for CKErrorCode]
0x197e98264  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges
0x197f29920  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges
0x1e3ca7d58  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.SentDatabaseChanges
0x197ef7af4  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.SentDatabaseChanges : Swift.CustomStringConvertible in CloudKit
0x197ef8878  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.sentDatabaseChanges(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.SentDatabaseChanges) -> CloudKit.CKSyncEngine.Event
0x197e978bc  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave.description : Swift.String
0x197e98d0c  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave.error.getter : __C_Synthesized.related decl 'e' for CKErrorCode
0x197ef7d98  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave.error : __C_Synthesized.related decl 'e' for CKErrorCode
0x197e98d4c  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave.record.getter : __C.CKRecord
0x197ef7d94  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave.record : __C.CKRecord
0x197e98310  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave
0x197f29974  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave
0x1e3ca7cd8  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave
0x197ef7b6c  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave : Swift.CustomStringConvertible in CloudKit
0x197e98d00  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.failedRecordSaves.getter : [CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave]
0x197ef7d88  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.failedRecordSaves : [CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave]
0x197e98d08  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.failedRecordDeletes.getter : [__C.CKRecordID : __C_Synthesized.related decl 'e' for CKErrorCode]
0x197ef7d90  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.failedRecordDeletes : [__C.CKRecordID : __C_Synthesized.related decl 'e' for CKErrorCode]
0x197e98d04  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.deletedRecordIDs.getter : [__C.CKRecordID]
0x197ef7d8c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.deletedRecordIDs : [__C.CKRecordID]
0x197e96b08  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.description : Swift.String
0x197e98d48  __TEXT,__text  CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.savedRecords.getter : [__C.CKRecord]
0x197ef7d84  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges.savedRecords : [__C.CKRecord]
0x197e98300  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges
0x197f29958  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges
0x1e3ca7c50  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges
0x197ef7b44  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.SentRecordZoneChanges : Swift.CustomStringConvertible in CloudKit
0x197ef887c  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.sentRecordZoneChanges(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.SentRecordZoneChanges) -> CloudKit.CKSyncEngine.Event
0x197e9671c  __TEXT,__text  CloudKit.CKSyncEngine.Event.FetchedDatabaseChanges.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.FetchedDatabaseChanges.description : Swift.String
0x197e96284  __TEXT,__text  CloudKit.CKSyncEngine.Event.FetchedDatabaseChanges.modifications.getter : [(extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification]
0x197ef7d54  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.FetchedDatabaseChanges.modifications : [(extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification]
0x197e96288  __TEXT,__text  CloudKit.CKSyncEngine.Event.FetchedDatabaseChanges.deletions.getter : [(extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion]
0x197ef7d58  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.FetchedDatabaseChanges.deletions : [(extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion]
0x197e98244  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.FetchedDatabaseChanges
0x197f298e8  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.FetchedDatabaseChanges
0x1e3ca7bd0  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.FetchedDatabaseChanges
0x197ef7aa4  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.FetchedDatabaseChanges : Swift.CustomStringConvertible in CloudKit
0x197ef8870  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.fetchedDatabaseChanges(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.FetchedDatabaseChanges) -> CloudKit.CKSyncEngine.Event
0x197e967c8  __TEXT,__text  CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges.description : Swift.String
0x197e9628c  __TEXT,__text  CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges.modifications.getter : [(extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification]
0x197ef7d5c  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges.modifications : [(extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification]
0x197e96294  __TEXT,__text  CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges.zoneModifications.getter : [(extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneModification]
0x197ef7d64  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges.zoneModifications : [(extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneModification]
0x197e96298  __TEXT,__text  CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges.zoneAttributesModifications.getter : [(extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneAttributesModification]
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges.zoneAttributesModifications : [(extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneAttributesModification]
0x197e96290  __TEXT,__text  CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges.deletions.getter : [(extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion]
0x197ef7d60  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges.deletions : [(extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion]
0x197e98254  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges
0x197f29904  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges
0x1e3ca7b48  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges
0x197ef7acc  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges : Swift.CustomStringConvertible in CloudKit
0x197ef8874  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.fetchedRecordZoneChanges(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.FetchedRecordZoneChanges) -> CloudKit.CKSyncEngine.Event
0x197e96eac  __TEXT,__text  CloudKit.CKSyncEngine.Event.DidFetchRecordZoneChanges.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.DidFetchRecordZoneChanges.description : Swift.String
0x197e96384  __TEXT,__text  CloudKit.CKSyncEngine.Event.DidFetchRecordZoneChanges.error.getter : __C_Synthesized.related decl 'e' for CKErrorCode?
0x197ef7da8  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.DidFetchRecordZoneChanges.error : __C_Synthesized.related decl 'e' for CKErrorCode?
0x197e98d50  __TEXT,__text  CloudKit.CKSyncEngine.Event.DidFetchRecordZoneChanges.zoneID.getter : __C.CKRecordZoneID
0x197ef7da4  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.DidFetchRecordZoneChanges.zoneID : __C.CKRecordZoneID
0x197e983c0  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.DidFetchRecordZoneChanges
0x197f299c8  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.DidFetchRecordZoneChanges
0x1e3ca7ac8  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.DidFetchRecordZoneChanges
0x197ef7be4  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.DidFetchRecordZoneChanges : Swift.CustomStringConvertible in CloudKit
0x197ef8888  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.didFetchRecordZoneChanges(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.DidFetchRecordZoneChanges) -> CloudKit.CKSyncEngine.Event
0x197e96e38  __TEXT,__text  CloudKit.CKSyncEngine.Event.WillFetchRecordZoneChanges.description.getter : Swift.String
0x197ef7d68  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.WillFetchRecordZoneChanges.description : Swift.String
0x197e98d54  __TEXT,__text  CloudKit.CKSyncEngine.Event.WillFetchRecordZoneChanges.zoneID.getter : __C.CKRecordZoneID
0x197ef7da0  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.Event.WillFetchRecordZoneChanges.zoneID : __C.CKRecordZoneID
0x197e98338  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event.WillFetchRecordZoneChanges
0x197f299ac  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event.WillFetchRecordZoneChanges
0x1e3ca7a48  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event.WillFetchRecordZoneChanges
0x197ef7bbc  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event.WillFetchRecordZoneChanges : Swift.CustomStringConvertible in CloudKit
0x197ef8884  __TEXT,__const  enum case for CloudKit.CKSyncEngine.Event.willFetchRecordZoneChanges(CloudKit.CKSyncEngine.Event.Type) -> (CloudKit.CKSyncEngine.Event.WillFetchRecordZoneChanges) -> CloudKit.CKSyncEngine.Event
0x197e98164  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.Event
0x197f29878  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.Event
0x1e3ca79d0  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.Event
0x197ef7a04  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.Event : Swift.CustomStringConvertible in CloudKit
0x197e9d1bc  __TEXT,__text  CloudKit.CKSyncEngine.State.Serialization.init(deprecatedData: Foundation.Data) -> CloudKit.CKSyncEngine.State.Serialization
0x197c39778  __TEXT,__text  CloudKit.CKSyncEngine.State.Serialization.init(from: Swift.Decoder) throws -> CloudKit.CKSyncEngine.State.Serialization
0x197e9d224  __TEXT,__text  CloudKit.CKSyncEngine.State.Serialization.encode(to: Swift.Encoder) throws -> ()
0x197b89c8c  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.State.Serialization
0x197f29b2c  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.State.Serialization
0x1e3ca78a8  __AUTH_CONST,__const  type metadata for CloudKit.CKSyncEngine.State.Serialization
0x197ef9548  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.State.Serialization : Swift.Encodable in CloudKit
0x197ef9520  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine.State.Serialization : Swift.Decodable in CloudKit
0x197e9b3bc  __TEXT,__text  CloudKit.CKSyncEngine.State.pendingAssetSyncs.getter : [CloudKit.CKSyncEngine.PendingAssetSync]
0x1e0c41960  __DATA_CONST,__const  property descriptor for CloudKit.CKSyncEngine.State.pendingAssetSyncs : [CloudKit.CKSyncEngine.PendingAssetSync]
0x197e9d194  __TEXT,__text  CloudKit.CKSyncEngine.State.serverChangeToken(for: __C.CKRecordZoneID) -> __C.CKServerChangeToken?
0x197e9b620  __TEXT,__text  CloudKit.CKSyncEngine.State.setServerChangeToken(_: __C.CKServerChangeToken?, for: __C.CKRecordZoneID) -> ()
0x197bdd5c4  __TEXT,__text  CloudKit.CKSyncEngine.State.pendingDatabaseChanges.getter : [CloudKit.CKSyncEngine.PendingDatabaseChange]
0x1e0c41940  __DATA_CONST,__const  property descriptor for CloudKit.CKSyncEngine.State.pendingDatabaseChanges : [CloudKit.CKSyncEngine.PendingDatabaseChange]
0x197c16ff8  __TEXT,__text  CloudKit.CKSyncEngine.State.pendingRecordZoneChanges.getter : [CloudKit.CKSyncEngine.PendingRecordZoneChange]
0x1e0c41930  __DATA_CONST,__const  property descriptor for CloudKit.CKSyncEngine.State.pendingRecordZoneChanges : [CloudKit.CKSyncEngine.PendingRecordZoneChange]
0x197e9cad8  __TEXT,__text  CloudKit.CKSyncEngine.State.hasPendingUntrackedChanges.modify : Swift.Bool
0x197e9b75c  __TEXT,__text  CloudKit.CKSyncEngine.State.hasPendingUntrackedChanges.getter : Swift.Bool
0x1e0c41950  __DATA_CONST,__const  property descriptor for CloudKit.CKSyncEngine.State.hasPendingUntrackedChanges : Swift.Bool
0x197e9c3a4  __TEXT,__text  CloudKit.CKSyncEngine.State.hasPendingUntrackedChanges.setter : Swift.Bool
0x197e9d10c  __TEXT,__text  CloudKit.CKSyncEngine.State.serverChangeTokenForDatabase.modify : __C.CKServerChangeToken?
0x197e9b500  __TEXT,__text  CloudKit.CKSyncEngine.State.serverChangeTokenForDatabase.getter : __C.CKServerChangeToken?
0x1e0c41970  __DATA_CONST,__const  property descriptor for CloudKit.CKSyncEngine.State.serverChangeTokenForDatabase : __C.CKServerChangeToken?
0x197e9b524  __TEXT,__text  CloudKit.CKSyncEngine.State.serverChangeTokenForDatabase.setter : __C.CKServerChangeToken?
0x197bd011c  __TEXT,__text  CloudKit.CKSyncEngine.State.zoneIDsWithUnfetchedServerChanges.getter : [__C.CKRecordZoneID]
0x197ef9720  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.State.zoneIDsWithUnfetchedServerChanges : [__C.CKRecordZoneID]
0x197e9b630  __TEXT,__text  CloudKit.CKSyncEngine.State.add(pendingAssetSyncs: [CloudKit.CKSyncEngine.PendingAssetSync]) -> ()
0x197e9cc98  __TEXT,__text  CloudKit.CKSyncEngine.State.add(pendingDatabaseChanges: [CloudKit.CKSyncEngine.PendingDatabaseChange]) -> ()
0x197e9cb30  __TEXT,__text  CloudKit.CKSyncEngine.State.add(pendingRecordZoneChanges: [CloudKit.CKSyncEngine.PendingRecordZoneChange]) -> ()
0x197e9cdf8  __TEXT,__text  CloudKit.CKSyncEngine.State.remove(pendingAssetSyncs: [CloudKit.CKSyncEngine.PendingAssetSync]) -> ()
0x197e9cd48  __TEXT,__text  CloudKit.CKSyncEngine.State.remove(pendingDatabaseChanges: [CloudKit.CKSyncEngine.PendingDatabaseChange]) -> ()
0x197e9cbe4  __TEXT,__text  CloudKit.CKSyncEngine.State.remove(pendingRecordZoneChanges: [CloudKit.CKSyncEngine.PendingRecordZoneChange]) -> ()
0x197c312d0  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine.State
0x1ee07e110  __DATA_DIRTY,__data  metaclass for CloudKit.CKSyncEngine.State
0x197f29ae0  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine.State
0x197ef9738  __TEXT,__const  class metadata base offset for CloudKit.CKSyncEngine.State
0x197e9db64  __TEXT,__text  method lookup function for CloudKit.CKSyncEngine.State
0x1ee07d9c0  __DATA_DIRTY,__data  type metadata for CloudKit.CKSyncEngine.State
0x197e9d36c  __TEXT,__text  CloudKit.CKSyncEngine.State.__deallocating_deinit
0x197e9d34c  __TEXT,__text  CloudKit.CKSyncEngine.State.deinit
0x197e8cde0  __TEXT,__text  CloudKit.CKSyncEngine.state.getter : CloudKit.CKSyncEngine.State
0x197ef7348  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.state : CloudKit.CKSyncEngine.State
0x197e8cfb0  __TEXT,__text  CloudKit.CKSyncEngine.database.getter : __C.CKDatabase
0x197ef7348  __TEXT,__const  property descriptor for CloudKit.CKSyncEngine.database : __C.CKDatabase
0x197c2bda0  __TEXT,__text  type metadata accessor for CloudKit.CKSyncEngine
0x1ee07e0e8  __DATA_DIRTY,__data  metaclass for CloudKit.CKSyncEngine
0x197f296b8  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSyncEngine
0x197ef7368  __TEXT,__const  class metadata base offset for CloudKit.CKSyncEngine
0x197e8e03c  __TEXT,__text  method lookup function for CloudKit.CKSyncEngine
0x1ee07d940  __DATA_DIRTY,__data  type metadata for CloudKit.CKSyncEngine
0x197e8cfdc  __TEXT,__text  CloudKit.CKSyncEngine.__deallocating_deinit
0x197e8cfbc  __TEXT,__text  CloudKit.CKSyncEngine.deinit
0x197ef7320  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSyncEngine : Swift.CustomStringConvertible in CloudKit
0x197e8cdec  __TEXT,__text  CloudKit.CKSyncEngine.__allocating_init(CloudKit.CKSyncEngine.Configuration) -> CloudKit.CKSyncEngine
0x197e8e054  __TEXT,__text  dispatch thunk of CloudKit.CKSyncEngine.__allocating_init(CloudKit.CKSyncEngine.Configuration) -> CloudKit.CKSyncEngine
0x197f296ec  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSyncEngine.__allocating_init(CloudKit.CKSyncEngine.Configuration) -> CloudKit.CKSyncEngine
0x197bcd608  __TEXT,__text  CloudKit.CKSyncEngine.init(CloudKit.CKSyncEngine.Configuration) -> CloudKit.CKSyncEngine
0x197ec07a4  __TEXT,__text  CloudKit.CKLogLogStats.getter : os.Logger
0x197b84fa4  __TEXT,__text  CloudKit.CKOncePerBoot(Swift.String, @Sendable () -> ()) -> ()
0x197e02bf8  __TEXT,__text  static CloudKit.CKZoneFeature.== infix(CloudKit.CKZoneFeature, CloudKit.CKZoneFeature) -> Swift.Bool
0x197e02c5c  __TEXT,__text  CloudKit.CKZoneFeature.hash(into: inout Swift.Hasher) -> ()
0x197e02be8  __TEXT,__text  CloudKit.CKZoneFeature.init(name: Swift.String, value: Swift.String) -> CloudKit.CKZoneFeature
0x197e02b6c  __TEXT,__text  CloudKit.CKZoneFeature.name.modify : Swift.String
0x197e02b38  __TEXT,__text  CloudKit.CKZoneFeature.name.getter : Swift.String
0x1e0c41370  __DATA_CONST,__const  property descriptor for CloudKit.CKZoneFeature.name : Swift.String
0x197e02b68  __TEXT,__text  CloudKit.CKZoneFeature.name.setter : Swift.String
0x197e02bc8  __TEXT,__text  CloudKit.CKZoneFeature.value.modify : Swift.String
0x197e02b94  __TEXT,__text  CloudKit.CKZoneFeature.value.getter : Swift.String
0x1e0c41380  __DATA_CONST,__const  property descriptor for CloudKit.CKZoneFeature.value : Swift.String
0x197e02bc4  __TEXT,__text  CloudKit.CKZoneFeature.value.setter : Swift.String
0x197e02c60  __TEXT,__text  CloudKit.CKZoneFeature.hashValue.getter : Swift.Int
0x197ef27f4  __TEXT,__const  property descriptor for CloudKit.CKZoneFeature.hashValue : Swift.Int
0x197ef22f8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKZoneFeature : CloudKit.CKFeatureProtocol in CloudKit
0x1e3ca76f0  __AUTH_CONST,__const  protocol witness table for CloudKit.CKZoneFeature : CloudKit.CKFeatureProtocol in CloudKit
0x197bec720  __TEXT,__text  type metadata accessor for CloudKit.CKZoneFeature
0x197f2832c  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKZoneFeature
0x1e3ca76d8  __AUTH_CONST,__const  type metadata for CloudKit.CKZoneFeature
0x197ef23ac  __TEXT,__const  protocol conformance descriptor for CloudKit.CKZoneFeature : Swift.Hashable in CloudKit
0x197ef233c  __TEXT,__const  protocol conformance descriptor for CloudKit.CKZoneFeature : Swift.Comparable in CloudKit
0x197ef2384  __TEXT,__const  protocol conformance descriptor for CloudKit.CKZoneFeature : Swift.Equatable in CloudKit
0x197ef2314  __TEXT,__const  protocol conformance descriptor for CloudKit.CKZoneFeature : Swift.CustomStringConvertible in CloudKit
0x197e09a9c  __TEXT,__text  static CloudKit.CKFieldFeature.== infix(CloudKit.CKFieldFeature, CloudKit.CKFieldFeature) -> Swift.Bool
0x197e09aa0  __TEXT,__text  CloudKit.CKFieldFeature.hash(into: inout Swift.Hasher) -> ()
0x197e09a80  __TEXT,__text  CloudKit.CKFieldFeature.init(name: Swift.String, value: Swift.String) -> CloudKit.CKFieldFeature
0x197e02d00  __TEXT,__text  CloudKit.CKFieldFeature.name.modify : Swift.String
0x197e09a70  __TEXT,__text  CloudKit.CKFieldFeature.name.getter : Swift.String
0x1e0c413b0  __DATA_CONST,__const  property descriptor for CloudKit.CKFieldFeature.name : Swift.String
0x197e09ad0  __TEXT,__text  CloudKit.CKFieldFeature.name.setter : Swift.String
0x197e02db8  __TEXT,__text  CloudKit.CKFieldFeature.value.modify : Swift.String
0x197e09a88  __TEXT,__text  CloudKit.CKFieldFeature.value.getter : Swift.String
0x1e0c413c0  __DATA_CONST,__const  property descriptor for CloudKit.CKFieldFeature.value : Swift.String
0x197e09ad4  __TEXT,__text  CloudKit.CKFieldFeature.value.setter : Swift.String
0x197e09aec  __TEXT,__text  CloudKit.CKFieldFeature.hashValue.getter : Swift.Int
0x197ef27f4  __TEXT,__const  property descriptor for CloudKit.CKFieldFeature.hashValue : Swift.Int
0x197ef24e0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKFieldFeature : CloudKit.CKFeatureProtocol in CloudKit
0x1e3ca7648  __AUTH_CONST,__const  protocol witness table for CloudKit.CKFieldFeature : CloudKit.CKFeatureProtocol in CloudKit
0x197bec740  __TEXT,__text  type metadata accessor for CloudKit.CKFieldFeature
0x197f28364  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKFieldFeature
0x1e3ca7630  __AUTH_CONST,__const  type metadata for CloudKit.CKFieldFeature
0x197ef2594  __TEXT,__const  protocol conformance descriptor for CloudKit.CKFieldFeature : Swift.Hashable in CloudKit
0x197ef2524  __TEXT,__const  protocol conformance descriptor for CloudKit.CKFieldFeature : Swift.Comparable in CloudKit
0x197ef256c  __TEXT,__const  protocol conformance descriptor for CloudKit.CKFieldFeature : Swift.Equatable in CloudKit
0x197ef24fc  __TEXT,__const  protocol conformance descriptor for CloudKit.CKFieldFeature : Swift.CustomStringConvertible in CloudKit
0x197ec07ec  __TEXT,__text  CloudKit.CKLogScheduler.getter : os.Logger
0x197e1906c  __TEXT,__text  CloudKit.CKShareTypeKey.getter : Swift.String
0x197ec0934  __TEXT,__text  CloudKit.CKLogDataRepair.getter : os.Logger
0x197ec0aa8  __TEXT,__text  CloudKit.CKLogMockServer.getter : os.Logger
0x197ec0af0  __TEXT,__text  CloudKit.CKLogReportJunk.getter : os.Logger
0x197e09a94  __TEXT,__text  static CloudKit.CKRecordFeature.== infix(CloudKit.CKRecordFeature, CloudKit.CKRecordFeature) -> Swift.Bool
0x197e09a98  __TEXT,__text  CloudKit.CKRecordFeature.hash(into: inout Swift.Hasher) -> ()
0x197e09a7c  __TEXT,__text  CloudKit.CKRecordFeature.init(name: Swift.String, value: Swift.String) -> CloudKit.CKRecordFeature
0x197e02c64  __TEXT,__text  CloudKit.CKRecordFeature.name.modify : Swift.String
0x197e09a6c  __TEXT,__text  CloudKit.CKRecordFeature.name.getter : Swift.String
0x1e0c41390  __DATA_CONST,__const  property descriptor for CloudKit.CKRecordFeature.name : Swift.String
0x197e09ac0  __TEXT,__text  CloudKit.CKRecordFeature.name.setter : Swift.String
0x197e02c88  __TEXT,__text  CloudKit.CKRecordFeature.value.modify : Swift.String
0x197e09a84  __TEXT,__text  CloudKit.CKRecordFeature.value.getter : Swift.String
0x1e0c413a0  __DATA_CONST,__const  property descriptor for CloudKit.CKRecordFeature.value : Swift.String
0x197e09ac4  __TEXT,__text  CloudKit.CKRecordFeature.value.setter : Swift.String
0x197e09ae8  __TEXT,__text  CloudKit.CKRecordFeature.hashValue.getter : Swift.Int
0x197ef27f4  __TEXT,__const  property descriptor for CloudKit.CKRecordFeature.hashValue : Swift.Int
0x197ef23ec  __TEXT,__const  protocol conformance descriptor for CloudKit.CKRecordFeature : CloudKit.CKFeatureProtocol in CloudKit
0x1e3ca75a0  __AUTH_CONST,__const  protocol witness table for CloudKit.CKRecordFeature : CloudKit.CKFeatureProtocol in CloudKit
0x197bec730  __TEXT,__text  type metadata accessor for CloudKit.CKRecordFeature
0x197f28348  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKRecordFeature
0x1e3ca7588  __AUTH_CONST,__const  type metadata for CloudKit.CKRecordFeature
0x197ef24a0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKRecordFeature : Swift.Hashable in CloudKit
0x197ef2430  __TEXT,__const  protocol conformance descriptor for CloudKit.CKRecordFeature : Swift.Comparable in CloudKit
0x197ef2478  __TEXT,__const  protocol conformance descriptor for CloudKit.CKRecordFeature : Swift.Equatable in CloudKit
0x197ef2408  __TEXT,__const  protocol conformance descriptor for CloudKit.CKRecordFeature : Swift.CustomStringConvertible in CloudKit
0x197e18fcc  __TEXT,__text  CloudKit.CKShareTitleKey.getter : Swift.String
0x197ec4178  __TEXT,__text  CloudKit.CKActivityCreate(_: Swift.StaticString, dso: Swift.UnsafeRawPointer?) -> __C.OS_os_activity
0x197e0d7ec  __TEXT,__text  CloudKit.CKRecordShareKey.getter : Swift.String
0x197ec0474  __TEXT,__text  static CloudKit.__CKLogSubsystem.name.getter : Swift.String
0x197efb110  __TEXT,__const  property descriptor for static CloudKit.__CKLogSubsystem.name : Swift.String
0x197ec0bb0  __TEXT,__text  type metadata accessor for CloudKit.__CKLogSubsystem
0x197f29fac  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.__CKLogSubsystem
0x1e3ca7510  __AUTH_CONST,__const  type metadata for CloudKit.__CKLogSubsystem
0x197f282e8  __TEXT,__constg_swiftt  protocol descriptor for CloudKit.CKFeatureProtocol
0x197e0970c  __TEXT,__text  dispatch thunk of CloudKit.CKFeatureProtocol.init(name: Swift.String, value: Swift.String) -> A
0x197f28324  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKFeatureProtocol.init(name: Swift.String, value: Swift.String) -> A
0x197e096e4  __TEXT,__text  dispatch thunk of CloudKit.CKFeatureProtocol.name.getter : Swift.String
0x197f28314  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKFeatureProtocol.name.getter : Swift.String
0x197e096f8  __TEXT,__text  dispatch thunk of CloudKit.CKFeatureProtocol.value.getter : Swift.String
0x197f2831c  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKFeatureProtocol.value.getter : Swift.String
0x197e028b4  __TEXT,__text  static (extension in CloudKit):CloudKit.CKFeatureProtocol.< infix(A, A) -> Swift.Bool
0x197e02a1c  __TEXT,__text  (extension in CloudKit):CloudKit.CKFeatureProtocol< where A: Swift.CustomStringConvertible>.description.getter : Swift.String
0x197ef27f4  __TEXT,__const  property descriptor for (extension in CloudKit):CloudKit.CKFeatureProtocol< where A: Swift.CustomStringConvertible>.description : Swift.String
0x197f2830c  __TEXT,__constg_swiftt  base conformance descriptor for CloudKit.CKFeatureProtocol: Swift.Comparable
0x197f28304  __TEXT,__constg_swiftt  protocol requirements base descriptor for CloudKit.CKFeatureProtocol
0x197e0d79c  __TEXT,__text  CloudKit.CKRecordParentKey.getter : Swift.String
0x197e18f7c  __TEXT,__text  CloudKit.CKRecordTypeShare.getter : Swift.String
0x197e34784  __TEXT,__text  dispatch thunk of static CloudKit.CKSecureCodingBox.supportsSecureCoding.getter : Swift.Bool
0x197f29020  __TEXT,__constg_swiftt  method descriptor for static CloudKit.CKSecureCodingBox.supportsSecureCoding.getter : Swift.Bool
0x197ef5988  __TEXT,__const  property descriptor for static CloudKit.CKSecureCodingBox.supportsSecureCoding : Swift.Bool
0x197ef5958  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSecureCodingBox : CloudCoreInternal.PropertyDescribable in CloudKit
0x197e342d0  __TEXT,__text  CloudKit.CKSecureCodingBox.description.getter : Swift.String
0x197e340bc  __TEXT,__text  CloudKit.CKSecureCodingBox.propertyDescriptions.getter : [CloudCoreInternal.PropertyDescription]
0x197ef5988  __TEXT,__const  property descriptor for CloudKit.CKSecureCodingBox.propertyDescriptions : [CloudCoreInternal.PropertyDescription]
0x197e33fe4  __TEXT,__text  CloudKit.CKSecureCodingBox.__allocating_init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSecureCodingBox?
0x197e3482c  __TEXT,__text  dispatch thunk of CloudKit.CKSecureCodingBox.__allocating_init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSecureCodingBox?
0x197f29050  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSecureCodingBox.__allocating_init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSecureCodingBox?
0x197c120ec  __TEXT,__text  CloudKit.CKSecureCodingBox.init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSecureCodingBox?
0x197e33f70  __TEXT,__text  CloudKit.CKSecureCodingBox.__allocating_init(sqliteRepresentation: Swift.String) -> CloudKit.CKSecureCodingBox?
0x197e347ec  __TEXT,__text  dispatch thunk of CloudKit.CKSecureCodingBox.__allocating_init(sqliteRepresentation: Swift.String) -> CloudKit.CKSecureCodingBox?
0x197f29040  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSecureCodingBox.__allocating_init(sqliteRepresentation: Swift.String) -> CloudKit.CKSecureCodingBox?
0x197e33f88  __TEXT,__text  CloudKit.CKSecureCodingBox.init(sqliteRepresentation: Swift.String) -> CloudKit.CKSecureCodingBox?
0x197e34800  __TEXT,__text  dispatch thunk of CloudKit.CKSecureCodingBox.sqliteRepresentation() -> Swift.String
0x197f29048  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSecureCodingBox.sqliteRepresentation() -> Swift.String
0x197e33e18  __TEXT,__text  CloudKit.CKSecureCodingBox.__allocating_init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSecureCodingBox?
0x197e347d8  __TEXT,__text  dispatch thunk of CloudKit.CKSecureCodingBox.__allocating_init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSecureCodingBox?
0x197f29038  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSecureCodingBox.__allocating_init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSecureCodingBox?
0x197c2b25c  __TEXT,__text  CloudKit.CKSecureCodingBox.init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSecureCodingBox?
0x197e33dc4  __TEXT,__text  CloudKit.CKSecureCodingBox.__allocating_init(coder: __C.NSCoder) -> CloudKit.CKSecureCodingBox?
0x197e347c4  __TEXT,__text  dispatch thunk of CloudKit.CKSecureCodingBox.__allocating_init(coder: __C.NSCoder) -> CloudKit.CKSecureCodingBox?
0x197f29030  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSecureCodingBox.__allocating_init(coder: __C.NSCoder) -> CloudKit.CKSecureCodingBox?
0x197e33ddc  __TEXT,__text  CloudKit.CKSecureCodingBox.init(coder: __C.NSCoder) -> CloudKit.CKSecureCodingBox?
0x197e34798  __TEXT,__text  dispatch thunk of CloudKit.CKSecureCodingBox.encode(with: __C.NSCoder) -> ()
0x197f29028  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSecureCodingBox.encode(with: __C.NSCoder) -> ()
0x197e34744  __TEXT,__text  dispatch thunk of CloudKit.CKSecureCodingBox.wrapped.modify : Swift.Decodable & Swift.Encodable & Swift.Hashable
0x197f29010  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSecureCodingBox.wrapped.modify : Swift.Decodable & Swift.Encodable & Swift.Hashable
0x197e346ec  __TEXT,__text  dispatch thunk of CloudKit.CKSecureCodingBox.wrapped.getter : Swift.Decodable & Swift.Encodable & Swift.Hashable
0x197f29000  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSecureCodingBox.wrapped.getter : Swift.Decodable & Swift.Encodable & Swift.Hashable
0x1e0c41560  __DATA_CONST,__const  property descriptor for CloudKit.CKSecureCodingBox.wrapped : Swift.Decodable & Swift.Encodable & Swift.Hashable
0x197e34718  __TEXT,__text  dispatch thunk of CloudKit.CKSecureCodingBox.wrapped.setter : Swift.Decodable & Swift.Encodable & Swift.Hashable
0x197f29008  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSecureCodingBox.wrapped.setter : Swift.Decodable & Swift.Encodable & Swift.Hashable
0x197e33c9c  __TEXT,__text  CloudKit.CKSecureCodingBox.__allocating_init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSecureCodingBox
0x197e34770  __TEXT,__text  dispatch thunk of CloudKit.CKSecureCodingBox.__allocating_init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSecureCodingBox
0x197f29018  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSecureCodingBox.__allocating_init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSecureCodingBox
0x197e336c0  __TEXT,__text  CloudKit.CKSecureCodingBox.init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSecureCodingBox
0x197e34058  __TEXT,__text  CloudKit.CKSecureCodingBox.__allocating_init() -> CloudKit.CKSecureCodingBox
0x197ecc158  __TEXT,__text  CloudKit.CKSecureCodingBox.init() -> CloudKit.CKSecureCodingBox
0x197c125a0  __TEXT,__text  type metadata accessor for CloudKit.CKSecureCodingBox
0x197f28fcc  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSecureCodingBox
0x197ef59a8  __TEXT,__const  class metadata base offset for CloudKit.CKSecureCodingBox
0x197e346d4  __TEXT,__text  method lookup function for CloudKit.CKSecureCodingBox
0x1ee078fc8  __DATA_DIRTY,__objc_data  type metadata for CloudKit.CKSecureCodingBox
0x197e34088  __TEXT,__text  CloudKit.CKSecureCodingBox.__deallocating_deinit
0x197e1581c  __TEXT,__text  CloudKit.CKServerTimestamp.description.getter : Swift.String
0x197ef3dd8  __TEXT,__const  property descriptor for CloudKit.CKServerTimestamp.description : Swift.String
0x197e14e54  __TEXT,__text  static CloudKit.CKServerTimestamp.== infix(CloudKit.CKServerTimestamp, CloudKit.CKServerTimestamp) -> Swift.Bool
0x197e15b64  __TEXT,__text  CloudKit.CKServerTimestamp.Time.description.getter : Swift.String
0x197ef3dd8  __TEXT,__const  property descriptor for CloudKit.CKServerTimestamp.Time.description : Swift.String
0x197e15a78  __TEXT,__text  static CloudKit.CKServerTimestamp.Time.< infix(CloudKit.CKServerTimestamp.Time, CloudKit.CKServerTimestamp.Time) -> Swift.Bool
0x197e14768  __TEXT,__text  static CloudKit.CKServerTimestamp.Time.== infix(CloudKit.CKServerTimestamp.Time, CloudKit.CKServerTimestamp.Time) -> Swift.Bool
0x197e14b90  __TEXT,__text  CloudKit.CKServerTimestamp.Time.init(from: Swift.Decoder) throws -> CloudKit.CKServerTimestamp.Time
0x197e149d8  __TEXT,__text  CloudKit.CKServerTimestamp.Time.hash(into: inout Swift.Hasher) -> ()
0x197e148c4  __TEXT,__text  CloudKit.CKServerTimestamp.Time.encode(to: Swift.Encoder) throws -> ()
0x197e14aa8  __TEXT,__text  CloudKit.CKServerTimestamp.Time.hashValue.getter : Swift.Int
0x197ef3dd8  __TEXT,__const  property descriptor for CloudKit.CKServerTimestamp.Time.hashValue : Swift.Int
0x197e14744  __TEXT,__text  CloudKit.CKServerTimestamp.Time.init() -> CloudKit.CKServerTimestamp.Time
0x197e18544  __TEXT,__text  type metadata accessor for CloudKit.CKServerTimestamp.Time
0x197f2879c  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKServerTimestamp.Time
0x1e3ca72c8  __AUTH_CONST,__const  type metadata for CloudKit.CKServerTimestamp.Time
0x197ef3bd0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp.Time : Swift.Encodable in CloudKit
0x197ef3bf8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp.Time : Swift.Hashable in CloudKit
0x197ef3d68  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp.Time : Swift.Comparable in CloudKit
0x197ef3c38  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp.Time : Swift.Equatable in CloudKit
0x197ef3ba8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp.Time : Swift.Decodable in CloudKit
0x197ef3db0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp.Time : Swift.CustomStringConvertible in CloudKit
0x197e154c4  __TEXT,__text  CloudKit.CKServerTimestamp.init(from: Swift.Decoder) throws -> CloudKit.CKServerTimestamp
0x197e152cc  __TEXT,__text  CloudKit.CKServerTimestamp.hash(into: inout Swift.Hasher) -> ()
0x197e14e28  __TEXT,__text  CloudKit.CKServerTimestamp.time.getter : CloudKit.CKServerTimestamp.Time
0x197ef3de0  __TEXT,__const  property descriptor for CloudKit.CKServerTimestamp.time : CloudKit.CKServerTimestamp.Time
0x197ef3fbc  __TEXT,__const  enum case for CloudKit.CKServerTimestamp.Domain.recordZone(CloudKit.CKServerTimestamp.Domain.Type) -> (__C.CKRecordZoneID) -> CloudKit.CKServerTimestamp.Domain
0x197e15958  __TEXT,__text  CloudKit.CKServerTimestamp.Domain.description.getter : Swift.String
0x197ef3dd8  __TEXT,__const  property descriptor for CloudKit.CKServerTimestamp.Domain.description : Swift.String
0x197e13664  __TEXT,__text  static CloudKit.CKServerTimestamp.Domain.== infix(CloudKit.CKServerTimestamp.Domain, CloudKit.CKServerTimestamp.Domain) -> Swift.Bool
0x197e1401c  __TEXT,__text  CloudKit.CKServerTimestamp.Domain.init(from: Swift.Decoder) throws -> CloudKit.CKServerTimestamp.Domain
0x197e13f90  __TEXT,__text  CloudKit.CKServerTimestamp.Domain.hash(into: inout Swift.Hasher) -> ()
0x197ef3fc0  __TEXT,__const  enum case for CloudKit.CKServerTimestamp.Domain.user(CloudKit.CKServerTimestamp.Domain.Type) -> (__C.CKRecordID) -> CloudKit.CKServerTimestamp.Domain
0x197e13a20  __TEXT,__text  CloudKit.CKServerTimestamp.Domain.encode(to: Swift.Encoder) throws -> ()
0x197ef3fb8  __TEXT,__const  enum case for CloudKit.CKServerTimestamp.Domain.record(CloudKit.CKServerTimestamp.Domain.Type) -> (__C.CKRecordID) -> CloudKit.CKServerTimestamp.Domain
0x197e13fc4  __TEXT,__text  CloudKit.CKServerTimestamp.Domain.hashValue.getter : Swift.Int
0x197ef3dd8  __TEXT,__const  property descriptor for CloudKit.CKServerTimestamp.Domain.hashValue : Swift.Int
0x197e18488  __TEXT,__text  type metadata accessor for CloudKit.CKServerTimestamp.Domain
0x197f28780  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKServerTimestamp.Domain
0x1e3ca7010  __AUTH_CONST,__const  type metadata for CloudKit.CKServerTimestamp.Domain
0x197ef3b18  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp.Domain : Swift.Encodable in CloudKit
0x197ef3b68  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp.Domain : Swift.Hashable in CloudKit
0x197ef3b40  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp.Domain : Swift.Equatable in CloudKit
0x197ef3af0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp.Domain : Swift.Decodable in CloudKit
0x197ef3d40  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp.Domain : Swift.CustomStringConvertible in CloudKit
0x197e14e14  __TEXT,__text  CloudKit.CKServerTimestamp.domain.getter : CloudKit.CKServerTimestamp.Domain
0x197ef3ddc  __TEXT,__const  property descriptor for CloudKit.CKServerTimestamp.domain : CloudKit.CKServerTimestamp.Domain
0x197e15104  __TEXT,__text  CloudKit.CKServerTimestamp.encode(to: Swift.Encoder) throws -> ()
0x197e153cc  __TEXT,__text  CloudKit.CKServerTimestamp.hashValue.getter : Swift.Int
0x197ef3dd8  __TEXT,__const  property descriptor for CloudKit.CKServerTimestamp.hashValue : Swift.Int
0x197e183f4  __TEXT,__text  type metadata accessor for CloudKit.CKServerTimestamp
0x197f28764  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKServerTimestamp
0x1e3ca6f78  __AUTH_CONST,__const  type metadata for CloudKit.CKServerTimestamp
0x197ef3c88  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp : Swift.Encodable in CloudKit
0x197ef3cd8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp : Swift.Hashable in CloudKit
0x197ef3cb0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp : Swift.Equatable in CloudKit
0x197ef3c60  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp : Swift.Decodable in CloudKit
0x197ef3d18  __TEXT,__const  protocol conformance descriptor for CloudKit.CKServerTimestamp : Swift.CustomStringConvertible in CloudKit
0x197eb87c0  __TEXT,__text  CloudKit.AsyncResourcesLock.description.getter : Swift.String
0x197efad50  __TEXT,__const  property descriptor for CloudKit.AsyncResourcesLock.description : Swift.String
0x197eb8750  __TEXT,__text  CloudKit.AsyncResourcesLock.getLoggingID() -> Swift.String
0x197eaa2f8  __TEXT,__text  CloudKit.AsyncResourcesLock.setLoggingID(Swift.String) -> ()
0x197eb8798  __TEXT,__text  CloudKit.AsyncResourcesLock.unownedExecutor.getter : Swift.UnownedSerialExecutor
0x197efad50  __TEXT,__const  property descriptor for CloudKit.AsyncResourcesLock.unownedExecutor : Swift.UnownedSerialExecutor
0x197eabb34  __TEXT,__text  CloudKit.AsyncResourcesLock.with<A where A1: Swift.Sendable>(block: () async throws -> A1) async throws -> A1
0x197efac30  __TEXT,__const  async function pointer to CloudKit.AsyncResourcesLock.with<A where A1: Swift.Sendable>(block: () async throws -> A1) async throws -> A1
0x197eada44  __TEXT,__text  CloudKit.AsyncResourcesLock.with<A, B where A == B1.Element, A1: Swift.Sendable, B1: Swift.Collection>(_: B1, block: () async throws -> A1) async throws -> A1
0x197efac40  __TEXT,__const  async function pointer to CloudKit.AsyncResourcesLock.with<A, B where A == B1.Element, A1: Swift.Sendable, B1: Swift.Collection>(_: B1, block: () async throws -> A1) async throws -> A1
0x197eb0970  __TEXT,__text  CloudKit.AsyncResourcesLock.with<A where A1: Swift.Sendable>(_: A, block: () async throws -> A1) async throws -> A1
0x197efac50  __TEXT,__const  async function pointer to CloudKit.AsyncResourcesLock.with<A where A1: Swift.Sendable>(_: A, block: () async throws -> A1) async throws -> A1
0x197efae30  __TEXT,__const  enum case for CloudKit.AsyncResourcesLock.Error.lockTearDown<A where A: Swift.Hashable, A: Swift.Sendable>(CloudKit.AsyncResourcesLock<A>.Error.Type) -> CloudKit.AsyncResourcesLock<A>.Error
0x197eaebc0  __TEXT,__text  static CloudKit.AsyncResourcesLock.Error.== infix(CloudKit.AsyncResourcesLock<A>.Error, CloudKit.AsyncResourcesLock<A>.Error) -> Swift.Bool
0x197eaebc8  __TEXT,__text  CloudKit.AsyncResourcesLock.Error.hash(into: inout Swift.Hasher) -> ()
0x197eaebf0  __TEXT,__text  CloudKit.AsyncResourcesLock.Error.hashValue.getter : Swift.Int
0x197efad50  __TEXT,__const  property descriptor for CloudKit.AsyncResourcesLock.Error.hashValue : Swift.Int
0x197ebc00c  __TEXT,__text  type metadata accessor for CloudKit.AsyncResourcesLock.Error
0x197f29e6c  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.AsyncResourcesLock.Error
0x197efac80  __TEXT,__const  protocol conformance descriptor for CloudKit.AsyncResourcesLock<A>.Error : Swift.Hashable in CloudKit
0x197efac58  __TEXT,__const  protocol conformance descriptor for CloudKit.AsyncResourcesLock<A>.Error : Swift.Equatable in CloudKit
0x197efacc0  __TEXT,__const  protocol conformance descriptor for CloudKit.AsyncResourcesLock<A>.Error : Swift.Error in CloudKit
0x197eaf66c  __TEXT,__text  CloudKit.AsyncResourcesLock.tearDown() -> ()
0x197eaa2c0  __TEXT,__text  CloudKit.AsyncResourcesLock.__allocating_init() -> CloudKit.AsyncResourcesLock<A>
0x197ebc058  __TEXT,__text  dispatch thunk of CloudKit.AsyncResourcesLock.__allocating_init() -> CloudKit.AsyncResourcesLock<A>
0x197f29e64  __TEXT,__constg_swiftt  method descriptor for CloudKit.AsyncResourcesLock.__allocating_init() -> CloudKit.AsyncResourcesLock<A>
0x197eaf200  __TEXT,__text  CloudKit.AsyncResourcesLock.init() -> CloudKit.AsyncResourcesLock<A>
0x197c339f4  __TEXT,__text  type metadata accessor for CloudKit.AsyncResourcesLock
0x197f29e10  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.AsyncResourcesLock
0x197efad90  __TEXT,__const  class metadata base offset for CloudKit.AsyncResourcesLock
0x197ebc040  __TEXT,__text  method lookup function for CloudKit.AsyncResourcesLock
0x197eaf64c  __TEXT,__text  CloudKit.AsyncResourcesLock.__deallocating_deinit
0x197eaf37c  __TEXT,__text  CloudKit.AsyncResourcesLock.deinit
0x197efad00  __TEXT,__const  protocol conformance descriptor for CloudKit.AsyncResourcesLock<A> : Swift.Actor in CloudKit
0x197efad28  __TEXT,__const  protocol conformance descriptor for CloudKit.AsyncResourcesLock<A> : Swift.CustomStringConvertible in CloudKit
0x197df4794  __TEXT,__text  static CloudKit.CKDeviceCapability.MaxUTF8Bytes.getter : Swift.Int
0x197ef1e88  __TEXT,__const  property descriptor for static CloudKit.CKDeviceCapability.MaxUTF8Bytes : Swift.Int
0x197df4b80  __TEXT,__text  static CloudKit.CKDeviceCapability.== infix(CloudKit.CKDeviceCapability, CloudKit.CKDeviceCapability) -> Swift.Bool
0x197df4c1c  __TEXT,__text  CloudKit.CKDeviceCapability.hash(into: inout Swift.Hasher) -> ()
0x197df491c  __TEXT,__text  CloudKit.CKDeviceCapability.name.modify : Swift.String
0x197df484c  __TEXT,__text  CloudKit.CKDeviceCapability.name.getter : Swift.String
0x1e0c412e0  __DATA_CONST,__const  property descriptor for CloudKit.CKDeviceCapability.name : Swift.String
0x197df48c4  __TEXT,__text  CloudKit.CKDeviceCapability.name.setter : Swift.String
0x197ef1edc  __TEXT,__const  enum case for CloudKit.CKDeviceCapability.Level.zone(CloudKit.CKDeviceCapability.Level.Type) -> CloudKit.CKDeviceCapability.Level
0x197ef1ee4  __TEXT,__const  enum case for CloudKit.CKDeviceCapability.Level.field(CloudKit.CKDeviceCapability.Level.Type) -> CloudKit.CKDeviceCapability.Level
0x197ef1ee0  __TEXT,__const  enum case for CloudKit.CKDeviceCapability.Level.record(CloudKit.CKDeviceCapability.Level.Type) -> CloudKit.CKDeviceCapability.Level
0x197df479c  __TEXT,__text  CloudKit.CKDeviceCapability.Level.init(rawValue: Swift.Int) -> CloudKit.CKDeviceCapability.Level?
0x197df47c0  __TEXT,__text  CloudKit.CKDeviceCapability.Level.rawValue.getter : Swift.Int
0x197ef1e88  __TEXT,__const  property descriptor for CloudKit.CKDeviceCapability.Level.rawValue : Swift.Int
0x197dfaa1c  __TEXT,__text  type metadata accessor for CloudKit.CKDeviceCapability.Level
0x197f2822c  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKDeviceCapability.Level
0x1e3ca6bd0  __AUTH_CONST,__const  type metadata for CloudKit.CKDeviceCapability.Level
0x197ef19f8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapability.Level : Swift.Hashable in CloudKit
0x197ef19d0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapability.Level : Swift.Equatable in CloudKit
0x197ef1a38  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapability.Level : Swift.RawRepresentable in CloudKit
0x197df4abc  __TEXT,__text  CloudKit.CKDeviceCapability.init(level: CloudKit.CKDeviceCapability.Level, name: Swift.String, value: Swift.String) -> CloudKit.CKDeviceCapability
0x197df482c  __TEXT,__text  CloudKit.CKDeviceCapability.level.modify : CloudKit.CKDeviceCapability.Level
0x197df4814  __TEXT,__text  CloudKit.CKDeviceCapability.level.getter : CloudKit.CKDeviceCapability.Level
0x197ef1e8c  __TEXT,__const  property descriptor for CloudKit.CKDeviceCapability.level : CloudKit.CKDeviceCapability.Level
0x197df4820  __TEXT,__text  CloudKit.CKDeviceCapability.level.setter : CloudKit.CKDeviceCapability.Level
0x197df4a54  __TEXT,__text  CloudKit.CKDeviceCapability.value.modify : Swift.String
0x197df4984  __TEXT,__text  CloudKit.CKDeviceCapability.value.getter : Swift.String
0x1e0c412f0  __DATA_CONST,__const  property descriptor for CloudKit.CKDeviceCapability.value : Swift.String
0x197df49fc  __TEXT,__text  CloudKit.CKDeviceCapability.value.setter : Swift.String
0x197df4b40  __TEXT,__text  CloudKit.CKDeviceCapability.isEmpty.getter : Swift.Bool
0x197ef1e88  __TEXT,__const  property descriptor for CloudKit.CKDeviceCapability.isEmpty : Swift.Bool
0x197df4c64  __TEXT,__text  CloudKit.CKDeviceCapability.hashValue.getter : Swift.Int
0x197ef1e88  __TEXT,__const  property descriptor for CloudKit.CKDeviceCapability.hashValue : Swift.Int
0x197dfa940  __TEXT,__text  type metadata accessor for CloudKit.CKDeviceCapability
0x197f28210  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKDeviceCapability
0x1e3ca6b30  __AUTH_CONST,__const  type metadata for CloudKit.CKDeviceCapability
0x197ef1a70  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapability : Swift.Hashable in CloudKit
0x197ef1ab0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapability : Swift.Equatable in CloudKit
0x197ec06a8  __TEXT,__text  CloudKit.CKLogTrafficBinary.getter : os.Logger
0x197ec0984  __TEXT,__text  CloudKit.CKLogDistributedSync.getter : os.Logger
0x197e06d80  __TEXT,__text  CloudKit.CKRequiredFeatureSet.description.getter : Swift.String
0x197ef27f4  __TEXT,__const  property descriptor for CloudKit.CKRequiredFeatureSet.description : Swift.String
0x197e06ce0  __TEXT,__text  static CloudKit.CKRequiredFeatureSet.== infix(CloudKit.CKRequiredFeatureSet, CloudKit.CKRequiredFeatureSet) -> Swift.Bool
0x197e06f88  __TEXT,__text  CloudKit.CKRequiredFeatureSet.hash(into: inout Swift.Hasher) -> ()
0x197e06910  __TEXT,__text  CloudKit.CKRequiredFeatureSet.init<A, B, C where A: Swift.Collection, B: Swift.Collection, C: Swift.Collection, A.Element == CloudKit.CKZoneFeature, B.Element == CloudKit.CKRecordFeature, C.Element == CloudKit.CKFieldFeature>(zone: A, record: B, field: C) -> CloudKit.CKRequiredFeatureSet
0x197e0683c  __TEXT,__text  CloudKit.CKRequiredFeatureSet.zone.modify : CloudKit.CKFeatureSet<CloudKit.CKZoneFeature>
0x197e06808  __TEXT,__text  CloudKit.CKRequiredFeatureSet.zone.getter : CloudKit.CKFeatureSet<CloudKit.CKZoneFeature>
0x197ef27f8  __TEXT,__const  property descriptor for CloudKit.CKRequiredFeatureSet.zone : CloudKit.CKFeatureSet<CloudKit.CKZoneFeature>
0x197e06810  __TEXT,__text  CloudKit.CKRequiredFeatureSet.zone.setter : CloudKit.CKFeatureSet<CloudKit.CKZoneFeature>
0x197e068e4  __TEXT,__text  CloudKit.CKRequiredFeatureSet.field.modify : CloudKit.CKFeatureSet<CloudKit.CKFieldFeature>
0x197e068b0  __TEXT,__text  CloudKit.CKRequiredFeatureSet.field.getter : CloudKit.CKFeatureSet<CloudKit.CKFieldFeature>
0x197ef2800  __TEXT,__const  property descriptor for CloudKit.CKRequiredFeatureSet.field : CloudKit.CKFeatureSet<CloudKit.CKFieldFeature>
0x197e068b8  __TEXT,__text  CloudKit.CKRequiredFeatureSet.field.setter : CloudKit.CKFeatureSet<CloudKit.CKFieldFeature>
0x197e06b90  __TEXT,__text  CloudKit.CKRequiredFeatureSet.insert(CloudKit.CKZoneFeature) -> ()
0x197e06c64  __TEXT,__text  CloudKit.CKRequiredFeatureSet.insert(CloudKit.CKFieldFeature) -> ()
0x197e06be8  __TEXT,__text  CloudKit.CKRequiredFeatureSet.insert(CloudKit.CKRecordFeature) -> ()
0x197e06ba0  __TEXT,__text  CloudKit.CKRequiredFeatureSet.insert<A where A: Swift.Collection, A.Element == CloudKit.CKZoneFeature>(A) -> ()
0x197e06c94  __TEXT,__text  CloudKit.CKRequiredFeatureSet.insert<A where A: Swift.Collection, A.Element == CloudKit.CKFieldFeature>(A) -> ()
0x197e06c18  __TEXT,__text  CloudKit.CKRequiredFeatureSet.insert<A where A: Swift.Collection, A.Element == CloudKit.CKRecordFeature>(A) -> ()
0x197e06890  __TEXT,__text  CloudKit.CKRequiredFeatureSet.record.modify : CloudKit.CKFeatureSet<CloudKit.CKRecordFeature>
0x197e0685c  __TEXT,__text  CloudKit.CKRequiredFeatureSet.record.getter : CloudKit.CKFeatureSet<CloudKit.CKRecordFeature>
0x197ef27fc  __TEXT,__const  property descriptor for CloudKit.CKRequiredFeatureSet.record : CloudKit.CKFeatureSet<CloudKit.CKRecordFeature>
0x197e06864  __TEXT,__text  CloudKit.CKRequiredFeatureSet.record.setter : CloudKit.CKFeatureSet<CloudKit.CKRecordFeature>
0x197e06b5c  __TEXT,__text  CloudKit.CKRequiredFeatureSet.isEmpty.getter : Swift.Bool
0x197ef27f4  __TEXT,__const  property descriptor for CloudKit.CKRequiredFeatureSet.isEmpty : Swift.Bool
0x197e07244  __TEXT,__text  CloudKit.CKRequiredFeatureSet.hashValue.getter : Swift.Int
0x197ef27f4  __TEXT,__const  property descriptor for CloudKit.CKRequiredFeatureSet.hashValue : Swift.Int
0x197e068fc  __TEXT,__text  CloudKit.CKRequiredFeatureSet.init() -> CloudKit.CKRequiredFeatureSet
0x197e098d4  __TEXT,__text  type metadata accessor for CloudKit.CKRequiredFeatureSet
0x197f283f8  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKRequiredFeatureSet
0x1e3ca6a18  __AUTH_CONST,__const  type metadata for CloudKit.CKRequiredFeatureSet
0x197ef27b4  __TEXT,__const  protocol conformance descriptor for CloudKit.CKRequiredFeatureSet : Swift.Hashable in CloudKit
0x197ef2764  __TEXT,__const  protocol conformance descriptor for CloudKit.CKRequiredFeatureSet : Swift.Equatable in CloudKit
0x197ef278c  __TEXT,__const  protocol conformance descriptor for CloudKit.CKRequiredFeatureSet : Swift.CustomStringConvertible in CloudKit
0x197f29770  __TEXT,__constg_swiftt  protocol descriptor for CloudKit.CKSyncEngineDelegate
0x197e95a54  __TEXT,__text  dispatch thunk of CloudKit.CKSyncEngineDelegate.handleEvent(_: CloudKit.CKSyncEngine.Event, syncEngine: CloudKit.CKSyncEngine) async -> ()
0x197ef7828  __TEXT,__const  async function pointer to dispatch thunk of CloudKit.CKSyncEngineDelegate.handleEvent(_: CloudKit.CKSyncEngine.Event, syncEngine: CloudKit.CKSyncEngine) async -> ()
0x197f29794  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSyncEngineDelegate.handleEvent(_: CloudKit.CKSyncEngine.Event, syncEngine: CloudKit.CKSyncEngine) async -> ()
0x197e95e40  __TEXT,__text  dispatch thunk of CloudKit.CKSyncEngineDelegate.shouldFetchChanges(zoneID: __C.CKRecordZoneID, syncEngine: CloudKit.CKSyncEngine) async -> Swift.Bool
0x197ef7868  __TEXT,__const  async function pointer to dispatch thunk of CloudKit.CKSyncEngineDelegate.shouldFetchChanges(zoneID: __C.CKRecordZoneID, syncEngine: CloudKit.CKSyncEngine) async -> Swift.Bool
0x197f297bc  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSyncEngineDelegate.shouldFetchChanges(zoneID: __C.CKRecordZoneID, syncEngine: CloudKit.CKSyncEngine) async -> Swift.Bool
0x197e95cb0  __TEXT,__text  dispatch thunk of CloudKit.CKSyncEngineDelegate.nextFetchAssetsOptions(_: CloudKit.CKSyncEngine.FetchAssetsContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.FetchAssetsOptions
0x197ef7848  __TEXT,__const  async function pointer to dispatch thunk of CloudKit.CKSyncEngineDelegate.nextFetchAssetsOptions(_: CloudKit.CKSyncEngine.FetchAssetsContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.FetchAssetsOptions
0x197f297ac  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSyncEngineDelegate.nextFetchAssetsOptions(_: CloudKit.CKSyncEngine.FetchAssetsContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.FetchAssetsOptions
0x197e95d78  __TEXT,__text  dispatch thunk of CloudKit.CKSyncEngineDelegate.nextSendChangesOptions(_: CloudKit.CKSyncEngine.SendChangesContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.SendChangesOptions
0x197ef7858  __TEXT,__const  async function pointer to dispatch thunk of CloudKit.CKSyncEngineDelegate.nextSendChangesOptions(_: CloudKit.CKSyncEngine.SendChangesContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.SendChangesOptions
0x197f297b4  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSyncEngineDelegate.nextSendChangesOptions(_: CloudKit.CKSyncEngine.SendChangesContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.SendChangesOptions
0x197e95be8  __TEXT,__text  dispatch thunk of CloudKit.CKSyncEngineDelegate.nextFetchChangesOptions(_: CloudKit.CKSyncEngine.FetchChangesContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.FetchChangesOptions
0x197ef7838  __TEXT,__const  async function pointer to dispatch thunk of CloudKit.CKSyncEngineDelegate.nextFetchChangesOptions(_: CloudKit.CKSyncEngine.FetchChangesContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.FetchChangesOptions
0x197f297a4  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSyncEngineDelegate.nextFetchChangesOptions(_: CloudKit.CKSyncEngine.FetchChangesContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.FetchChangesOptions
0x197e95b20  __TEXT,__text  dispatch thunk of CloudKit.CKSyncEngineDelegate.nextRecordZoneChangeBatch(_: CloudKit.CKSyncEngine.SendChangesContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.RecordZoneChangeBatch?
0x197ef7830  __TEXT,__const  async function pointer to dispatch thunk of CloudKit.CKSyncEngineDelegate.nextRecordZoneChangeBatch(_: CloudKit.CKSyncEngine.SendChangesContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.RecordZoneChangeBatch?
0x197f2979c  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSyncEngineDelegate.nextRecordZoneChangeBatch(_: CloudKit.CKSyncEngine.SendChangesContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.RecordZoneChangeBatch?
0x197e95fc0  __TEXT,__text  dispatch thunk of CloudKit.CKSyncEngineDelegate.relatedApplicationBundleIdentifiers(zoneIDs: [__C.CKRecordZoneID], recordIDs: [__C.CKRecordID], syncEngine: CloudKit.CKSyncEngine) async -> [Swift.String]?
0x197ef7878  __TEXT,__const  async function pointer to dispatch thunk of CloudKit.CKSyncEngineDelegate.relatedApplicationBundleIdentifiers(zoneIDs: [__C.CKRecordZoneID], recordIDs: [__C.CKRecordID], syncEngine: CloudKit.CKSyncEngine) async -> [Swift.String]?
0x197f297c4  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSyncEngineDelegate.relatedApplicationBundleIdentifiers(zoneIDs: [__C.CKRecordZoneID], recordIDs: [__C.CKRecordID], syncEngine: CloudKit.CKSyncEngine) async -> [Swift.String]?
0x197ec3598  __TEXT,__text  (extension in CloudKit):CloudKit.CKSyncEngineDelegate.shouldFetchChanges(zoneID: __C.CKRecordZoneID, syncEngine: CloudKit.CKSyncEngine) async -> Swift.Bool
0x197efb220  __TEXT,__const  async function pointer to (extension in CloudKit):CloudKit.CKSyncEngineDelegate.shouldFetchChanges(zoneID: __C.CKRecordZoneID, syncEngine: CloudKit.CKSyncEngine) async -> Swift.Bool
0x197e95664  __TEXT,__text  (extension in CloudKit):CloudKit.CKSyncEngineDelegate.nextFetchAssetsOptions(_: CloudKit.CKSyncEngine.FetchAssetsContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.FetchAssetsOptions
0x197ef77f0  __TEXT,__const  async function pointer to (extension in CloudKit):CloudKit.CKSyncEngineDelegate.nextFetchAssetsOptions(_: CloudKit.CKSyncEngine.FetchAssetsContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.FetchAssetsOptions
0x197e959e0  __TEXT,__text  (extension in CloudKit):CloudKit.CKSyncEngineDelegate.nextSendChangesOptions(_: CloudKit.CKSyncEngine.SendChangesContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.SendChangesOptions
0x197ef7808  __TEXT,__const  async function pointer to (extension in CloudKit):CloudKit.CKSyncEngineDelegate.nextSendChangesOptions(_: CloudKit.CKSyncEngine.SendChangesContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.SendChangesOptions
0x197e9577c  __TEXT,__text  (extension in CloudKit):CloudKit.CKSyncEngineDelegate.nextFetchChangesOptions(_: CloudKit.CKSyncEngine.FetchChangesContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.FetchChangesOptions
0x197ef77f8  __TEXT,__const  async function pointer to (extension in CloudKit):CloudKit.CKSyncEngineDelegate.nextFetchChangesOptions(_: CloudKit.CKSyncEngine.FetchChangesContext, syncEngine: CloudKit.CKSyncEngine) async -> CloudKit.CKSyncEngine.FetchChangesOptions
0x197ec3580  __TEXT,__text  (extension in CloudKit):CloudKit.CKSyncEngineDelegate.relatedApplicationBundleIdentifiers(zoneIDs: [__C.CKRecordZoneID], recordIDs: [__C.CKRecordID], syncEngine: CloudKit.CKSyncEngine) async -> [Swift.String]?
0x197efb218  __TEXT,__const  async function pointer to (extension in CloudKit):CloudKit.CKSyncEngineDelegate.relatedApplicationBundleIdentifiers(zoneIDs: [__C.CKRecordZoneID], recordIDs: [__C.CKRecordID], syncEngine: CloudKit.CKSyncEngine) async -> [Swift.String]?
0x197f2978c  __TEXT,__constg_swiftt  protocol requirements base descriptor for CloudKit.CKSyncEngineDelegate
0x197ec4808  __TEXT,__text  CloudKit.CKAssociatedObjectKey() -> Swift.UnsafeRawPointer
0x197df6a2c  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.startIndex.getter : Swift.Int
0x197ef1e88  __TEXT,__const  property descriptor for CloudKit.CKDeviceCapabilitySet.startIndex : Swift.Int
0x197df73f0  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.init(arrayLiteral: CloudKit.CKDeviceCapability...) -> CloudKit.CKDeviceCapabilitySet
0x197df57a0  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.capabilities.modify : [CloudKit.CKDeviceCapability]
0x197df4e20  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.capabilities.getter : [CloudKit.CKDeviceCapability]
0x1e0c41300  __DATA_CONST,__const  property descriptor for CloudKit.CKDeviceCapabilitySet.capabilities : [CloudKit.CKDeviceCapability]
0x197df4e90  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.capabilities.setter : [CloudKit.CKDeviceCapability]
0x197df70a8  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.init(dictionaryLiteral: (CloudKit.CKDeviceCapability.Level, [Swift.String : [Swift.String]])...) -> CloudKit.CKDeviceCapabilitySet
0x197df663c  __TEXT,__text  static CloudKit.CKDeviceCapabilitySet.== infix(CloudKit.CKDeviceCapabilitySet, CloudKit.CKDeviceCapabilitySet) -> Swift.Bool
0x197df6994  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.hash(into: inout Swift.Hasher) -> ()
0x197df63d0  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.subscript.modify : (level: CloudKit.CKDeviceCapability.Level) -> [CloudKit.CKDeviceCapability]
0x197df596c  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.subscript.getter : (level: CloudKit.CKDeviceCapability.Level) -> [CloudKit.CKDeviceCapability]
0x1e0c41310  __DATA_CONST,__const  property descriptor for CloudKit.CKDeviceCapabilitySet.subscript(level: CloudKit.CKDeviceCapability.Level) -> [CloudKit.CKDeviceCapability]
0x197df5b24  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.subscript.setter : (level: CloudKit.CKDeviceCapability.Level) -> [CloudKit.CKDeviceCapability]
0x197df64a4  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.insert(CloudKit.CKDeviceCapability) -> ()
0x197df655c  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.insert<A where A: Swift.Collection, A.Element == CloudKit.CKDeviceCapability>(A) -> ()
0x197df6a40  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.isEmpty.getter : Swift.Bool
0x197ef1e88  __TEXT,__const  property descriptor for CloudKit.CKDeviceCapabilitySet.isEmpty : Swift.Bool
0x197df6abc  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.contains(CloudKit.CKDeviceCapabilitySet) -> Swift.Bool
0x197df6a34  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.endIndex.getter : Swift.Int
0x197ef1e88  __TEXT,__const  property descriptor for CloudKit.CKDeviceCapabilitySet.endIndex : Swift.Int
0x197df699c  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.hashValue.getter : Swift.Int
0x197ef1e88  __TEXT,__const  property descriptor for CloudKit.CKDeviceCapabilitySet.hashValue : Swift.Int
0x197df58f8  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.init() -> CloudKit.CKDeviceCapabilitySet
0x197dfaa2c  __TEXT,__text  type metadata accessor for CloudKit.CKDeviceCapabilitySet
0x197f28248  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKDeviceCapabilitySet
0x1e3ca6998  __AUTH_CONST,__const  type metadata for CloudKit.CKDeviceCapabilitySet
0x197ef1ad8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapabilitySet : Swift.Hashable in CloudKit
0x197ef1ba0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapabilitySet : Swift.BidirectionalCollection in CloudKit
0x197ef1b18  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapabilitySet : Swift.Equatable in CloudKit
0x197ef1ce8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapabilitySet : Swift.Sequence in CloudKit
0x197ef1b50  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapabilitySet : Swift.RandomAccessCollection in CloudKit
0x197ef1c00  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapabilitySet : Swift.Collection in CloudKit
0x197ef1d88  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapabilitySet : Swift.ExpressibleByArrayLiteral in CloudKit
0x197ef1d50  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapabilitySet : Swift.ExpressibleByDictionaryLiteral in CloudKit
0x197df6a54  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.subscript.getter : (Swift.Int) -> CloudKit.CKDeviceCapability
0x197ef1e88  __TEXT,__const  property descriptor for CloudKit.CKDeviceCapabilitySet.subscript(Swift.Int) -> CloudKit.CKDeviceCapability
0x197df5908  __TEXT,__text  CloudKit.CKDeviceCapabilitySet.init<A where A: Swift.Collection, A.Element == CloudKit.CKDeviceCapability>(A) -> CloudKit.CKDeviceCapabilitySet
0x197f2860c  __TEXT,__constg_swiftt  protocol descriptor for CloudKit.CKRecordValueProtocol
0x197c05a4c  __TEXT,__text  (extension in CloudKit):CloudKit.CKRecordValueProtocol.CKToObjCRecordValue() -> __C.CKRecordValue
0x197e21c68  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.anySessionAcquiredInfo.modify : CloudCoreInternal.AnySessionAcquiredInfo
0x197c25cec  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.anySessionAcquiredInfo.getter : CloudCoreInternal.AnySessionAcquiredInfo
0x1e0c41510  __DATA_CONST,__const  property descriptor for CloudKit.CKSessionAcquiredInfo.anySessionAcquiredInfo : CloudCoreInternal.AnySessionAcquiredInfo
0x197e21ba8  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.anySessionAcquiredInfo.setter : CloudCoreInternal.AnySessionAcquiredInfo
0x197ecbca8  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.__allocating_init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionAcquiredInfo?
0x197ecbcd8  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionAcquiredInfo?
0x197e21f2c  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.__allocating_init(sqliteRepresentation: Swift.String) -> CloudKit.CKSessionAcquiredInfo?
0x197c125f0  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.init(sqliteRepresentation: Swift.String) -> CloudKit.CKSessionAcquiredInfo?
0x197e21ef0  __TEXT,__text  static CloudKit.CKSessionAcquiredInfo.supportsSecureCoding.getter : Swift.Bool
0x197ecbc78  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.__allocating_init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionAcquiredInfo?
0x197ecbce8  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionAcquiredInfo?
0x197e21ef8  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.__allocating_init(coder: __C.NSCoder) -> CloudKit.CKSessionAcquiredInfo?
0x197c2b730  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.init(coder: __C.NSCoder) -> CloudKit.CKSessionAcquiredInfo?
0x197ecbc48  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.__allocating_init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSessionAcquiredInfo
0x197ecbcf8  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSessionAcquiredInfo
0x197c25cc8  __TEXT,__text  type metadata accessor for CloudKit.CKSessionAcquiredInfo
0x197f28a8c  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSessionAcquiredInfo
0x197ef50f8  __TEXT,__const  class metadata base offset for CloudKit.CKSessionAcquiredInfo
0x197e21fc8  __TEXT,__text  method lookup function for CloudKit.CKSessionAcquiredInfo
0x1ef67a948  __AUTH,__objc_data  type metadata for CloudKit.CKSessionAcquiredInfo
0x197e21f70  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.__deallocating_deinit
0x197e21dd0  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.__allocating_init(CloudCoreInternal.AnySessionAcquiredInfo) -> CloudKit.CKSessionAcquiredInfo
0x197e21fe0  __TEXT,__text  dispatch thunk of CloudKit.CKSessionAcquiredInfo.__allocating_init(CloudCoreInternal.AnySessionAcquiredInfo) -> CloudKit.CKSessionAcquiredInfo
0x197f28ac0  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSessionAcquiredInfo.__allocating_init(CloudCoreInternal.AnySessionAcquiredInfo) -> CloudKit.CKSessionAcquiredInfo
0x197e21e04  __TEXT,__text  CloudKit.CKSessionAcquiredInfo.init(CloudCoreInternal.AnySessionAcquiredInfo) -> CloudKit.CKSessionAcquiredInfo
0x197bec814  __TEXT,__text  CloudKit.CKLogTrafficCompressed.getter : os.Logger
0x197e454f8  __TEXT,__text  CloudKit.CKOperationSignpostEnd(_: __C.CKOperation, _: Swift.StaticString, error: Swift.Error?) -> ()
0x197e0d74c  __TEXT,__text  CloudKit.CKRecordTypeUserRecord.getter : Swift.String
0x197e2abbc  __TEXT,__text  CloudKit.CKSessionConfiguration.anySessionConfiguration.modify : CloudCoreInternal.AnySessionConfiguration
0x197c1a4d0  __TEXT,__text  CloudKit.CKSessionConfiguration.anySessionConfiguration.getter : CloudCoreInternal.AnySessionConfiguration
0x1e0c41520  __DATA_CONST,__const  property descriptor for CloudKit.CKSessionConfiguration.anySessionConfiguration : CloudCoreInternal.AnySessionConfiguration
0x197e2aafc  __TEXT,__text  CloudKit.CKSessionConfiguration.anySessionConfiguration.setter : CloudCoreInternal.AnySessionConfiguration
0x197ecbd98  __TEXT,__text  CloudKit.CKSessionConfiguration.__allocating_init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionConfiguration?
0x197ecbdc8  __TEXT,__text  CloudKit.CKSessionConfiguration.init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionConfiguration?
0x197e2aedc  __TEXT,__text  CloudKit.CKSessionConfiguration.__allocating_init(sqliteRepresentation: Swift.String) -> CloudKit.CKSessionConfiguration?
0x197c12038  __TEXT,__text  CloudKit.CKSessionConfiguration.init(sqliteRepresentation: Swift.String) -> CloudKit.CKSessionConfiguration?
0x197e2ae10  __TEXT,__text  static CloudKit.CKSessionConfiguration.supportsSecureCoding.getter : Swift.Bool
0x197ecbd68  __TEXT,__text  CloudKit.CKSessionConfiguration.__allocating_init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionConfiguration?
0x197ecbdd8  __TEXT,__text  CloudKit.CKSessionConfiguration.init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionConfiguration?
0x197e2ae18  __TEXT,__text  CloudKit.CKSessionConfiguration.__allocating_init(coder: __C.NSCoder) -> CloudKit.CKSessionConfiguration?
0x197e2ae4c  __TEXT,__text  CloudKit.CKSessionConfiguration.init(coder: __C.NSCoder) -> CloudKit.CKSessionConfiguration?
0x197ecbd38  __TEXT,__text  CloudKit.CKSessionConfiguration.__allocating_init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSessionConfiguration
0x197ecbde8  __TEXT,__text  CloudKit.CKSessionConfiguration.init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSessionConfiguration
0x197c1a6e4  __TEXT,__text  type metadata accessor for CloudKit.CKSessionConfiguration
0x197f28cec  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSessionConfiguration
0x197ef5708  __TEXT,__const  class metadata base offset for CloudKit.CKSessionConfiguration
0x197e2af58  __TEXT,__text  method lookup function for CloudKit.CKSessionConfiguration
0x1ef67a878  __AUTH,__objc_data  type metadata for CloudKit.CKSessionConfiguration
0x197e2af20  __TEXT,__text  CloudKit.CKSessionConfiguration.__deallocating_deinit
0x197e2aa10  __TEXT,__text  CloudKit.CKSessionConfiguration.__allocating_init(CloudCoreInternal.AnySessionConfiguration) -> CloudKit.CKSessionConfiguration
0x197e2af70  __TEXT,__text  dispatch thunk of CloudKit.CKSessionConfiguration.__allocating_init(CloudCoreInternal.AnySessionConfiguration) -> CloudKit.CKSessionConfiguration
0x197f28d20  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSessionConfiguration.__allocating_init(CloudCoreInternal.AnySessionConfiguration) -> CloudKit.CKSessionConfiguration
0x197e2ad24  __TEXT,__text  CloudKit.CKSessionConfiguration.init(CloudCoreInternal.AnySessionConfiguration) -> CloudKit.CKSessionConfiguration
0x197ec4794  __TEXT,__text  CloudKit.CKUnsafeObjectTransfer.wrapped.modify : A
0x197ec467c  __TEXT,__text  CloudKit.CKUnsafeObjectTransfer.wrapped.getter : A
0x197efb268  __TEXT,__const  property descriptor for CloudKit.CKUnsafeObjectTransfer.wrapped : A
0x197ec4704  __TEXT,__text  CloudKit.CKUnsafeObjectTransfer.wrapped.setter : A
0x197c39130  __TEXT,__text  type metadata accessor for CloudKit.CKUnsafeObjectTransfer
0x197f2a020  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKUnsafeObjectTransfer
0x197efb2a0  __TEXT,__const  class metadata base offset for CloudKit.CKUnsafeObjectTransfer
0x197ec4c60  __TEXT,__text  method lookup function for CloudKit.CKUnsafeObjectTransfer
0x197c2c3bc  __TEXT,__text  CloudKit.CKUnsafeObjectTransfer.__deallocating_deinit
0x197c2d68c  __TEXT,__text  CloudKit.CKUnsafeObjectTransfer.deinit
0x197ec3a4c  __TEXT,__text  CloudKit.CKUnsafeObjectTransfer.__allocating_init(A) -> CloudKit.CKUnsafeObjectTransfer<A>
0x197ec4c78  __TEXT,__text  dispatch thunk of CloudKit.CKUnsafeObjectTransfer.__allocating_init(A) -> CloudKit.CKUnsafeObjectTransfer<A>
0x197f2a068  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKUnsafeObjectTransfer.__allocating_init(A) -> CloudKit.CKUnsafeObjectTransfer<A>
0x197ec4624  __TEXT,__text  CloudKit.CKUnsafeObjectTransfer.init(A) -> CloudKit.CKUnsafeObjectTransfer<A>
0x197ef5060  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDatabaseConfiguration : CloudCoreInternal.PropertyDescribable in CloudKit
0x197e218b4  __TEXT,__text  CloudKit.CKDatabaseConfiguration.propertyDescriptions.getter : [CloudCoreInternal.PropertyDescription]
0x197ef5094  __TEXT,__const  property descriptor for CloudKit.CKDatabaseConfiguration.propertyDescriptions : [CloudCoreInternal.PropertyDescription]
0x197e2185c  __TEXT,__text  CloudKit.CKDatabaseConfiguration.scope.modify : __C.CKDatabaseScope
0x197e2184c  __TEXT,__text  CloudKit.CKDatabaseConfiguration.scope.getter : __C.CKDatabaseScope
0x197ef5090  __TEXT,__const  property descriptor for CloudKit.CKDatabaseConfiguration.scope : __C.CKDatabaseScope
0x197e21854  __TEXT,__text  CloudKit.CKDatabaseConfiguration.scope.setter : __C.CKDatabaseScope
0x197e2187c  __TEXT,__text  static CloudKit.CKDatabaseConfiguration.standard(scope: __C.CKDatabaseScope) -> CloudKit.CKDatabaseConfiguration
0x197e21a8c  __TEXT,__text  type metadata accessor for CloudKit.CKDatabaseConfiguration
0x197f28a70  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKDatabaseConfiguration
0x1e3ca68d8  __AUTH_CONST,__const  type metadata for CloudKit.CKDatabaseConfiguration
0x197ef5038  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDatabaseConfiguration : Swift.CustomStringConvertible in CloudKit
0x197e1123c  __TEXT,__text  CloudKit.CKRecordZoneDefaultName.getter : Swift.String
0x197ec0a60  __TEXT,__text  CloudKit.CKLogDiscretionaryDaemon.getter : os.Logger
0x197e4487c  __TEXT,__text  CloudKit.CKOperationSignpostBegin(__C.CKOperation, Swift.StaticString) -> ()
0x197e0c07c  __TEXT,__text  CloudKit.CKRecordKeyValueIterator.next() -> (Swift.String, CloudKit.CKRecordValueProtocol)?
0x197e0d8b4  __TEXT,__text  type metadata accessor for CloudKit.CKRecordKeyValueIterator
0x197f284f4  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKRecordKeyValueIterator
0x1e3ca6850  __AUTH_CONST,__const  type metadata for CloudKit.CKRecordKeyValueIterator
0x197ef2a80  __TEXT,__const  protocol conformance descriptor for CloudKit.CKRecordKeyValueIterator : Swift.IteratorProtocol in CloudKit
0x197ec08c8  __TEXT,__text  CloudKit.CKLogNotificationListener.getter : os.Logger
0x197ef4f78  __TEXT,__const  protocol conformance descriptor for CloudKit.CKCodeServiceConfiguration : CloudCoreInternal.PropertyDescribable in CloudKit
0x197e1fef8  __TEXT,__text  CloudKit.CKCodeServiceConfiguration.serviceInstanceURL.modify : Foundation.URL?
0x197e1fd6c  __TEXT,__text  CloudKit.CKCodeServiceConfiguration.serviceInstanceURL.getter : Foundation.URL?
0x197ef4fac  __TEXT,__const  property descriptor for CloudKit.CKCodeServiceConfiguration.serviceInstanceURL : Foundation.URL?
0x197e1fe58  __TEXT,__text  CloudKit.CKCodeServiceConfiguration.serviceInstanceURL.setter : Foundation.URL?
0x197e1fff0  __TEXT,__text  CloudKit.CKCodeServiceConfiguration.propertyDescriptions.getter : [CloudCoreInternal.PropertyDescription]
0x197ef4fb4  __TEXT,__const  property descriptor for CloudKit.CKCodeServiceConfiguration.propertyDescriptions : [CloudCoreInternal.PropertyDescription]
0x197e1fd4c  __TEXT,__text  CloudKit.CKCodeServiceConfiguration.name.modify : Swift.String
0x197e1fce4  __TEXT,__text  CloudKit.CKCodeServiceConfiguration.name.getter : Swift.String
0x197ef4fa8  __TEXT,__const  property descriptor for CloudKit.CKCodeServiceConfiguration.name : Swift.String
0x197e1fd14  __TEXT,__text  CloudKit.CKCodeServiceConfiguration.name.setter : Swift.String
0x197e1ff40  __TEXT,__text  static CloudKit.CKCodeServiceConfiguration.standard(name: Swift.String) -> CloudKit.CKCodeServiceConfiguration
0x197e1fda4  __TEXT,__text  type metadata accessor for CloudKit.CKCodeServiceConfiguration
0x197f28a48  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKCodeServiceConfiguration
0x1ef6804b0  __AUTH,__data  type metadata for CloudKit.CKCodeServiceConfiguration
0x197ef4f50  __TEXT,__const  protocol conformance descriptor for CloudKit.CKCodeServiceConfiguration : Swift.CustomStringConvertible in CloudKit
0x197e105ac  __TEXT,__text  CloudKit.CKRecordValueStoreIterator.next() -> (Swift.String, CloudKit.CKRecordValueProtocol)?
0x197e10914  __TEXT,__text  type metadata accessor for CloudKit.CKRecordValueStoreIterator
0x197f286ac  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKRecordValueStoreIterator
0x1e3ca66b8  __AUTH_CONST,__const  type metadata for CloudKit.CKRecordValueStoreIterator
0x197ef3628  __TEXT,__const  protocol conformance descriptor for CloudKit.CKRecordValueStoreIterator : Swift.IteratorProtocol in CloudKit
0x197e10548  __TEXT,__text  CloudKit.CKRecordValueStoreIterator.init(__C.CKRecordKeyValueSetting) -> CloudKit.CKRecordValueStoreIterator
0x197e2c200  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.sessionReadinessError.modify : CloudCoreInternal.SessionReadinessError
0x197e2bfb4  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.sessionReadinessError.getter : CloudCoreInternal.SessionReadinessError
0x1e0c41550  __DATA_CONST,__const  property descriptor for CloudKit.CKSessionReadinessErrorBox.sessionReadinessError : CloudCoreInternal.SessionReadinessError
0x197e2c0fc  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.sessionReadinessError.setter : CloudCoreInternal.SessionReadinessError
0x197e2c76c  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.CKXPCSuitableString() -> Swift.String
0x197ecbfd8  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.__allocating_init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionReadinessErrorBox?
0x197ecc008  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionReadinessErrorBox?
0x197e2c554  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.__allocating_init(sqliteRepresentation: Swift.String) -> CloudKit.CKSessionReadinessErrorBox?
0x197e2c598  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.init(sqliteRepresentation: Swift.String) -> CloudKit.CKSessionReadinessErrorBox?
0x197e2c488  __TEXT,__text  static CloudKit.CKSessionReadinessErrorBox.supportsSecureCoding.getter : Swift.Bool
0x197e2c66c  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.copy(with: ObjectiveC.NSZone?) -> Any
0x197ecbfa8  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.__allocating_init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionReadinessErrorBox?
0x197ecc018  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionReadinessErrorBox?
0x197e2c490  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.__allocating_init(coder: __C.NSCoder) -> CloudKit.CKSessionReadinessErrorBox?
0x197e2c4c4  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.init(coder: __C.NSCoder) -> CloudKit.CKSessionReadinessErrorBox?
0x197ecbf78  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.__allocating_init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSessionReadinessErrorBox
0x197ecc028  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSessionReadinessErrorBox
0x197e2c7f4  __TEXT,__text  type metadata accessor for CloudKit.CKSessionReadinessErrorBox
0x197f28e84  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSessionReadinessErrorBox
0x197ef5790  __TEXT,__const  class metadata base offset for CloudKit.CKSessionReadinessErrorBox
0x197e2c818  __TEXT,__text  method lookup function for CloudKit.CKSessionReadinessErrorBox
0x1ee078ef8  __DATA_DIRTY,__objc_data  type metadata for CloudKit.CKSessionReadinessErrorBox
0x197e2c634  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.__deallocating_deinit
0x197e2c368  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.__allocating_init(CloudCoreInternal.SessionReadinessError) -> CloudKit.CKSessionReadinessErrorBox
0x197e2c830  __TEXT,__text  dispatch thunk of CloudKit.CKSessionReadinessErrorBox.__allocating_init(CloudCoreInternal.SessionReadinessError) -> CloudKit.CKSessionReadinessErrorBox
0x197f28eb8  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSessionReadinessErrorBox.__allocating_init(CloudCoreInternal.SessionReadinessError) -> CloudKit.CKSessionReadinessErrorBox
0x197e2c39c  __TEXT,__text  CloudKit.CKSessionReadinessErrorBox.init(CloudCoreInternal.SessionReadinessError) -> CloudKit.CKSessionReadinessErrorBox
0x197ef5488  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSessionAcquisitionManager : CloudCoreInternal.CKImplementingCC.SessionAcquisitionManagerProtocol in CloudKit
0x197ef54d8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSessionAcquisitionManager : CloudCoreInternal.PropertyDescribable in CloudKit
0x197e296bc  __TEXT,__text  CloudKit.CKSessionAcquisitionManager.propertyDescriptions.getter : [CloudCoreInternal.PropertyDescription]
0x197ef5508  __TEXT,__const  property descriptor for CloudKit.CKSessionAcquisitionManager.propertyDescriptions : [CloudCoreInternal.PropertyDescription]
0x197e290a8  __TEXT,__text  static CloudKit.CKSessionAcquisitionManager.shared.getter : CloudKit.CKSessionAcquisitionManager
0x197ef5508  __TEXT,__const  property descriptor for static CloudKit.CKSessionAcquisitionManager.shared : CloudKit.CKSessionAcquisitionManager
0x197e290e4  __TEXT,__text  CloudKit.CKSessionAcquisitionManager.acquire<A where A: CloudCoreInternal.SessionConfiguration>(sessionID: CloudCoreInternal.SessionID, sessionConfiguration: A, previousInvalidationContext: CloudCoreInternal.SessionInvalidationContext?, testDeviceReferenceProtocol: Swift.AnyObject?, streamMap: @Send
0x197e290b8  __TEXT,__text  CloudKit.CKSessionAcquisitionManager.acquire<A where A: CloudCoreInternal.SessionConfiguration>(sessionID: CloudCoreInternal.SessionID, sessionConfiguration: A, previousInvalidationContext: CloudCoreInternal.SessionInvalidationContext?, streamMap: @Sendable (CloudCoreInternal.AnySessionAcquiredInfo)
0x197e297cc  __TEXT,__text  type metadata accessor for CloudKit.CKSessionAcquisitionManager
0x1ef680d00  __AUTH,__data  metaclass for CloudKit.CKSessionAcquisitionManager
0x197f28c68  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSessionAcquisitionManager
0x197ef5530  __TEXT,__const  class metadata base offset for CloudKit.CKSessionAcquisitionManager
0x197e297f0  __TEXT,__text  method lookup function for CloudKit.CKSessionAcquisitionManager
0x1ef680360  __AUTH,__data  type metadata for CloudKit.CKSessionAcquisitionManager
0x197e29624  __TEXT,__text  CloudKit.CKSessionAcquisitionManager.__deallocating_deinit
0x197e2961c  __TEXT,__text  CloudKit.CKSessionAcquisitionManager.deinit
0x197ef54b0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKSessionAcquisitionManager : Swift.CustomStringConvertible in CloudKit
0x197f297cc  __TEXT,__constg_swiftt  protocol descriptor for CloudKit.CKSyncEngineDelegatePrivate
0x197e96144  __TEXT,__text  dispatch thunk of CloudKit.CKSyncEngineDelegatePrivate.relatedBundleIDs(zoneIDs: [__C.CKRecordZoneID], recordIDs: [__C.CKRecordID], syncEngine: CloudKit.CKSyncEngine) async -> [Swift.String]?
0x197ef78b0  __TEXT,__const  async function pointer to dispatch thunk of CloudKit.CKSyncEngineDelegatePrivate.relatedBundleIDs(zoneIDs: [__C.CKRecordZoneID], recordIDs: [__C.CKRecordID], syncEngine: CloudKit.CKSyncEngine) async -> [Swift.String]?
0x197f297f0  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSyncEngineDelegatePrivate.relatedBundleIDs(zoneIDs: [__C.CKRecordZoneID], recordIDs: [__C.CKRecordID], syncEngine: CloudKit.CKSyncEngine) async -> [Swift.String]?
0x197f297e8  __TEXT,__constg_swiftt  protocol requirements base descriptor for CloudKit.CKSyncEngineDelegatePrivate
0x197e2b8c8  __TEXT,__text  CloudKit.CKSessionInvalidationContext.sessionInvalidationContext.modify : CloudCoreInternal.SessionInvalidationContext
0x197e2b68c  __TEXT,__text  CloudKit.CKSessionInvalidationContext.sessionInvalidationContext.getter : CloudCoreInternal.SessionInvalidationContext
0x1e0c41540  __DATA_CONST,__const  property descriptor for CloudKit.CKSessionInvalidationContext.sessionInvalidationContext : CloudCoreInternal.SessionInvalidationContext
0x197e2b808  __TEXT,__text  CloudKit.CKSessionInvalidationContext.sessionInvalidationContext.setter : CloudCoreInternal.SessionInvalidationContext
0x197e2bde8  __TEXT,__text  CloudKit.CKSessionInvalidationContext.CKXPCSuitableString() -> Swift.String
0x197ecbf18  __TEXT,__text  CloudKit.CKSessionInvalidationContext.__allocating_init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionInvalidationContext?
0x197ecbf48  __TEXT,__text  CloudKit.CKSessionInvalidationContext.init(sqliteRepresentation: Swift.String, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionInvalidationContext?
0x197e2bbe8  __TEXT,__text  CloudKit.CKSessionInvalidationContext.__allocating_init(sqliteRepresentation: Swift.String) -> CloudKit.CKSessionInvalidationContext?
0x197e2bc2c  __TEXT,__text  CloudKit.CKSessionInvalidationContext.init(sqliteRepresentation: Swift.String) -> CloudKit.CKSessionInvalidationContext?
0x197e2bb1c  __TEXT,__text  static CloudKit.CKSessionInvalidationContext.supportsSecureCoding.getter : Swift.Bool
0x197e2bd00  __TEXT,__text  CloudKit.CKSessionInvalidationContext.copy(with: ObjectiveC.NSZone?) -> Any
0x197ecbee8  __TEXT,__text  CloudKit.CKSessionInvalidationContext.__allocating_init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionInvalidationContext?
0x197ecbf58  __TEXT,__text  CloudKit.CKSessionInvalidationContext.init(coder: __C.NSCoder, wrappedType: Swift.Decodable & Swift.Encodable & Swift.Hashable.Type) -> CloudKit.CKSessionInvalidationContext?
0x197e2bb24  __TEXT,__text  CloudKit.CKSessionInvalidationContext.__allocating_init(coder: __C.NSCoder) -> CloudKit.CKSessionInvalidationContext?
0x197e2bb58  __TEXT,__text  CloudKit.CKSessionInvalidationContext.init(coder: __C.NSCoder) -> CloudKit.CKSessionInvalidationContext?
0x197ecbeb8  __TEXT,__text  CloudKit.CKSessionInvalidationContext.__allocating_init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSessionInvalidationContext
0x197ecbf68  __TEXT,__text  CloudKit.CKSessionInvalidationContext.init(wrapping: Swift.Decodable & Swift.Encodable & Swift.Hashable) -> CloudKit.CKSessionInvalidationContext
0x197e2bf08  __TEXT,__text  type metadata accessor for CloudKit.CKSessionInvalidationContext
0x197f28dfc  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSessionInvalidationContext
0x197ef5760  __TEXT,__const  class metadata base offset for CloudKit.CKSessionInvalidationContext
0x197e2bf2c  __TEXT,__text  method lookup function for CloudKit.CKSessionInvalidationContext
0x1ee078e28  __DATA_DIRTY,__objc_data  type metadata for CloudKit.CKSessionInvalidationContext
0x197e2bcc8  __TEXT,__text  CloudKit.CKSessionInvalidationContext.__deallocating_deinit
0x197e2b71c  __TEXT,__text  CloudKit.CKSessionInvalidationContext.__allocating_init(CloudCoreInternal.SessionInvalidationContext) -> CloudKit.CKSessionInvalidationContext
0x197e2bf44  __TEXT,__text  dispatch thunk of CloudKit.CKSessionInvalidationContext.__allocating_init(CloudCoreInternal.SessionInvalidationContext) -> CloudKit.CKSessionInvalidationContext
0x197f28e30  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSessionInvalidationContext.__allocating_init(CloudCoreInternal.SessionInvalidationContext) -> CloudKit.CKSessionInvalidationContext
0x197e2ba30  __TEXT,__text  CloudKit.CKSessionInvalidationContext.init(CloudCoreInternal.SessionInvalidationContext) -> CloudKit.CKSessionInvalidationContext
0x197e1901c  __TEXT,__text  CloudKit.CKShareThumbnailImageDataKey.getter : Swift.String
0x197e48d60  __TEXT,__text  CloudKit.CKSymptomDiagnosticsReporter.__allocating_init(shouldSubmitReportsInProcess: Swift.Bool?) -> CloudKit.CKSymptomDiagnosticsReporter
0x197e4b1fc  __TEXT,__text  dispatch thunk of CloudKit.CKSymptomDiagnosticsReporter.__allocating_init(shouldSubmitReportsInProcess: Swift.Bool?) -> CloudKit.CKSymptomDiagnosticsReporter
0x197f29284  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSymptomDiagnosticsReporter.__allocating_init(shouldSubmitReportsInProcess: Swift.Bool?) -> CloudKit.CKSymptomDiagnosticsReporter
0x197e48d98  __TEXT,__text  CloudKit.CKSymptomDiagnosticsReporter.init(shouldSubmitReportsInProcess: Swift.Bool?) -> CloudKit.CKSymptomDiagnosticsReporter
0x197e48e18  __TEXT,__text  CloudKit.CKSymptomDiagnosticsReporter.report(type: Swift.String, subType: Swift.String, reason: Swift.String?, context: Swift.String?, processName: Swift.String?) async throws -> ()
0x197ef6270  __TEXT,__const  async function pointer to CloudKit.CKSymptomDiagnosticsReporter.report(type: Swift.String, subType: Swift.String, reason: Swift.String?, context: Swift.String?, processName: Swift.String?) async throws -> ()
0x197e4b1ac  __TEXT,__text  type metadata accessor for CloudKit.CKSymptomDiagnosticsReporter
0x1ef681038  __AUTH,__data  metaclass for CloudKit.CKSymptomDiagnosticsReporter
0x197f29248  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKSymptomDiagnosticsReporter
0x197ef62d0  __TEXT,__const  class metadata base offset for CloudKit.CKSymptomDiagnosticsReporter
0x197e4b1d0  __TEXT,__text  method lookup function for CloudKit.CKSymptomDiagnosticsReporter
0x1ef6802d8  __AUTH,__data  type metadata for CloudKit.CKSymptomDiagnosticsReporter
0x197e48ca4  __TEXT,__text  CloudKit.CKSymptomDiagnosticsReporter.__allocating_init(_: @Sendable () -> __C.SDRDiagnosticReporter, shouldSubmitReportsInProcess: Swift.Bool) -> CloudKit.CKSymptomDiagnosticsReporter
0x197e4b1e8  __TEXT,__text  dispatch thunk of CloudKit.CKSymptomDiagnosticsReporter.__allocating_init(_: @Sendable () -> __C.SDRDiagnosticReporter, shouldSubmitReportsInProcess: Swift.Bool) -> CloudKit.CKSymptomDiagnosticsReporter
0x197f2927c  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKSymptomDiagnosticsReporter.__allocating_init(_: @Sendable () -> __C.SDRDiagnosticReporter, shouldSubmitReportsInProcess: Swift.Bool) -> CloudKit.CKSymptomDiagnosticsReporter
0x197e48cf4  __TEXT,__text  CloudKit.CKSymptomDiagnosticsReporter.init(_: @Sendable () -> __C.SDRDiagnosticReporter, shouldSubmitReportsInProcess: Swift.Bool) -> CloudKit.CKSymptomDiagnosticsReporter
0x197e4a6bc  __TEXT,__text  CloudKit.CKSymptomDiagnosticsReporter.__deallocating_deinit
0x197e4a69c  __TEXT,__text  CloudKit.CKSymptomDiagnosticsReporter.deinit
0x197ec38d4  __TEXT,__text  CloudKit.CKCheckedUnsafeObjectTransfer.extractValue() -> A
0x197ec44a0  __TEXT,__text  CloudKit.CKCheckedUnsafeObjectTransfer.setValue(A) -> ()
0x197ec42f8  __TEXT,__text  CloudKit.CKCheckedUnsafeObjectTransfer.__allocating_init() -> CloudKit.CKCheckedUnsafeObjectTransfer<A>
0x197ec4c38  __TEXT,__text  dispatch thunk of CloudKit.CKCheckedUnsafeObjectTransfer.__allocating_init() -> CloudKit.CKCheckedUnsafeObjectTransfer<A>
0x197f2a010  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKCheckedUnsafeObjectTransfer.__allocating_init() -> CloudKit.CKCheckedUnsafeObjectTransfer<A>
0x197ec4330  __TEXT,__text  CloudKit.CKCheckedUnsafeObjectTransfer.init() -> CloudKit.CKCheckedUnsafeObjectTransfer<A>
0x197ec4c08  __TEXT,__text  type metadata accessor for CloudKit.CKCheckedUnsafeObjectTransfer
0x197f29fc8  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKCheckedUnsafeObjectTransfer
0x197efb270  __TEXT,__const  class metadata base offset for CloudKit.CKCheckedUnsafeObjectTransfer
0x197ec4c20  __TEXT,__text  method lookup function for CloudKit.CKCheckedUnsafeObjectTransfer
0x197c3bbf8  __TEXT,__text  CloudKit.CKCheckedUnsafeObjectTransfer.__deallocating_deinit
0x197c39648  __TEXT,__text  CloudKit.CKCheckedUnsafeObjectTransfer.deinit
0x197ec38bc  __TEXT,__text  CloudKit.CKCheckedUnsafeObjectTransfer.__allocating_init(A) -> CloudKit.CKCheckedUnsafeObjectTransfer<A>
0x197ec4c4c  __TEXT,__text  dispatch thunk of CloudKit.CKCheckedUnsafeObjectTransfer.__allocating_init(A) -> CloudKit.CKCheckedUnsafeObjectTransfer<A>
0x197f2a018  __TEXT,__constg_swiftt  method descriptor for CloudKit.CKCheckedUnsafeObjectTransfer.__allocating_init(A) -> CloudKit.CKCheckedUnsafeObjectTransfer<A>
0x197ec4370  __TEXT,__text  CloudKit.CKCheckedUnsafeObjectTransfer.init(A) -> CloudKit.CKCheckedUnsafeObjectTransfer<A>
0x197df79f0  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckResult.init(isSupported: Swift.Bool) -> CloudKit.CKDeviceCapabilityCheckResult
0x197df79e8  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckResult.isSupported.getter : Swift.Bool
0x197ef1e94  __TEXT,__const  property descriptor for CloudKit.CKDeviceCapabilityCheckResult.isSupported : Swift.Bool
0x197df79f8  __TEXT,__text  static CloudKit.CKDeviceCapabilityCheckResult.== infix(CloudKit.CKDeviceCapabilityCheckResult, CloudKit.CKDeviceCapabilityCheckResult) -> Swift.Bool
0x197df7a10  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckResult.hash(into: inout Swift.Hasher) -> ()
0x197df7a3c  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckResult.hashValue.getter : Swift.Int
0x197ef1e88  __TEXT,__const  property descriptor for CloudKit.CKDeviceCapabilityCheckResult.hashValue : Swift.Int
0x197dfac50  __TEXT,__text  type metadata accessor for CloudKit.CKDeviceCapabilityCheckResult
0x197f28280  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKDeviceCapabilityCheckResult
0x1e3ca6608  __AUTH_CONST,__const  type metadata for CloudKit.CKDeviceCapabilityCheckResult
0x197ef1e20  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapabilityCheckResult : Swift.Hashable in CloudKit
0x197ef1e60  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapabilityCheckResult : Swift.Equatable in CloudKit
0x197e195a4  __TEXT,__text  static CloudKit.CKShareTransferRepresentation.ExportedShare.prepareShare(container: __C.CKContainer, allowedSharingOptions: __C.CKAllowedSharingOptions, preparationHandler: @Sendable () async throws -> __C.CKShare) -> CloudKit.CKShareTransferRepresentation<A>.ExportedShare
0x197e19ab8  __TEXT,__text  static CloudKit.CKShareTransferRepresentation.ExportedShare.transferRepresentation.getter : some
0x197ef4818  __TEXT,__const  property descriptor for static CloudKit.CKShareTransferRepresentation.ExportedShare.transferRepresentation : some
0x197f28994  __TEXT,__constg_swiftt  opaque type descriptor for <<opaque return type of static CloudKit.CKShareTransferRepresentation.ExportedShare.transferRepresentation : some>>
0x197e19750  __TEXT,__text  static CloudKit.CKShareTransferRepresentation.ExportedShare.existing(_: __C.CKShare, container: __C.CKContainer, allowedSharingOptions: __C.CKAllowedSharingOptions) -> CloudKit.CKShareTransferRepresentation<A>.ExportedShare
0x197e19470  __TEXT,__text  type metadata accessor for CloudKit.CKShareTransferRepresentation.ExportedShare
0x197f28924  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKShareTransferRepresentation.ExportedShare
0x197ef4790  __TEXT,__const  protocol conformance descriptor for CloudKit.CKShareTransferRepresentation<A>.ExportedShare : CoreTransferable.Transferable in CloudKit
0x197e192b4  __TEXT,__text  CloudKit.CKShareTransferRepresentation.body.getter : some
0x197ef4818  __TEXT,__const  property descriptor for CloudKit.CKShareTransferRepresentation.body : some
0x197f28960  __TEXT,__constg_swiftt  opaque type descriptor for <<opaque return type of CloudKit.CKShareTransferRepresentation.body : some>>
0x197e192ac  __TEXT,__text  CloudKit.CKShareTransferRepresentation.init(exporter: @Sendable (A) throws -> CloudKit.CKShareTransferRepresentation<A>.ExportedShare) -> CloudKit.CKShareTransferRepresentation<A>
0x197e1b45c  __TEXT,__text  type metadata accessor for CloudKit.CKShareTransferRepresentation
0x197f288e8  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKShareTransferRepresentation
0x197ef47c8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKShareTransferRepresentation<A> : CoreTransferable.TransferRepresentation in CloudKit
0x197df77a0  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckOptions.init(excludeDevicesWithoutCapabilityCheckingSupport: Swift.Bool, excludeZoneAccessBefore: Foundation.Date?) -> CloudKit.CKDeviceCapabilityCheckOptions
0x197df7444  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckOptions.excludeDevicesWithoutCapabilityCheckingSupport.modify : Swift.Bool
0x197df7434  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckOptions.excludeDevicesWithoutCapabilityCheckingSupport.getter : Swift.Bool
0x197ef1e90  __TEXT,__const  property descriptor for CloudKit.CKDeviceCapabilityCheckOptions.excludeDevicesWithoutCapabilityCheckingSupport : Swift.Bool
0x197df743c  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckOptions.excludeDevicesWithoutCapabilityCheckingSupport.setter : Swift.Bool
0x197df75e8  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckOptions.excludeZoneAccessBefore.modify : Foundation.Date?
0x197df7464  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckOptions.excludeZoneAccessBefore.getter : Foundation.Date?
0x1e0c4132c  __DATA_CONST,__const  property descriptor for CloudKit.CKDeviceCapabilityCheckOptions.excludeZoneAccessBefore : Foundation.Date?
0x197df7588  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckOptions.excludeZoneAccessBefore.setter : Foundation.Date?
0x197df7800  __TEXT,__text  static CloudKit.CKDeviceCapabilityCheckOptions.== infix(CloudKit.CKDeviceCapabilityCheckOptions, CloudKit.CKDeviceCapabilityCheckOptions) -> Swift.Bool
0x197df789c  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckOptions.hash(into: inout Swift.Hasher) -> ()
0x197df78f0  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckOptions.hashValue.getter : Swift.Int
0x197ef1e88  __TEXT,__const  property descriptor for CloudKit.CKDeviceCapabilityCheckOptions.hashValue : Swift.Int
0x197df7794  __TEXT,__text  CloudKit.CKDeviceCapabilityCheckOptions.init() -> CloudKit.CKDeviceCapabilityCheckOptions
0x197dfaadc  __TEXT,__text  type metadata accessor for CloudKit.CKDeviceCapabilityCheckOptions
0x197f28264  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKDeviceCapabilityCheckOptions
0x1e3ca64d8  __AUTH_CONST,__const  type metadata for CloudKit.CKDeviceCapabilityCheckOptions
0x197ef1db8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapabilityCheckOptions : Swift.Hashable in CloudKit
0x197ef1df8  __TEXT,__const  protocol conformance descriptor for CloudKit.CKDeviceCapabilityCheckOptions : Swift.Equatable in CloudKit
0x197e028ac  __TEXT,__text  CloudKit.CKFeatureNameOrValueMaxUTF8Bytes.getter : Swift.Int
0x197bec770  __TEXT,__text  CloudKit.CKLog.getter : os.Logger
0x197ec0658  __TEXT,__text  CloudKit.CKLogOp.getter : os.Logger
0x197ec04ec  __TEXT,__text  CloudKit.CKLogPCS.getter : os.Logger
0x197ec0528  __TEXT,__text  CloudKit.CKLogSQL.getter : os.Logger
0x197ec05e4  __TEXT,__text  CloudKit.CKLogMMCS.getter : os.Logger
0x197e1d83c  __TEXT,__text  CloudKit.CKVersion.description.getter : Swift.String
0x197ef4a78  __TEXT,__const  property descriptor for CloudKit.CKVersion.description : Swift.String
0x197e1ca44  __TEXT,__text  static CloudKit.CKVersion.< infix(CloudKit.CKVersion, CloudKit.CKVersion) -> Swift.Bool
0x197e1c928  __TEXT,__text  static CloudKit.CKVersion.== infix(CloudKit.CKVersion, CloudKit.CKVersion) -> Swift.Bool
0x197e1d348  __TEXT,__text  CloudKit.CKVersion.init(from: Swift.Decoder) throws -> CloudKit.CKVersion
0x197e1d570  __TEXT,__text  CloudKit.CKVersion.hash(into: inout Swift.Hasher) -> ()
0x197e1d16c  __TEXT,__text  CloudKit.CKVersion.encode(to: Swift.Encoder) throws -> ()
0x197e1d638  __TEXT,__text  CloudKit.CKVersion.hashValue.getter : Swift.Int
0x197ef4a78  __TEXT,__const  property descriptor for CloudKit.CKVersion.hashValue : Swift.Int
0x197e1ec50  __TEXT,__text  type metadata accessor for CloudKit.CKVersion
0x197f289c8  __TEXT,__constg_swiftt  nominal type descriptor for CloudKit.CKVersion
0x1e3ca6148  __AUTH_CONST,__const  type metadata for CloudKit.CKVersion
0x197ef4978  __TEXT,__const  protocol conformance descriptor for CloudKit.CKVersion : Swift.Encodable in CloudKit
0x197ef49a0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKVersion : Swift.Hashable in CloudKit
0x197ef4a08  __TEXT,__const  protocol conformance descriptor for CloudKit.CKVersion : Swift.Comparable in CloudKit
0x197ef49e0  __TEXT,__const  protocol conformance descriptor for CloudKit.CKVersion : Swift.Equatable in CloudKit
0x197ef4950  __TEXT,__const  protocol conformance descriptor for CloudKit.CKVersion : Swift.Decodable in CloudKit
0x197ef4a50  __TEXT,__const  protocol conformance descriptor for CloudKit.CKVersion : Swift.CustomStringConvertible in CloudKit
0x197dff9d0  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.description.getter : Swift.String
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.description : Swift.String
0x197dff6ac  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.clientRecord.getter : __C.CKRecord?
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.clientRecord : __C.CKRecord?
0x197dff5c8  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.serverRecord.getter : __C.CKRecord?
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.serverRecord : __C.CKRecord?
0x197dff5bc  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.ancestorRecord.getter : __C.CKRecord?
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.ancestorRecord : __C.CKRecord?
0x197dff7b0  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.underlyingError.getter : __C_Synthesized.related decl 'e' for CKUnderlyingErrorCode?
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.underlyingError : __C_Synthesized.related decl 'e' for CKUnderlyingErrorCode?
0x197dff6b8  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.retryAfterSeconds.getter : Swift.Double?
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.retryAfterSeconds : Swift.Double?
0x197dff794  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.movedDestinationID.getter : __C.CKRecordID?
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.movedDestinationID : __C.CKRecordID?
0x197dfe5ac  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.partialErrorsByItemID.getter : [Swift.AnyHashable : Swift.Error]?
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.partialErrorsByItemID : [Swift.AnyHashable : Swift.Error]?
0x197dff85c  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.underlyingFunctionError.getter : Swift.Error?
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.underlyingFunctionError : Swift.Error?
0x197dffc1c  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.underlyingSessionReadinessError.getter : CloudCoreInternal.SessionReadinessError?
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.underlyingSessionReadinessError : CloudCoreInternal.SessionReadinessError?
0x197dffdbc  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.underlyingSessionInvalidationContext.getter : CloudCoreInternal.SessionInvalidationContext?
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.underlyingSessionInvalidationContext : CloudCoreInternal.SessionInvalidationContext?
0x197dfe43c  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKErrorCode.init(_: __C.CKErrorCode, description: Swift.String, serverRecord: __C.CKRecord?) -> __C_Synthesized.related decl 'e' for CKErrorCode
0x197ef21b8  __TEXT,__const  protocol conformance descriptor for __C_Synthesized.related decl 'e' for CKErrorCode : Swift.CustomStringConvertible in CloudKit
0x197e33388  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKUnderlyingErrorCode.init(sessionReadinessError: CloudCoreInternal.SessionReadinessError, invalidationContext: CloudCoreInternal.SessionInvalidationContext) -> __C_Synthesized.related decl 'e' for CKUnderlyingErrorCode
0x197e3352c  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKUnderlyingErrorCode.init(sessionReadinessErrorBox: CloudKit.CKSessionReadinessErrorBox, invalidationContextBox: CloudKit.CKSessionInvalidationContext) -> __C_Synthesized.related decl 'e' for CKUnderlyingErrorCode
0x197dffa30  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKUnderlyingErrorCode.underlyingFunctionError.getter : Swift.Error?
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKUnderlyingErrorCode.underlyingFunctionError : Swift.Error?
0x197dffd74  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKUnderlyingErrorCode.underlyingSessionReadinessError.getter : CloudCoreInternal.SessionReadinessError?
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKUnderlyingErrorCode.underlyingSessionReadinessError : CloudCoreInternal.SessionReadinessError?
0x197dfff14  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKUnderlyingErrorCode.underlyingSessionInvalidationContext.getter : CloudCoreInternal.SessionInvalidationContext?
0x197ef21e0  __TEXT,__const  property descriptor for (extension in CloudKit):__C_Synthesized.related decl 'e' for CKUnderlyingErrorCode.underlyingSessionInvalidationContext : CloudCoreInternal.SessionInvalidationContext?
0x197dffb30  __TEXT,__text  (extension in CloudKit):__C_Synthesized.related decl 'e' for CKUnderlyingErrorCode.init(_: __C.CKUnderlyingErrorCode, description: Swift.String) -> __C_Synthesized.related decl 'e' for CKUnderlyingErrorCode
0x197ef3218  __TEXT,__const  protocol conformance descriptor for Swift.String : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca5f70  __AUTH_CONST,__const  protocol witness table for Swift.String : CloudKit.CKRecordValueProtocol in CloudKit
0x197ec3c80  __TEXT,__text  (extension in CloudKit):Swift.String.ckLowercaseHexStringWithoutSpaces() -> Swift.String
0x197ef3418  __TEXT,__const  protocol conformance descriptor for <A where A: CloudKit.CKRecordValueProtocol> [A] : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef3278  __TEXT,__const  protocol conformance descriptor for Swift.Bool : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca5f20  __AUTH_CONST,__const  protocol witness table for Swift.Bool : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef3298  __TEXT,__const  protocol conformance descriptor for Swift.Double : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca5ef8  __AUTH_CONST,__const  protocol witness table for Swift.Double : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef33f8  __TEXT,__const  protocol conformance descriptor for Swift.Float : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca5ed0  __AUTH_CONST,__const  protocol witness table for Swift.Float : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef32b8  __TEXT,__const  protocol conformance descriptor for Swift.Int : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca5ea8  __AUTH_CONST,__const  protocol witness table for Swift.Int : CloudKit.CKRecordValueProtocol in CloudKit
0x197de1bac  __TEXT,__text  (extension in CloudKit):__C.CKDatabase._recordZone(for: __C.CKRecordZoneID) async throws -> __C.CKRecordZone
0x197ef0d18  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase._recordZone(for: __C.CKRecordZoneID) async throws -> __C.CKRecordZone
0x197e21578  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.codeService(configuration: CloudKit.CKCodeServiceConfiguration) throws -> __C.CKCodeService
0x197bc8140  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.recordZones(for: [__C.CKRecordZoneID]) async throws -> [__C.CKRecordZoneID : Swift.Result<__C.CKRecordZone, Swift.Error>]
0x197ef0d28  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.recordZones(for: [__C.CKRecordZoneID]) async throws -> [__C.CKRecordZoneID : Swift.Result<__C.CKRecordZone, Swift.Error>]
0x197dde20c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.subscription(for: Swift.String) async throws -> __C.CKSubscription
0x197ef0c58  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.subscription(for: Swift.String) async throws -> __C.CKSubscription
0x197de052c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase._deleteRecord(withID: __C.CKRecordID) async throws -> __C.CKRecordID
0x197ef0cc0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase._deleteRecord(withID: __C.CKRecordID) async throws -> __C.CKRecordID
0x197de08d8  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.modifyRecords(saving: [__C.CKRecord], deleting: [__C.CKRecordID], savePolicy: __C.CKRecordSavePolicy, atomically: Swift.Bool, completionHandler: (Swift.Result<(saveResults: [__C.CKRecordID : Swift.Result<__C.CKRecord, Swift.Error>], deleteResults: [__C.CKRecord
0x197de0a8c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.modifyRecords(saving: [__C.CKRecord], deleting: [__C.CKRecordID], savePolicy: __C.CKRecordSavePolicy, atomically: Swift.Bool) async throws -> (saveResults: [__C.CKRecordID : Swift.Result<__C.CKRecord, Swift.Error>], deleteResults: [__C.CKRecordID : Swift.Result
0x197ef0cd0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.modifyRecords(saving: [__C.CKRecord], deleting: [__C.CKRecordID], savePolicy: __C.CKRecordSavePolicy, atomically: Swift.Bool) async throws -> (saveResults: [__C.CKRecordID : Swift.Result<__C.CKRecord, Swift.Error>], deleteResults: [__C
0x197de2fc0  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.subscriptions(for: [Swift.String]) async throws -> [Swift.String : Swift.Result<__C.CKSubscription, Swift.Error>]
0x197ef0d70  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.subscriptions(for: [Swift.String]) async throws -> [Swift.String : Swift.Result<__C.CKSubscription, Swift.Error>]
0x197de49d8  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification.description.getter : Swift.String
0x197ef10f8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification.description : Swift.String
0x197de461c  __TEXT,__text  static (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification.== infix((extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification, (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification) -> Swift.Bool
0x197de464c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification.hash(into: inout Swift.Hasher) -> ()
0x197de356c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification.init(zoneID: __C.CKRecordZoneID) -> (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification
0x197de3538  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification.zoneID.modify : __C.CKRecordZoneID
0x197de350c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification.zoneID.getter : __C.CKRecordZoneID
0x1e0c41260  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification.zoneID : __C.CKRecordZoneID
0x197de3510  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification.zoneID.setter : __C.CKRecordZoneID
0x197de4670  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification.hashValue.getter : Swift.Int
0x197ef10f8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification.hashValue : Swift.Int
0x197deb59c  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification
0x197f280e0  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification
0x1e3ca5e70  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification
0x197ef0ee0  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification : Swift.Hashable in CloudKit
0x197ef0eb8  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification : Swift.Equatable in CloudKit
0x197ef1058  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification : Swift.CustomStringConvertible in CloudKit
0x197de4a70  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.description.getter : Swift.String
0x197ef10f8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.description : Swift.String
0x197de4674  __TEXT,__text  static (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.== infix((extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion, (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion) -> Swift.Bool
0x197de46c0  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.hash(into: inout Swift.Hasher) -> ()
0x197ef1180  __TEXT,__const  enum case for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason.encryptedDataReset((extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason.Type) -> (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason
0x197de3724  __TEXT,__text  static (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason.== infix((extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason, (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason) -> Swift.Bool
0x197de3738  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason.hash(into: inout Swift.Hasher) -> ()
0x197ef117c  __TEXT,__const  enum case for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason.purged((extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason.Type) -> (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason
0x197ef1178  __TEXT,__const  enum case for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason.deleted((extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason.Type) -> (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason
0x197de3764  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason.hashValue.getter : Swift.Int
0x197ef10f8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason.hashValue : Swift.Int
0x197deb704  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason
0x197f28118  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason
0x1e3ca5df8  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason
0x197ef0e50  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason : Swift.Hashable in CloudKit
0x197ef0e90  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason : Swift.Equatable in CloudKit
0x197de37f4  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.purged.getter : Swift.Bool
0x197ef10f8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.purged : Swift.Bool
0x197de36e8  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.reason.modify : (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason
0x197de365c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.reason.getter : (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason
0x1e0c41280  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.reason : (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason
0x197de36dc  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.reason.setter : (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason
0x197de3804  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.init(zoneID: __C.CKRecordZoneID, reason: (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.Reason) -> (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion
0x197de3610  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.zoneID.modify : __C.CKRecordZoneID
0x197de3574  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.zoneID.getter : __C.CKRecordZoneID
0x1e0c41270  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.zoneID : __C.CKRecordZoneID
0x197de35e8  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.zoneID.setter : __C.CKRecordZoneID
0x197de4700  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.hashValue.getter : Swift.Int
0x197ef10f8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion.hashValue : Swift.Int
0x197deb628  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion
0x197f280fc  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion
0x1e3ca5d60  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion
0x197ef0f48  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion : Swift.Hashable in CloudKit
0x197ef0f20  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion : Swift.Equatable in CloudKit
0x197ef1080  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion : Swift.CustomStringConvertible in CloudKit
0x197deb58c  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKDatabase.DatabaseChange
0x197f280c4  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKDatabase.DatabaseChange
0x1e3ca5ce8  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKDatabase.DatabaseChange
0x197ddef28  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.configuredWith<A>(configuration: __C.CKOperationConfiguration?, group: __C.CKOperationGroup?, body: (__C.CKDatabase) throws -> A) throws -> A
0x197ddf63c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.configuredWith<A>(configuration: __C.CKOperationConfiguration?, group: __C.CKOperationGroup?, body: (__C.CKDatabase) async throws -> A) async throws -> A
0x197ef0c88  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.configuredWith<A>(configuration: __C.CKOperationConfiguration?, group: __C.CKOperationGroup?, body: (__C.CKDatabase) async throws -> A) async throws -> A
0x197de1984  __TEXT,__text  (extension in CloudKit):__C.CKDatabase._allRecordZones() async throws -> [__C.CKRecordZone]
0x197ef0d08  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase._allRecordZones() async throws -> [__C.CKRecordZone]
0x197de39b0  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.databaseChanges(since: __C.CKServerChangeToken?, resultsLimit: Swift.Int?) async throws -> (modifications: [(extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification], deletions: [(extension in CloudKit):__C.CKDatabase.DatabaseChange.Deletion], changeT
0x197ef0d90  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.databaseChanges(since: __C.CKServerChangeToken?, resultsLimit: Swift.Int?) async throws -> (modifications: [(extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification], deletions: [(extension in CloudKit):__C.CKDatabase.Databas
0x197de4054  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneModification.zone.modify : __C.CKRecordZone
0x197dee20c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneModification.zone.getter : __C.CKRecordZone
0x197ef10fc  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneModification.zone : __C.CKRecordZone
0x197dee188  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneModification.zone.setter : __C.CKRecordZone
0x197deb7e0  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneModification
0x197f28188  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneModification
0x1e3ca5c50  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneModification
0x197dee1d4  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneAttributesModification.init(zone: __C.CKRecordZone) -> (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneAttributesModification
0x197de4074  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneAttributesModification.zone.modify : __C.CKRecordZone
0x197dee210  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneAttributesModification.zone.getter : __C.CKRecordZone
0x1e0c412c0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneAttributesModification.zone : __C.CKRecordZone
0x197dee18c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneAttributesModification.zone.setter : __C.CKRecordZone
0x197deb7f0  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneAttributesModification
0x197f281a4  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneAttributesModification
0x1e3ca5bd0  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.ZoneAttributesModification
0x197de4b6c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification.description.getter : Swift.String
0x197ef10f8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification.description : Swift.String
0x197dee194  __TEXT,__text  static (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification.== infix((extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification, (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification) -> Swift.Bool
0x197dee270  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification.hash(into: inout Swift.Hasher) -> ()
0x197dee1d0  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification.init(record: __C.CKRecord) -> (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification
0x197de3d34  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification.record.modify : __C.CKRecord
0x197dee208  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification.record.getter : __C.CKRecord
0x1e0c41290  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification.record : __C.CKRecord
0x197dee184  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification.record.setter : __C.CKRecord
0x197dee258  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification.hashValue.getter : Swift.Int
0x197ef10f8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification.hashValue : Swift.Int
0x197deb7c0  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification
0x197f28150  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification
0x1e3ca5b50  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification
0x197ef0fb0  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification : Swift.Hashable in CloudKit
0x197ef0f88  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification : Swift.Equatable in CloudKit
0x197ef10a8  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Modification : Swift.CustomStringConvertible in CloudKit
0x197de3f94  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.recordType.modify : Swift.String
0x197de3eac  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.recordType.getter : Swift.String
0x1e0c412b0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.recordType : Swift.String
0x197de3f60  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.recordType.setter : Swift.String
0x197de4c14  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.description.getter : Swift.String
0x197ef10f8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.description : Swift.String
0x197de483c  __TEXT,__text  static (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.== infix((extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion, (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion) -> Swift.Bool
0x197de48d0  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.hash(into: inout Swift.Hasher) -> ()
0x197de4048  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.init(recordID: __C.CKRecordID, recordType: Swift.String) -> (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion
0x197de3df8  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.recordID.modify : __C.CKRecordID
0x197de3d5c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.recordID.getter : __C.CKRecordID
0x1e0c412a0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.recordID : __C.CKRecordID
0x197de3dd0  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.recordID.setter : __C.CKRecordID
0x197de4910  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.hashValue.getter : Swift.Int
0x197ef10f8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion.hashValue : Swift.Int
0x197deb7d0  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion
0x197f2816c  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion
0x1e3ca5ad0  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion
0x197ef1018  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion : Swift.Hashable in CloudKit
0x197ef0ff0  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion : Swift.Equatable in CloudKit
0x197ef10d0  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange.Deletion : Swift.CustomStringConvertible in CloudKit
0x197deb7b0  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange
0x197f28134  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKDatabase.RecordZoneChange
0x1e3ca5a58  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKDatabase.RecordZoneChange
0x197dddfa4  __TEXT,__text  (extension in CloudKit):__C.CKDatabase._allSubscriptions() async throws -> [__C.CKSubscription]
0x197ef0c48  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase._allSubscriptions() async throws -> [__C.CKSubscription]
0x197de2564  __TEXT,__text  (extension in CloudKit):__C.CKDatabase._deleteRecordZone(withID: __C.CKRecordZoneID) async throws -> __C.CKRecordZoneID
0x197ef0d48  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase._deleteRecordZone(withID: __C.CKRecordZoneID) async throws -> __C.CKRecordZoneID
0x197de2c60  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.modifyRecordZones(saving: [__C.CKRecordZone], deleting: [__C.CKRecordZoneID], markZonesAsUserPurged: Swift.Bool) async throws -> (saveResults: [__C.CKRecordZoneID : Swift.Result<__C.CKRecordZone, Swift.Error>], deleteResults: [__C.CKRecordZoneID : Swift.Result<
0x197ef0d68  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.modifyRecordZones(saving: [__C.CKRecordZone], deleting: [__C.CKRecordZoneID], markZonesAsUserPurged: Swift.Bool) async throws -> (saveResults: [__C.CKRecordZoneID : Swift.Result<__C.CKRecordZone, Swift.Error>], deleteResults: [__C.CKRe
0x197de290c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.modifyRecordZones(saving: [__C.CKRecordZone], deleting: [__C.CKRecordZoneID], completionHandler: (Swift.Result<(saveResults: [__C.CKRecordZoneID : Swift.Result<__C.CKRecordZone, Swift.Error>], deleteResults: [__C.CKRecordZoneID : Swift.Result<(), Swift.Error>])
0x197de2aa8  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.modifyRecordZones(saving: [__C.CKRecordZone], deleting: [__C.CKRecordZoneID]) async throws -> (saveResults: [__C.CKRecordZoneID : Swift.Result<__C.CKRecordZone, Swift.Error>], deleteResults: [__C.CKRecordZoneID : Swift.Result<(), Swift.Error>])
0x197ef0d58  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.modifyRecordZones(saving: [__C.CKRecordZone], deleting: [__C.CKRecordZoneID]) async throws -> (saveResults: [__C.CKRecordZoneID : Swift.Result<__C.CKRecordZone, Swift.Error>], deleteResults: [__C.CKRecordZoneID : Swift.Result<(), Swift
0x197de4260  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.recordZoneChanges(inZoneWith: __C.CKRecordZoneID, since: __C.CKServerChangeToken?, desiredKeys: [Swift.String]?, resultsLimit: Swift.Int?) async throws -> (modificationResultsByID: [__C.CKRecordID : Swift.Result<(extension in CloudKit):__C.CKDatabase.RecordZone
0x197ef0da0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.recordZoneChanges(inZoneWith: __C.CKRecordZoneID, since: __C.CKServerChangeToken?, desiredKeys: [Swift.String]?, resultsLimit: Swift.Int?) async throws -> (modificationResultsByID: [__C.CKRecordID : Swift.Result<(extension in CloudKit)
0x197ddeb68  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.deleteSubscription(withID: Swift.String) async throws -> Swift.String
0x197ef0c78  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.deleteSubscription(withID: Swift.String) async throws -> Swift.String
0x197de3134  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.modifySubscriptions(saving: [__C.CKSubscription], deleting: [Swift.String], completionHandler: (Swift.Result<(saveResults: [Swift.String : Swift.Result<__C.CKSubscription, Swift.Error>], deleteResults: [Swift.String : Swift.Result<(), Swift.Error>]), Swift.Erro
0x197de32b4  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.modifySubscriptions(saving: [__C.CKSubscription], deleting: [Swift.String]) async throws -> (saveResults: [Swift.String : Swift.Result<__C.CKSubscription, Swift.Error>], deleteResults: [Swift.String : Swift.Result<(), Swift.Error>])
0x197ef0d80  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.modifySubscriptions(saving: [__C.CKSubscription], deleting: [Swift.String]) async throws -> (saveResults: [Swift.String : Swift.Result<__C.CKSubscription, Swift.Error>], deleteResults: [Swift.String : Swift.Result<(), Swift.Error>])
0x197de3814  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.fetchDatabaseChanges(since: __C.CKServerChangeToken?, resultsLimit: Swift.Int?, completionHandler: (Swift.Result<(modifications: [(extension in CloudKit):__C.CKDatabase.DatabaseChange.Modification], deletions: [(extension in CloudKit):__C.CKDatabase.DatabaseCha
0x197ddda0c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.undeprecated_perform(_: __C.CKQuery, inZoneWith: __C.CKRecordZoneID?, completionHandler: ([__C.CKRecord]?, Swift.Error?) -> ()) -> ()
0x197de409c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.fetchRecordZoneChanges(inZoneWith: __C.CKRecordZoneID, since: __C.CKServerChangeToken?, desiredKeys: [Swift.String]?, resultsLimit: Swift.Int?, completionHandler: (Swift.Result<(modificationResultsByID: [__C.CKRecordID : Swift.Result<(extension in CloudKit):__C
0x197dee5ec  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.FetchAssetConfiguration.progressReporter.getter : Foundation.ProgressReporter
0x197ef15d4  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.FetchAssetConfiguration.progressReporter : Foundation.ProgressReporter
0x197dee610  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.FetchAssetConfiguration.init(assetID: (extension in CloudKit):__C.CKAsset.ID) -> (extension in CloudKit):__C.CKDatabase.FetchAssetConfiguration
0x197dee598  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.FetchAssetConfiguration.assetID.getter : (extension in CloudKit):__C.CKAsset.ID
0x197ef15d0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabase.FetchAssetConfiguration.assetID : (extension in CloudKit):__C.CKAsset.ID
0x197df0884  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKDatabase.FetchAssetConfiguration
0x197f281c0  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKDatabase.FetchAssetConfiguration
0x1e3ca59c0  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKDatabase.FetchAssetConfiguration
0x197df7eb8  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.checkSupportedDeviceCapabilities(_: CloudKit.CKDeviceCapabilitySet, in: __C.CKRecordZone, options: CloudKit.CKDeviceCapabilityCheckOptions?) async throws -> CloudKit.CKDeviceCapabilityCheckResult
0x197ef19c0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.checkSupportedDeviceCapabilities(_: CloudKit.CKDeviceCapabilitySet, in: __C.CKRecordZone, options: CloudKit.CKDeviceCapabilityCheckOptions?) async throws -> CloudKit.CKDeviceCapabilityCheckResult
0x197de21d0  __TEXT,__text  (extension in CloudKit):__C.CKDatabase._save(__C.CKRecordZone) async throws -> __C.CKRecordZone
0x197ef0d38  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase._save(__C.CKRecordZone) async throws -> __C.CKRecordZone
0x197dde69c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase._save(__C.CKSubscription) async throws -> __C.CKSubscription
0x197ef0c68  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase._save(__C.CKSubscription) async throws -> __C.CKSubscription
0x197de0194  __TEXT,__text  (extension in CloudKit):__C.CKDatabase._save(__C.CKRecord) async throws -> __C.CKRecord
0x197ef0cb0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase._save(__C.CKRecord) async throws -> __C.CKRecord
0x197de1400  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.fetch(withCursor: __C.CKQueryCursor, desiredKeys: [Swift.String]?, resultsLimit: Swift.Int, completionHandler: (Swift.Result<(matchResults: [(__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>)], queryCursor: __C.CKQueryCursor?), Swift.Error>) -> ()) -> ()
0x197ddfce4  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.fetch(withRecordIDs: [__C.CKRecordID], desiredKeys: [Swift.String]?, completionHandler: (Swift.Result<[__C.CKRecordID : Swift.Result<__C.CKRecord, Swift.Error>], Swift.Error>) -> ()) -> ()
0x197de2024  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.fetch(withRecordZoneIDs: [__C.CKRecordZoneID], completionHandler: (Swift.Result<[__C.CKRecordZoneID : Swift.Result<__C.CKRecordZone, Swift.Error>], Swift.Error>) -> ()) -> ()
0x197dde170  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.fetch(withSubscriptionID: Swift.String, completionHandler: (__C.CKSubscription?, Swift.Error?) -> ()) -> ()
0x197de2e30  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.fetch(withSubscriptionIDs: [Swift.String], completionHandler: (Swift.Result<[Swift.String : Swift.Result<__C.CKSubscription, Swift.Error>], Swift.Error>) -> ()) -> ()
0x197de126c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.fetch(withQuery: __C.CKQuery, inZoneWith: __C.CKRecordZoneID?, desiredKeys: [Swift.String]?, resultsLimit: Swift.Int, completionHandler: (Swift.Result<(matchResults: [(__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>)], queryCursor: __C.CKQueryCursor?), 
0x197dee778  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.assets(for: [(extension in CloudKit):__C.CKAsset.ID], subprogress: __owned Foundation.Subprogress?) -> any Swift.AsyncSequence<Self.Swift.AsyncSequence.Element == (assetID: (extension in CloudKit):__C.CKAsset.ID, result: Swift.Result<__C.CKAsset, Swift.Error>),
0x197deec1c  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.assets(with: [(extension in CloudKit):__C.CKDatabase.FetchAssetConfiguration], subprogress: __owned Foundation.Subprogress?) -> any Swift.AsyncSequence<Self.Swift.AsyncSequence.Element == (assetID: (extension in CloudKit):__C.CKAsset.ID, result: Swift.Result<__
0x197ddea48  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.delete(withSubscriptionID: Swift.String, completionHandler: (Swift.String?, Swift.Error?) -> ()) -> ()
0x197ddf958  __TEXT,__text  (extension in CloudKit):__C.CKDatabase._record(for: __C.CKRecordID) async throws -> __C.CKRecord
0x197ef0c90  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase._record(for: __C.CKRecordID) async throws -> __C.CKRecord
0x197de1718  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.records(continuingMatchFrom: __C.CKQueryCursor, desiredKeys: [Swift.String]?, resultsLimit: Swift.Int) async throws -> (matchResults: [(__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>)], queryCursor: __C.CKQueryCursor?)
0x197ef0cf8  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.records(continuingMatchFrom: __C.CKQueryCursor, desiredKeys: [Swift.String]?, resultsLimit: Swift.Int) async throws -> (matchResults: [(__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>)], queryCursor: __C.CKQueryCursor?)
0x197ddfdec  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.records(for: [__C.CKRecordID], desiredKeys: [Swift.String]?) async throws -> [__C.CKRecordID : Swift.Result<__C.CKRecord, Swift.Error>]
0x197ef0ca0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.records(for: [__C.CKRecordID], desiredKeys: [Swift.String]?) async throws -> [__C.CKRecordID : Swift.Result<__C.CKRecord, Swift.Error>]
0x197ddddc4  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.records(matching: __C.CKQuery, inZoneWith: __C.CKRecordZoneID?, desiredKeys: [Swift.String]?, resultsLimit: Swift.Int) async throws -> (matchResults: [(__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>)], queryCursor: __C.CKQueryCursor?)
0x197ef0c38  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.records(matching: __C.CKQuery, inZoneWith: __C.CKRecordZoneID?, desiredKeys: [Swift.String]?, resultsLimit: Swift.Int) async throws -> (matchResults: [(__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>)], queryCursor: __C.CKQuery
0x197dddb38  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.records(matching: __C.CKQuery, inZoneWith: __C.CKRecordZoneID?) async throws -> [__C.CKRecord]
0x197ef0c30  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.records(matching: __C.CKQuery, inZoneWith: __C.CKRecordZoneID?) async throws -> [__C.CKRecord]
0x197de0e08  __TEXT,__text  (extension in CloudKit):__C.CKDatabase.signature(for: __C.CKAsset) async throws -> (extension in CloudKit):__C.CKAsset.Signature
0x197ef0ce0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabase.signature(for: __C.CKAsset) async throws -> (extension in CloudKit):__C.CKAsset.Signature
0x197c3458c  __TEXT,__text  (extension in CloudKit):__C.CKRecordID.init(recordName: Swift.String, zoneID: __C.CKRecordZoneID) -> __C.CKRecordID
0x197e0e32c  __TEXT,__text  (extension in CloudKit):__C.CKRecordID.init(from: Swift.Decoder) throws -> __C.CKRecordID
0x197e0e0f0  __TEXT,__text  (extension in CloudKit):__C.CKRecordID.encode(to: Swift.Encoder) throws -> ()
0x197ef307c  __TEXT,__const  protocol conformance descriptor for __C.CKRecordID : Swift.Encodable in CloudKit
0x197ef3054  __TEXT,__const  protocol conformance descriptor for __C.CKRecordID : Swift.Decodable in CloudKit
0x197ef356c  __TEXT,__const  protocol conformance descriptor for __C.CLLocation : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca5870  __AUTH_CONST,__const  protocol witness table for __C.CLLocation : CloudKit.CKRecordValueProtocol in CloudKit
0x197dd4d00  __TEXT,__text  (extension in CloudKit):__C.CKContainer.leaveShare(__C.CKShare) async throws -> ()
0x197ef08e0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.leaveShare(__C.CKShare) async throws -> ()
0x197ddbbd4  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKContainer.Application
0x197f28064  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKContainer.Application
0x1e3ca5830  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKContainer.Application
0x197dd4af0  __TEXT,__text  (extension in CloudKit):__C.CKContainer.leaveShares(shareIDs: [__C.CKRecordID]) async throws -> [__C.CKRecordID : Swift.Result<(), Swift.Error>]
0x197ef08d0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.leaveShares(shareIDs: [__C.CKRecordID]) async throws -> [__C.CKRecordID : Swift.Result<(), Swift.Error>]
0x197dd498c  __TEXT,__text  (extension in CloudKit):__C.CKContainer.leaveShares(_: [__C.CKRecordID], completionHandler: @Sendable (Swift.Result<[__C.CKRecordID : Swift.Result<(), Swift.Error>], Swift.Error>) -> ()) -> ()
0x197dd0fa4  __TEXT,__text  (extension in CloudKit):__C.CKContainer._userIdentity(forPhoneNumber: Swift.String) async throws -> __C.CKUserIdentity?
0x197ef07b8  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer._userIdentity(forPhoneNumber: Swift.String) async throws -> __C.CKUserIdentity?
0x197dd0b90  __TEXT,__text  (extension in CloudKit):__C.CKContainer._userIdentity(forEmailAddress: Swift.String) async throws -> __C.CKUserIdentity?
0x197ef0798  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer._userIdentity(forEmailAddress: Swift.String) async throws -> __C.CKUserIdentity?
0x197dd1658  __TEXT,__text  (extension in CloudKit):__C.CKContainer._userIdentity(forUserRecordID: __C.CKRecordID) async throws -> __C.CKUserIdentity?
0x197ef07d8  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer._userIdentity(forUserRecordID: __C.CKRecordID) async throws -> __C.CKUserIdentity?
0x197ddb014  __TEXT,__text  static (extension in CloudKit):__C.CKContainer.AccountChanged.makeMessage(Foundation.Notification) -> (extension in CloudKit):__C.CKContainer.AccountChanged?
0x197ddafc8  __TEXT,__text  static (extension in CloudKit):__C.CKContainer.AccountChanged.makeNotification((extension in CloudKit):__C.CKContainer.AccountChanged) -> Foundation.Notification
0x197ddafa8  __TEXT,__text  static (extension in CloudKit):__C.CKContainer.AccountChanged.name.getter : __C.NSNotificationName
0x197ef0998  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKContainer.AccountChanged.name : __C.NSNotificationName
0x197ddbbe4  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKContainer.AccountChanged
0x197f28080  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKContainer.AccountChanged
0x1e3ca57a0  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKContainer.AccountChanged
0x197ef0918  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKContainer.AccountChanged : (extension in Foundation):__C.NSNotificationCenter.AsyncMessage in CloudKit
0x197dd3640  __TEXT,__text  (extension in CloudKit):__C.CKContainer._shareMetadata(for: Foundation.URL) async throws -> __C.CKShareMetadata
0x197ef0868  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer._shareMetadata(for: Foundation.URL) async throws -> __C.CKShareMetadata
0x197dd0480  __TEXT,__text  (extension in CloudKit):__C.CKContainer.configuredWith<A>(configuration: __C.CKOperationConfiguration?, group: __C.CKOperationGroup?, body: (__C.CKContainer) throws -> A) throws -> A
0x197dd0560  __TEXT,__text  (extension in CloudKit):__C.CKContainer.configuredWith<A>(configuration: __C.CKOperationConfiguration?, group: __C.CKOperationGroup?, body: (__C.CKContainer) async throws -> A) async throws -> A
0x197ef0780  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.configuredWith<A>(configuration: __C.CKOperationConfiguration?, group: __C.CKOperationGroup?, body: (__C.CKContainer) async throws -> A) async throws -> A
0x197dd3fcc  __TEXT,__text  (extension in CloudKit):__C.CKContainer.shareMetadatas(for: [Foundation.URL], invitationTokensByShareURL: [Foundation.URL : __C.CKDeviceToDeviceShareInvitationToken]) async throws -> [Foundation.URL : Swift.Result<__C.CKShareMetadata, Swift.Error>]
0x197ef0888  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.shareMetadatas(for: [Foundation.URL], invitationTokensByShareURL: [Foundation.URL : __C.CKDeviceToDeviceShareInvitationToken]) async throws -> [Foundation.URL : Swift.Result<__C.CKShareMetadata, Swift.Error>]
0x197dd3c38  __TEXT,__text  (extension in CloudKit):__C.CKContainer.shareMetadatas(for: [Foundation.URL]) async throws -> [Foundation.URL : Swift.Result<__C.CKShareMetadata, Swift.Error>]
0x197ef0878  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.shareMetadatas(for: [Foundation.URL]) async throws -> [Foundation.URL : Swift.Result<__C.CKShareMetadata, Swift.Error>]
0x197dd1398  __TEXT,__text  (extension in CloudKit):__C.CKContainer.userIdentities(forPhoneNumbers: [Swift.String]) async throws -> [Swift.String : __C.CKUserIdentity]
0x197ef07c8  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.userIdentities(forPhoneNumbers: [Swift.String]) async throws -> [Swift.String : __C.CKUserIdentity]
0x197dd194c  __TEXT,__text  (extension in CloudKit):__C.CKContainer.userIdentities(forUserRecordIDs: [__C.CKRecordID]) async throws -> [__C.CKRecordID : __C.CKUserIdentity]
0x197ef07e8  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.userIdentities(forUserRecordIDs: [__C.CKRecordID]) async throws -> [__C.CKRecordID : __C.CKUserIdentity]
0x197dd0ce4  __TEXT,__text  (extension in CloudKit):__C.CKContainer.userIdentities(forEmailAddresses: [Swift.String]) async throws -> [Swift.String : __C.CKUserIdentity]
0x197ef07a8  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.userIdentities(forEmailAddresses: [Swift.String]) async throws -> [Swift.String : __C.CKUserIdentity]
0x197ddce74  __TEXT,__text  static (extension in CloudKit):__C.CKContainer.IdentityUpdated.makeMessage(Foundation.Notification) -> (extension in CloudKit):__C.CKContainer.IdentityUpdated?
0x197ddb06c  __TEXT,__text  static (extension in CloudKit):__C.CKContainer.IdentityUpdated.makeNotification((extension in CloudKit):__C.CKContainer.IdentityUpdated) -> Foundation.Notification
0x197ddb05c  __TEXT,__text  static (extension in CloudKit):__C.CKContainer.IdentityUpdated.name.getter : __C.NSNotificationName
0x197ef0998  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKContainer.IdentityUpdated.name : __C.NSNotificationName
0x197ddbc90  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKContainer.IdentityUpdated
0x197f2809c  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKContainer.IdentityUpdated
0x1e3ca5728  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKContainer.IdentityUpdated
0x197ef0958  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKContainer.IdentityUpdated : (extension in Foundation):__C.NSNotificationCenter.AsyncMessage in CloudKit
0x197dd5820  __TEXT,__text  (extension in CloudKit):__C.CKContainer.exportedAssetID(for: (extension in CloudKit):__C.CKAsset.ID) async throws -> (extension in CloudKit):__C.CKAsset.ExportedAssetID
0x197ef0908  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.exportedAssetID(for: (extension in CloudKit):__C.CKAsset.ID) async throws -> (extension in CloudKit):__C.CKAsset.ExportedAssetID
0x197dd2338  __TEXT,__text  (extension in CloudKit):__C.CKContainer._shareParticipant(forPhoneNumber: Swift.String) async throws -> __C.CKShareParticipant
0x197ef0818  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer._shareParticipant(forPhoneNumber: Swift.String) async throws -> __C.CKShareParticipant
0x197dd1c1c  __TEXT,__text  (extension in CloudKit):__C.CKContainer._shareParticipant(forEmailAddress: Swift.String) async throws -> __C.CKShareParticipant
0x197ef07f8  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer._shareParticipant(forEmailAddress: Swift.String) async throws -> __C.CKShareParticipant
0x197dd2c18  __TEXT,__text  (extension in CloudKit):__C.CKContainer._shareParticipant(forUserRecordID: __C.CKRecordID) async throws -> __C.CKShareParticipant
0x197ef0838  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer._shareParticipant(forUserRecordID: __C.CKRecordID) async throws -> __C.CKShareParticipant
0x197dd272c  __TEXT,__text  (extension in CloudKit):__C.CKContainer.shareParticipants(forPhoneNumbers: [Swift.String]) async throws -> [Swift.String : Swift.Result<__C.CKShareParticipant, Swift.Error>]
0x197ef0828  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.shareParticipants(forPhoneNumbers: [Swift.String]) async throws -> [Swift.String : Swift.Result<__C.CKShareParticipant, Swift.Error>]
0x197dd2fd0  __TEXT,__text  (extension in CloudKit):__C.CKContainer.shareParticipants(forUserRecordIDs: [__C.CKRecordID]) async throws -> [__C.CKRecordID : Swift.Result<__C.CKShareParticipant, Swift.Error>]
0x197ef0848  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.shareParticipants(forUserRecordIDs: [__C.CKRecordID]) async throws -> [__C.CKRecordID : Swift.Result<__C.CKShareParticipant, Swift.Error>]
0x197dd1e4c  __TEXT,__text  (extension in CloudKit):__C.CKContainer.shareParticipants(forEmailAddresses: [Swift.String]) async throws -> [Swift.String : Swift.Result<__C.CKShareParticipant, Swift.Error>]
0x197ef0808  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.shareParticipants(forEmailAddresses: [Swift.String]) async throws -> [Swift.String : Swift.Result<__C.CKShareParticipant, Swift.Error>]
0x197dd34f8  __TEXT,__text  (extension in CloudKit):__C.CKContainer.shareParticipants(for: [__C.CKUserIdentityLookupInfo]) async throws -> [__C.CKUserIdentityLookupInfo : Swift.Result<__C.CKShareParticipant, Swift.Error>]
0x197ef0858  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.shareParticipants(for: [__C.CKUserIdentityLookupInfo]) async throws -> [__C.CKUserIdentityLookupInfo : Swift.Result<__C.CKShareParticipant, Swift.Error>]
0x197dd0034  __TEXT,__text  (extension in CloudKit):__C.CKContainer.longLivedOperation(for: Swift.String) async throws -> __C.CKOperation?
0x197ef0770  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.longLivedOperation(for: Swift.String) async throws -> __C.CKOperation?
0x197dd483c  __TEXT,__text  (extension in CloudKit):__C.CKContainer.requestShareAccess(for: [Foundation.URL]) async throws -> [Foundation.URL : Swift.Result<(), Swift.Error>]
0x197ef08c0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.requestShareAccess(for: [Foundation.URL]) async throws -> [Foundation.URL : Swift.Result<(), Swift.Error>]
0x197dd3a40  __TEXT,__text  (extension in CloudKit):__C.CKContainer.fetchShareMetadatas(for: [Foundation.URL], completionHandler: (Swift.Result<[Foundation.URL : Swift.Result<__C.CKShareMetadata, Swift.Error>], Swift.Error>) -> ()) -> ()
0x197dd1880  __TEXT,__text  (extension in CloudKit):__C.CKContainer.discoverUserIdentities(forUserRecordIDs: [__C.CKRecordID], completionHandler: (Swift.Result<[__C.CKRecordID : __C.CKUserIdentity], Swift.Error>) -> ()) -> ()
0x197dd12cc  __TEXT,__text  (extension in CloudKit):__C.CKContainer.discoverUserIdentities(forPhoneNumbers: [Swift.String], completionHandler: (Swift.Result<[Swift.String : __C.CKUserIdentity], Swift.Error>) -> ()) -> ()
0x197dd0ac4  __TEXT,__text  (extension in CloudKit):__C.CKContainer.discoverUserIdentities(forEmailAddresses: [Swift.String], completionHandler: (Swift.Result<[Swift.String : __C.CKUserIdentity], Swift.Error>) -> ()) -> ()
0x197dd2660  __TEXT,__text  (extension in CloudKit):__C.CKContainer.fetchShareParticipants(forPhoneNumbers: [Swift.String], completionHandler: (Swift.Result<[Swift.String : Swift.Result<__C.CKShareParticipant, Swift.Error>], Swift.Error>) -> ()) -> ()
0x197dd2f04  __TEXT,__text  (extension in CloudKit):__C.CKContainer.fetchShareParticipants(forUserRecordIDs: [__C.CKRecordID], completionHandler: (Swift.Result<[__C.CKRecordID : Swift.Result<__C.CKShareParticipant, Swift.Error>], Swift.Error>) -> ()) -> ()
0x197dd1d80  __TEXT,__text  (extension in CloudKit):__C.CKContainer.fetchShareParticipants(forEmailAddresses: [Swift.String], completionHandler: (Swift.Result<[Swift.String : Swift.Result<__C.CKShareParticipant, Swift.Error>], Swift.Error>) -> ()) -> ()
0x197dcff8c  __TEXT,__text  (extension in CloudKit):__C.CKContainer.fetchLongLivedOperation(withID: Swift.String, completionHandler: (__C.CKOperation?, Swift.Error?) -> ()) -> ()
0x197dcfba8  __TEXT,__text  (extension in CloudKit):__C.CKContainer.allLongLivedOperationIDs() async throws -> [Swift.String]
0x197ef0760  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.allLongLivedOperationIDs() async throws -> [Swift.String]
0x197dd52d8  __TEXT,__text  (extension in CloudKit):__C.CKContainer.fetchOrgAdminUserRecordID() async throws -> __C.CKRecordID?
0x197ef08f0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.fetchOrgAdminUserRecordID() async throws -> __C.CKRecordID?
0x197dcfa9c  __TEXT,__text  (extension in CloudKit):__C.CKContainer.fetchAllLongLivedOperationIDs(completionHandler: ([Swift.String]?, Swift.Error?) -> ()) -> ()
0x197dd085c  __TEXT,__text  (extension in CloudKit):__C.CKContainer._allUserIdentitiesFromContacts() async throws -> [__C.CKUserIdentity]
0x197ef0788  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer._allUserIdentitiesFromContacts() async throws -> [__C.CKUserIdentity]
0x197dd4404  __TEXT,__text  (extension in CloudKit):__C.CKContainer.accept(_: [__C.CKShareMetadata], completionHandler: (Swift.Result<[__C.CKShareMetadata : Swift.Result<__C.CKShare, Swift.Error>], Swift.Error>) -> ()) -> ()
0x197dd44d0  __TEXT,__text  (extension in CloudKit):__C.CKContainer.accept([__C.CKShareMetadata]) async throws -> [__C.CKShareMetadata : Swift.Result<__C.CKShare, Swift.Error>]
0x197ef08a0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.accept([__C.CKShareMetadata]) async throws -> [__C.CKShareMetadata : Swift.Result<__C.CKShare, Swift.Error>]
0x197dd4074  __TEXT,__text  (extension in CloudKit):__C.CKContainer._accept(__C.CKShareMetadata) async throws -> __C.CKShare
0x197ef0890  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer._accept(__C.CKShareMetadata) async throws -> __C.CKShare
0x197dd4620  __TEXT,__text  (extension in CloudKit):__C.CKContainer.decline(_: [__C.CKShareMetadata], completionHandler: @Sendable (Swift.Result<[__C.CKShareMetadata : Swift.Result<(), Swift.Error>], Swift.Error>) -> ()) -> ()
0x197dd46ec  __TEXT,__text  (extension in CloudKit):__C.CKContainer.decline([__C.CKShareMetadata]) async throws -> [__C.CKShareMetadata : Swift.Result<(), Swift.Error>]
0x197ef08b0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKContainer.decline([__C.CKShareMetadata]) async throws -> [__C.CKShareMetadata : Swift.Result<(), Swift.Error>]
0x197e4466c  __TEXT,__text  (extension in CloudKit):__C.CKOperation.operationID.getter : Swift.String
0x197ef5b48  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKOperation.operationID : Swift.String
0x197ef3538  __TEXT,__const  protocol conformance descriptor for __C.CKReference : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca5698  __AUTH_CONST,__const  protocol witness table for __C.CKReference : CloudKit.CKRecordValueProtocol in CloudKit
0x197e077b4  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.requiredFeatures.modify : CloudKit.CKRequiredFeatureSet
0x197e07680  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.requiredFeatures.getter : CloudKit.CKRequiredFeatureSet
0x1e0c41408  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKRecordZone.requiredFeatures : CloudKit.CKRequiredFeatureSet
0x197e07740  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.requiredFeatures.setter : CloudKit.CKRequiredFeatureSet
0x197e123e4  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.parent.modify : (extension in CloudKit):__C.CKRecordZone.Reference?
0x197e122d0  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.parent.getter : (extension in CloudKit):__C.CKRecordZone.Reference?
0x1e0c41490  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKRecordZone.parent : (extension in CloudKit):__C.CKRecordZone.Reference?
0x197e12354  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.parent.setter : (extension in CloudKit):__C.CKRecordZone.Reference?
0x197e11ee0  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.Reference.description.getter : Swift.String
0x197e11fec  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.Reference.copy(with: ObjectiveC.NSZone?) -> Any
0x197e12258  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.Reference.hash.getter : Swift.Int
0x197e11dc8  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.Reference.__allocating_init(zone: __C.CKRecordZone, action: (extension in CloudKit):__C.CKRecordZone.Reference.Action) -> (extension in CloudKit):__C.CKRecordZone.Reference
0x197e12574  __TEXT,__text  dispatch thunk of (extension in CloudKit):__C.CKRecordZone.Reference.__allocating_init(zone: __C.CKRecordZone, action: (extension in CloudKit):__C.CKRecordZone.Reference.Action) -> (extension in CloudKit):__C.CKRecordZone.Reference
0x197f28740  __TEXT,__constg_swiftt  method descriptor for (extension in CloudKit):__C.CKRecordZone.Reference.__allocating_init(zone: __C.CKRecordZone, action: (extension in CloudKit):__C.CKRecordZone.Reference.Action) -> (extension in CloudKit):__C.CKRecordZone.Reference
0x197e11e04  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.Reference.init(zone: __C.CKRecordZone, action: (extension in CloudKit):__C.CKRecordZone.Reference.Action) -> (extension in CloudKit):__C.CKRecordZone.Reference
0x197ef3a44  __TEXT,__const  enum case for (extension in CloudKit):__C.CKRecordZone.Reference.Action.deleteSelf((extension in CloudKit):__C.CKRecordZone.Reference.Action.Type) -> (extension in CloudKit):__C.CKRecordZone.Reference.Action
0x197ef3a40  __TEXT,__const  enum case for (extension in CloudKit):__C.CKRecordZone.Reference.Action.none((extension in CloudKit):__C.CKRecordZone.Reference.Action.Type) -> (extension in CloudKit):__C.CKRecordZone.Reference.Action
0x197e11c30  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.Reference.Action.init(rawValue: Swift.Int) -> (extension in CloudKit):__C.CKRecordZone.Reference.Action?
0x197e11c3c  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.Reference.Action.rawValue.getter : Swift.Int
0x197ef3a18  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRecordZone.Reference.Action.rawValue : Swift.Int
0x197ef3a48  __TEXT,__const  enum case for (extension in CloudKit):__C.CKRecordZone.Reference.Action.validate((extension in CloudKit):__C.CKRecordZone.Reference.Action.Type) -> (extension in CloudKit):__C.CKRecordZone.Reference.Action
0x197e12654  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKRecordZone.Reference.Action
0x197f28748  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKRecordZone.Reference.Action
0x1e3ca5688  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKRecordZone.Reference.Action
0x197ef39a0  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKRecordZone.Reference.Action : Swift.Hashable in CloudKit
0x197ef3978  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKRecordZone.Reference.Action : Swift.Equatable in CloudKit
0x197ef39e0  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKRecordZone.Reference.Action : Swift.RawRepresentable in CloudKit
0x197e11c94  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.Reference.action.getter : (extension in CloudKit):__C.CKRecordZone.Reference.Action
0x1e0c41488  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKRecordZone.Reference.action : (extension in CloudKit):__C.CKRecordZone.Reference.Action
0x197e11d28  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.Reference.__allocating_init(zoneID: __C.CKRecordZoneID, action: (extension in CloudKit):__C.CKRecordZone.Reference.Action) -> (extension in CloudKit):__C.CKRecordZone.Reference
0x197e12560  __TEXT,__text  dispatch thunk of (extension in CloudKit):__C.CKRecordZone.Reference.__allocating_init(zoneID: __C.CKRecordZoneID, action: (extension in CloudKit):__C.CKRecordZone.Reference.Action) -> (extension in CloudKit):__C.CKRecordZone.Reference
0x197f28738  __TEXT,__constg_swiftt  method descriptor for (extension in CloudKit):__C.CKRecordZone.Reference.__allocating_init(zoneID: __C.CKRecordZoneID, action: (extension in CloudKit):__C.CKRecordZone.Reference.Action) -> (extension in CloudKit):__C.CKRecordZone.Reference
0x197e11d64  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.Reference.init(zoneID: __C.CKRecordZoneID, action: (extension in CloudKit):__C.CKRecordZone.Reference.Action) -> (extension in CloudKit):__C.CKRecordZone.Reference
0x197e11c84  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.Reference.zoneID.getter : __C.CKRecordZoneID
0x1e0c41480  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKRecordZone.Reference.zoneID : __C.CKRecordZoneID
0x197e120bc  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.Reference.isEqual(Any?) -> Swift.Bool
0x197e12524  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKRecordZone.Reference
0x197f28704  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKRecordZone.Reference
0x197ef3a28  __TEXT,__const  class metadata base offset for (extension in CloudKit):__C.CKRecordZone.Reference
0x197e12548  __TEXT,__text  method lookup function for (extension in CloudKit):__C.CKRecordZone.Reference
0x1ef67a778  __AUTH,__objc_data  type metadata for (extension in CloudKit):__C.CKRecordZone.Reference
0x197e12288  __TEXT,__text  (extension in CloudKit):__C.CKRecordZone.Reference.__deallocating_deinit
0x197e8e3f8  __TEXT,__text  (extension in CloudKit):__C.CKSyncEngine.description.getter : Swift.String
0x197e8f1dc  __TEXT,__text  (extension in CloudKit):__C.CKSyncEngine.init() -> __C.CKSyncEngine
0x197ecc1b8  __TEXT,__text  (extension in CloudKit):__C.CKSyncEngine.init() -> __C.CKSyncEngine
0x197e8f210  __TEXT,__text  type metadata accessor for __C.CKSyncEngine
0x197e48044  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReconnect.makeMessage(Foundation.Notification) -> (extension in CloudKit):__C.APSConnection.DidReconnect?
0x197e47f30  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReconnect.environmentName.modify : Swift.String
0x197e47ed8  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReconnect.environmentName.getter : Swift.String
0x197ef5eb8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReconnect.environmentName : Swift.String
0x197e47efc  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReconnect.environmentName.setter : Swift.String
0x197e47fc0  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReconnect.makeNotification((extension in CloudKit):__C.APSConnection.DidReconnect) -> Foundation.Notification
0x197e47fa8  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReconnect.namedDelegatePort.modify : Swift.String
0x197e47f50  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReconnect.namedDelegatePort.getter : Swift.String
0x197ef5ebc  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReconnect.namedDelegatePort : Swift.String
0x197e47f74  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReconnect.namedDelegatePort.setter : Swift.String
0x197e47ecc  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReconnect.name.getter : __C.NSNotificationName
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.APSConnection.DidReconnect.name : __C.NSNotificationName
0x197e485f0  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.APSConnection.DidReconnect
0x197f2922c  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.APSConnection.DidReconnect
0x1e3ca55a8  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.APSConnection.DidReconnect
0x197ef5e00  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.APSConnection.DidReconnect : (extension in Foundation):__C.NSNotificationCenter.AsyncMessage in CloudKit
0x197e46828  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.identifier.modify : Swift.String?
0x197e467c8  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.identifier.getter : Swift.String?
0x197ef5e70  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveToken.identifier : Swift.String?
0x197e467f4  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.identifier.setter : Swift.String?
0x197e46a5c  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReceiveToken.makeMessage(Foundation.Notification) -> (extension in CloudKit):__C.APSConnection.DidReceiveToken?
0x197e46648  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.environmentName.modify : Swift.String
0x197e465f0  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.environmentName.getter : Swift.String
0x197ef5e60  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveToken.environmentName : Swift.String
0x197e46614  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.environmentName.setter : Swift.String
0x197e46848  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReceiveToken.makeNotification((extension in CloudKit):__C.APSConnection.DidReceiveToken) -> Foundation.Notification
0x197e466c0  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.namedDelegatePort.modify : Swift.String
0x197e46668  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.namedDelegatePort.getter : Swift.String
0x197ef5e64  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveToken.namedDelegatePort : Swift.String
0x197e4668c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.namedDelegatePort.setter : Swift.String
0x197e465e4  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReceiveToken.name.getter : __C.NSNotificationName
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.APSConnection.DidReceiveToken.name : __C.NSNotificationName
0x197e46738  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.token.modify : Foundation.Data?
0x197e466d8  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.token.getter : Foundation.Data?
0x197ef5e68  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveToken.token : Foundation.Data?
0x197e46704  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.token.setter : Foundation.Data?
0x197e467b0  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.topic.modify : Swift.String?
0x197e46750  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.topic.getter : Swift.String?
0x197ef5e6c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveToken.topic : Swift.String?
0x197e4677c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveToken.topic.setter : Swift.String?
0x197e4843c  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.APSConnection.DidReceiveToken
0x197f29184  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveToken
0x1e3ca54d0  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.APSConnection.DidReceiveToken
0x197ef5c20  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveToken : (extension in Foundation):__C.NSNotificationCenter.AsyncMessage in CloudKit
0x197e4637c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.publicToken.modify : Foundation.Data?
0x197e4631c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.publicToken.getter : Foundation.Data?
0x197ef5e5c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.publicToken : Foundation.Data?
0x197e46348  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.publicToken.setter : Foundation.Data?
0x197e46488  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.makeMessage(Foundation.Notification) -> (extension in CloudKit):__C.APSConnection.DidReceivePublicToken?
0x197e4628c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.environmentName.modify : Swift.String
0x197e46234  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.environmentName.getter : Swift.String
0x197ef5e54  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.environmentName : Swift.String
0x197e46258  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.environmentName.setter : Swift.String
0x197e46394  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.makeNotification((extension in CloudKit):__C.APSConnection.DidReceivePublicToken) -> Foundation.Notification
0x197e46304  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.namedDelegatePort.modify : Swift.String
0x197e462ac  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.namedDelegatePort.getter : Swift.String
0x197ef5e58  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.namedDelegatePort : Swift.String
0x197e462d0  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.namedDelegatePort.setter : Swift.String
0x197e46228  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.name.getter : __C.NSNotificationName
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.APSConnection.DidReceivePublicToken.name : __C.NSNotificationName
0x197e48394  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.APSConnection.DidReceivePublicToken
0x197f29168  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.APSConnection.DidReceivePublicToken
0x1e3ca5400  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.APSConnection.DidReceivePublicToken
0x197ef5bd0  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.APSConnection.DidReceivePublicToken : (extension in Foundation):__C.NSNotificationCenter.AsyncMessage in CloudKit
0x197e47594  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.makeMessage(Foundation.Notification) -> (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage?
0x197e473e4  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.environmentName.modify : Swift.String
0x197e4738c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.environmentName.getter : Swift.String
0x197ef5e90  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.environmentName : Swift.String
0x197e473b0  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.environmentName.setter : Swift.String
0x197e474e0  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.makeNotification((extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage) -> Foundation.Notification
0x197e4745c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.namedDelegatePort.modify : Swift.String
0x197e47404  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.namedDelegatePort.getter : Swift.String
0x197ef5e94  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.namedDelegatePort : Swift.String
0x197e47428  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.namedDelegatePort.setter : Swift.String
0x197e47380  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.name.getter : __C.NSNotificationName
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.name : __C.NSNotificationName
0x197e474c8  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.message.modify : __C.APSOutgoingMessage?
0x197e47474  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.message.getter : __C.APSOutgoingMessage?
0x197ef5e98  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.message : __C.APSOutgoingMessage?
0x197e4749c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage.message.setter : __C.APSOutgoingMessage?
0x197e484ac  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage
0x197f291d8  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage
0x1e3ca5330  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage
0x197ef5d10  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage : (extension in Foundation):__C.NSNotificationCenter.AsyncMessage in CloudKit
0x197e47d78  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.makeMessage(Foundation.Notification) -> (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus?
0x197e47c18  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.environmentName.modify : Swift.String
0x197e47bc0  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.environmentName.getter : Swift.String
0x197ef5eac  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.environmentName : Swift.String
0x197e47be4  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.environmentName.setter : Swift.String
0x197e47cd0  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.makeNotification((extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus) -> Foundation.Notification
0x197e47c90  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.namedDelegatePort.modify : Swift.String
0x197e47c38  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.namedDelegatePort.getter : Swift.String
0x197ef5eb0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.namedDelegatePort : Swift.String
0x197e47c5c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.namedDelegatePort.setter : Swift.String
0x197e47bb4  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.name.getter : __C.NSNotificationName
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.name : __C.NSNotificationName
0x197e47cb8  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.connected.modify : Swift.Bool
0x197e47ca8  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.connected.getter : Swift.Bool
0x197ef5eb4  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.connected : Swift.Bool
0x197e47cb0  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus.connected.setter : Swift.Bool
0x197e485e0  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus
0x197f29210  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus
0x1e3ca5260  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus
0x197ef5db0  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus : (extension in Foundation):__C.NSNotificationCenter.AsyncMessage in CloudKit
0x197e46e38  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.makeMessage(Foundation.Notification) -> (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage?
0x197e46d14  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.environmentName.modify : Swift.String
0x197e48600  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.environmentName.getter : Swift.String
0x197ef5e74  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.environmentName : Swift.String
0x197e48610  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.environmentName.setter : Swift.String
0x197e46d64  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.makeNotification((extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage) -> Foundation.Notification
0x197e46d34  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.namedDelegatePort.modify : Swift.String
0x197e48620  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.namedDelegatePort.getter : Swift.String
0x197ef5e78  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.namedDelegatePort : Swift.String
0x197e48630  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.namedDelegatePort.setter : Swift.String
0x197e46d08  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.name.getter : __C.NSNotificationName
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.name : __C.NSNotificationName
0x197e46d4c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.message.modify : __C.APSIncomingMessage?
0x197e4860c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.message.getter : __C.APSIncomingMessage?
0x197ef5e7c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.message : __C.APSIncomingMessage?
0x197e48608  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage.message.setter : __C.APSIncomingMessage?
0x197e4844c  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage
0x197f291a0  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage
0x1e3ca5190  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage
0x197ef5c70  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage : (extension in Foundation):__C.NSNotificationCenter.AsyncMessage in CloudKit
0x197e471d0  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.makeMessage(Foundation.Notification) -> (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic?
0x197e46efc  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.environmentName.modify : Swift.String
0x197e46ea4  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.environmentName.getter : Swift.String
0x197ef5e80  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.environmentName : Swift.String
0x197e46ec8  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.environmentName.setter : Swift.String
0x197e47050  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.makeNotification((extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic) -> Foundation.Notification
0x197e46f74  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.namedDelegatePort.modify : Swift.String
0x197e46f1c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.namedDelegatePort.getter : Swift.String
0x197ef5e84  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.namedDelegatePort : Swift.String
0x197e46f40  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.namedDelegatePort.setter : Swift.String
0x197e46e98  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.name.getter : __C.NSNotificationName
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.name : __C.NSNotificationName
0x197e46fec  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.topic.modify : Swift.String?
0x197e46f8c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.topic.getter : Swift.String?
0x197ef5e88  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.topic : Swift.String?
0x197e46fb8  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.topic.setter : Swift.String?
0x197e47038  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.userInfo.modify : [Swift.AnyHashable : Any]?
0x197e47004  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.userInfo.getter : [Swift.AnyHashable : Any]?
0x197ef5e8c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.userInfo : [Swift.AnyHashable : Any]?
0x197e4700c  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic.userInfo.setter : [Swift.AnyHashable : Any]?
0x197e4845c  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic
0x197f291bc  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic
0x1e3ca50c0  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic
0x197ef5cc0  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic : (extension in Foundation):__C.NSNotificationCenter.AsyncMessage in CloudKit
0x197e479ec  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.makeMessage(Foundation.Notification) -> (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage?
0x197e47708  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.environmentName.modify : Swift.String
0x197e48604  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.environmentName.getter : Swift.String
0x197ef5e9c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.environmentName : Swift.String
0x197e48614  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.environmentName.setter : Swift.String
0x197e47824  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.makeNotification((extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage) -> Foundation.Notification
0x197e47728  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.namedDelegatePort.modify : Swift.String
0x197e48624  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.namedDelegatePort.getter : Swift.String
0x197ef5ea0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.namedDelegatePort : Swift.String
0x197e48634  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.namedDelegatePort.setter : Swift.String
0x197e476fc  __TEXT,__text  static (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.name.getter : __C.NSNotificationName
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.name : __C.NSNotificationName
0x197e47804  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.error.modify : Swift.Error?
0x197e477ac  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.error.getter : Swift.Error?
0x197ef5ea8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.error : Swift.Error?
0x197e477d8  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.error.setter : Swift.Error?
0x197e47794  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.message.modify : __C.APSOutgoingMessage?
0x197e47740  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.message.getter : __C.APSOutgoingMessage?
0x197ef5ea4  __TEXT,__const  property descriptor for (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.message : __C.APSOutgoingMessage?
0x197e47768  __TEXT,__text  (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage.message.setter : __C.APSOutgoingMessage?
0x197e4853c  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage
0x197f291f4  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage
0x1e3ca4ff0  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage
0x197ef5d60  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage : (extension in Foundation):__C.NSNotificationCenter.AsyncMessage in CloudKit
0x197e2c8a0  __TEXT,__text  (extension in CloudKit):__C.CKContainerID.init(CloudCoreInternal.ContainerID) -> __C.CKContainerID
0x197bb3548  __TEXT,__text  (extension in CloudKit):__C.CKPersonaType.description.getter : Swift.String
0x197efb20c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKPersonaType.description : Swift.String
0x197ec0ccc  __TEXT,__text  static (extension in CloudKit):__C.CKPersonaType.allCases.getter : [__C.CKPersonaType]
0x197efb20c  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKPersonaType.allCases : [__C.CKPersonaType]
0x197efb1a4  __TEXT,__const  protocol conformance descriptor for __C.CKPersonaType : Swift.CaseIterable in CloudKit
0x197efb1e0  __TEXT,__const  protocol conformance descriptor for __C.CKPersonaType : Swift.CustomStringConvertible in CloudKit
0x197e0e7fc  __TEXT,__text  (extension in CloudKit):__C.CKRecordValue.CKToSwiftNativeValue() -> CloudKit.CKRecordValueProtocol
0x197ea88ac  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.didCreateDatabaseTable() throws -> ()
0x197ea9610  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.validateTableMatchesTOCEntry() throws -> ()
0x197ea8c70  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.fetchProperties(_: [Swift.String]?, inObject: Swift.AnyObject, matchingDBProperties: [Swift.String]?, label: __C._CKSQLiteCompiledStatementLabel?) throws -> ()
0x197ea8dcc  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.fetchProperties(_: [Swift.String]?, inObject: Swift.AnyObject, label: __C._CKSQLiteCompiledStatementLabel?) throws -> ()
0x197ea9330  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.requestCallback(with: Foundation.Date, coalescingInterval: Swift.Double, minimumSeparation: Swift.Double) throws -> ()
0x197ea8f08  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.enumerateEntries((Any) throws -> Swift.Bool) throws -> ()
0x197ea8b10  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.updateProperties(_: [Swift.String], usingObject: Swift.AnyObject, label: __C._CKSQLiteCompiledStatementLabel?) throws -> ()
0x197ea88e8  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.wakeFromDatabase() throws -> ()
0x197ea8ecc  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.fetchAllProperties(Swift.AnyObject) throws -> ()
0x197ea8924  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.finishInitializing() throws -> ()
0x197ea9110  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.performTransaction(() throws -> ()) throws -> ()
0x197ea9688  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.validateReferences() throws -> ()
0x197ea9220  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.performInTransaction(() throws -> ()) throws -> ()
0x197ea8bfc  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.deletePrimaryKeyValue(Swift.Int) throws -> ()
0x197ea964c  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.prepareReferencedTables() throws -> ()
0x197ea96c4  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.enumerateTablesInDependencyOrder(using: (__C.CKSQLiteTable) throws -> ()) throws -> ()
0x197ea93b0  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.table(forReferenceProperty: Swift.String) throws -> (__C.CKSQLiteTableGroup, __C.CKSQLiteReferencedObjectTable)
0x197ea8bc0  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.delete(Swift.AnyObject) throws -> ()
0x197ea8a34  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.insert(_: Swift.AnyObject, orUpdateProperties: [Swift.String]?, label: __C._CKSQLiteCompiledStatementLabel?) throws -> ()
0x197ea8960  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.insert(Swift.AnyObject) throws -> ()
0x197ea8b84  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTable.update(using: Swift.AnyObject) throws -> ()
0x197e0a0ac  __TEXT,__text  (extension in CloudKit):__C.CKZoneFeature.description.getter : Swift.String
0x197e0a0d0  __TEXT,__text  static (extension in CloudKit):__C.CKZoneFeature.supportsSecureCoding.getter : Swift.Bool
0x197ef2a20  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKZoneFeature.supportsSecureCoding : Swift.Bool
0x197e0a010  __TEXT,__text  (extension in CloudKit):__C.CKZoneFeature.hash.getter : Swift.Int
0x197e09ef4  __TEXT,__text  (extension in CloudKit):__C.CKZoneFeature.init(name: Swift.String, value: Swift.String) -> __C.CKZoneFeature
0x197e09ef8  __TEXT,__text  (extension in CloudKit):__C.CKZoneFeature.init(name: Swift.String, value: Swift.String) -> __C.CKZoneFeature
0x197e09f34  __TEXT,__text  (extension in CloudKit):__C.CKZoneFeature.name.getter : Swift.String
0x197ef2a20  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKZoneFeature.name : Swift.String
0x197e0a13c  __TEXT,__text  (extension in CloudKit):__C.CKZoneFeature.init(coder: __C.NSCoder) -> __C.CKZoneFeature?
0x197e0a140  __TEXT,__text  (extension in CloudKit):__C.CKZoneFeature.init(coder: __C.NSCoder) -> __C.CKZoneFeature?
0x197e09f98  __TEXT,__text  (extension in CloudKit):__C.CKZoneFeature.value.getter : Swift.String
0x197ef2a20  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKZoneFeature.value : Swift.String
0x197e0a0d4  __TEXT,__text  (extension in CloudKit):__C.CKZoneFeature.encode(with: __C.NSCoder) -> ()
0x197e09fa4  __TEXT,__text  (extension in CloudKit):__C.CKZoneFeature.isEqual(Any?) -> Swift.Bool
0x197bbbdbc  __TEXT,__text  type metadata accessor for __C.CKZoneFeature
0x197e0ad14  __TEXT,__text  (extension in CloudKit):__C.CKFieldFeature.description.getter : Swift.String
0x197e0ad38  __TEXT,__text  static (extension in CloudKit):__C.CKFieldFeature.supportsSecureCoding.getter : Swift.Bool
0x197ef2a20  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKFieldFeature.supportsSecureCoding : Swift.Bool
0x197e0ac14  __TEXT,__text  (extension in CloudKit):__C.CKFieldFeature.hash.getter : Swift.Int
0x197e0bd38  __TEXT,__text  (extension in CloudKit):__C.CKFieldFeature.init(name: Swift.String, value: Swift.String) -> __C.CKFieldFeature
0x197e0a978  __TEXT,__text  (extension in CloudKit):__C.CKFieldFeature.init(name: Swift.String, value: Swift.String) -> __C.CKFieldFeature
0x197e0aabc  __TEXT,__text  (extension in CloudKit):__C.CKFieldFeature.name.getter : Swift.String
0x197ef2a20  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKFieldFeature.name : Swift.String
0x197e0bd40  __TEXT,__text  (extension in CloudKit):__C.CKFieldFeature.init(coder: __C.NSCoder) -> __C.CKFieldFeature?
0x197e0ada4  __TEXT,__text  (extension in CloudKit):__C.CKFieldFeature.init(coder: __C.NSCoder) -> __C.CKFieldFeature?
0x197e0ab20  __TEXT,__text  (extension in CloudKit):__C.CKFieldFeature.value.getter : Swift.String
0x197ef2a20  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKFieldFeature.value : Swift.String
0x197e0ad3c  __TEXT,__text  (extension in CloudKit):__C.CKFieldFeature.encode(with: __C.NSCoder) -> ()
0x197e0ab70  __TEXT,__text  (extension in CloudKit):__C.CKFieldFeature.isEqual(Any?) -> Swift.Bool
0x197bbc4ec  __TEXT,__text  type metadata accessor for __C.CKFieldFeature
0x197e0bd48  __TEXT,__text  (extension in CloudKit):__C.CKNotification.subscriptionID.getter : Swift.String?
0x197ef2a58  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKNotification.subscriptionID : Swift.String?
0x197e110f4  __TEXT,__text  static (extension in CloudKit):__C.CKRecordZoneID.defaultZoneName.getter : Swift.String
0x197e113a4  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneID.init(from: Swift.Decoder) throws -> __C.CKRecordZoneID
0x197e116ec  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneID.encode(to: Swift.Encoder) throws -> ()
0x197e110a8  __TEXT,__text  static (extension in CloudKit):__C.CKRecordZoneID.default.getter : __C.CKRecordZoneID
0x197c34440  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneID.init(zoneName: Swift.String, ownerName: Swift.String) -> __C.CKRecordZoneID
0x197ef3800  __TEXT,__const  protocol conformance descriptor for __C.CKRecordZoneID : Swift.Encodable in CloudKit
0x197ef37d8  __TEXT,__const  protocol conformance descriptor for __C.CKRecordZoneID : Swift.Decodable in CloudKit
0x197e1b5b8  __TEXT,__text  (extension in CloudKit):__C.CKSubscription.subscriptionID.getter : Swift.String
0x197ef4920  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKSubscription.subscriptionID : Swift.String
0x197e1f0d4  __TEXT,__text  (extension in CloudKit):__C.NSItemProvider.registerCKShare(container: __C.CKContainer, allowedSharingOptions: __C.CKAllowedSharingOptions, preparationHandler: @Sendable () async throws -> __C.CKShare) -> ()
0x197e1f908  __TEXT,__text  (extension in CloudKit):__C.NSItemProvider.registerCKShare(_: __C.CKShare, container: __C.CKContainer, allowedSharingOptions: __C.CKAllowedSharingOptions) -> ()
0x197ddd848  __TEXT,__text  (extension in CloudKit):__C.CKDatabaseScope.description.getter : Swift.String
0x197ef10f8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDatabaseScope.description : Swift.String
0x197ddd6ac  __TEXT,__text  static (extension in CloudKit):__C.CKDatabaseScope.organization.getter : __C.CKDatabaseScope
0x197ddd6dc  __TEXT,__text  static (extension in CloudKit):__C.CKDatabaseScope.unknown.getter : __C.CKDatabaseScope
0x197ef0e00  __TEXT,__const  protocol conformance descriptor for __C.CKDatabaseScope : Swift.Encodable in CloudKit
0x197ef0dd8  __TEXT,__const  protocol conformance descriptor for __C.CKDatabaseScope : Swift.Decodable in CloudKit
0x197ef0e28  __TEXT,__const  protocol conformance descriptor for __C.CKDatabaseScope : Swift.CustomStringConvertible in CloudKit
0x197ef3608  __TEXT,__const  protocol conformance descriptor for __C.CKEncryptedData : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca4de0  __AUTH_CONST,__const  protocol witness table for __C.CKEncryptedData : CloudKit.CKRecordValueProtocol in CloudKit
0x197e0a604  __TEXT,__text  (extension in CloudKit):__C.CKRecordFeature.description.getter : Swift.String
0x197e0a75c  __TEXT,__text  static (extension in CloudKit):__C.CKRecordFeature.supportsSecureCoding.getter : Swift.Bool
0x197ef2a20  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKRecordFeature.supportsSecureCoding : Swift.Bool
0x197e0a568  __TEXT,__text  (extension in CloudKit):__C.CKRecordFeature.hash.getter : Swift.Int
0x197e0bd34  __TEXT,__text  (extension in CloudKit):__C.CKRecordFeature.init(name: Swift.String, value: Swift.String) -> __C.CKRecordFeature
0x197e0a220  __TEXT,__text  (extension in CloudKit):__C.CKRecordFeature.init(name: Swift.String, value: Swift.String) -> __C.CKRecordFeature
0x197e0a2c8  __TEXT,__text  (extension in CloudKit):__C.CKRecordFeature.name.getter : Swift.String
0x197ef2a20  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRecordFeature.name : Swift.String
0x197e0bd3c  __TEXT,__text  (extension in CloudKit):__C.CKRecordFeature.init(coder: __C.NSCoder) -> __C.CKRecordFeature?
0x197e0a838  __TEXT,__text  (extension in CloudKit):__C.CKRecordFeature.init(coder: __C.NSCoder) -> __C.CKRecordFeature?
0x197e0a2ec  __TEXT,__text  (extension in CloudKit):__C.CKRecordFeature.value.getter : Swift.String
0x197ef2a20  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRecordFeature.value : Swift.String
0x197e0a760  __TEXT,__text  (extension in CloudKit):__C.CKRecordFeature.encode(with: __C.NSCoder) -> ()
0x197e0a2f8  __TEXT,__text  (extension in CloudKit):__C.CKRecordFeature.isEqual(Any?) -> Swift.Bool
0x197bbbda8  __TEXT,__text  type metadata accessor for __C.CKRecordFeature
0x197e07898  __TEXT,__text  (extension in CloudKit):__C.CKShareMetadata.requiredFeatures.getter : CloudKit.CKRequiredFeatureSet?
0x1e0c41418  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKShareMetadata.requiredFeatures : CloudKit.CKRequiredFeatureSet?
0x197dce2e4  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.fileSignature() -> Foundation.Data
0x197dce56c  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.description.getter : Swift.String
0x197dce154  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.encryptionType.getter : __C.CKMMCSEncryptionType
0x197ef0250  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAssetSignature.encryptionType : __C.CKMMCSEncryptionType
0x197dce6c8  __TEXT,__text  static (extension in CloudKit):__C.CKAssetSignature.supportsSecureCoding.getter : Swift.Bool
0x197ef0250  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKAssetSignature.supportsSecureCoding : Swift.Bool
0x197dce628  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.copy(with: ObjectiveC.NSZone?) -> Any
0x197dceb94  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.data.getter : Foundation.Data
0x197ef0250  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAssetSignature.data : Foundation.Data
0x197dce1e0  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.init(data: Foundation.Data) -> __C.CKAssetSignature
0x197dce250  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.init(data: Foundation.Data) -> __C.CKAssetSignature
0x197dce4c0  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.hash.getter : Swift.Int
0x197dce7cc  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.init(coder: __C.NSCoder) -> __C.CKAssetSignature?
0x197dce80c  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.init(coder: __C.NSCoder) -> __C.CKAssetSignature?
0x197dce6d0  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.encode(with: __C.NSCoder) -> ()
0x197dce37c  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.isEqual(Any?) -> Swift.Bool
0x197dce930  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.init() -> __C.CKAssetSignature
0x197ecbb88  __TEXT,__text  (extension in CloudKit):__C.CKAssetSignature.init() -> __C.CKAssetSignature
0x197dce964  __TEXT,__text  type metadata accessor for __C.CKAssetSignature
0x197e3500c  __TEXT,__text  (extension in CloudKit):__C.CKQueryOperation.desiredKeys.modify : [Swift.String]?
0x197e34f8c  __TEXT,__text  (extension in CloudKit):__C.CKQueryOperation.desiredKeys.getter : [Swift.String]?
0x1e0c41570  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKQueryOperation.desiredKeys : [Swift.String]?
0x197e34d40  __TEXT,__text  (extension in CloudKit):__C.CKQueryOperation.desiredKeys.setter : [Swift.String]?
0x197e35558  __TEXT,__text  (extension in CloudKit):__C.CKQueryOperation.queryResultBlock.modify : ((Swift.Result<__C.CKQueryCursor?, Swift.Error>) -> ())?
0x197e352bc  __TEXT,__text  (extension in CloudKit):__C.CKQueryOperation.queryResultBlock.getter : ((Swift.Result<__C.CKQueryCursor?, Swift.Error>) -> ())?
0x1e0c41590  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKQueryOperation.queryResultBlock : ((Swift.Result<__C.CKQueryCursor?, Swift.Error>) -> ())?
0x197e34e90  __TEXT,__text  (extension in CloudKit):__C.CKQueryOperation.queryResultBlock.setter : ((Swift.Result<__C.CKQueryCursor?, Swift.Error>) -> ())?
0x197e35234  __TEXT,__text  (extension in CloudKit):__C.CKQueryOperation.recordMatchedBlock.modify : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x197e350a0  __TEXT,__text  (extension in CloudKit):__C.CKQueryOperation.recordMatchedBlock.getter : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x1e0c41580  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKQueryOperation.recordMatchedBlock : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x197e34da0  __TEXT,__text  (extension in CloudKit):__C.CKQueryOperation.recordMatchedBlock.setter : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x197ea7fb4  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteDatabase.performDatabaseTransaction(() throws -> ()) throws -> ()
0x197ea83d4  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteDatabase.performDatabaseTransactionWithoutForeignKeyConstraints(() throws -> ()) throws -> ()
0x197ea81b0  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteDatabase.performInDatabaseTransaction(() throws -> ()) throws -> ()
0x197ea82cc  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteDatabase.executeSQL(Swift.String) throws -> ()
0x197ea838c  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteDatabase.resetValidation() throws -> ()
0x197ea832c  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteDatabase.dropTable(Swift.String) throws -> ()
0x197eaa018  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTOCTable.addEntry(for: __C.CKSQLiteTable) throws -> ()
0x197eaa054  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTOCTable.setSchema(_: Swift.String, for: __C.CKSQLiteTable) throws -> ()
0x197ef35a4  __TEXT,__const  protocol conformance descriptor for __C.CKStreamingAsset : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca4dd8  __AUTH_CONST,__const  protocol witness table for __C.CKStreamingAsset : CloudKit.CKRecordValueProtocol in CloudKit
0x197db3168  __TEXT,__text  (extension in CloudKit):__C.CKConcretePackage.updateItems(atIndexes: [Swift.UInt64], fileURLs: [Foundation.URL]) throws -> ()
0x197db3654  __TEXT,__text  (extension in CloudKit):__C.CKConcretePackage.setSignature(_: Foundation.Data?, verificationKey: Foundation.Data?) throws -> ()
0x197db2ef4  __TEXT,__text  (extension in CloudKit):__C.CKConcretePackage.enumerateItems(inSection: Swift.UInt64, block: (__C.CKPackageItem) -> Swift.Bool) throws -> ()
0x197db3120  __TEXT,__text  (extension in CloudKit):__C.CKConcretePackage.prepareForSectionPlanning() throws -> ()
0x197db2ea8  __TEXT,__text  (extension in CloudKit):__C.CKConcretePackage.add(__C.CKPackageSection) throws -> ()
0x197db35a0  __TEXT,__text  (extension in CloudKit):__C.CKConcretePackage.update(_: __C.CKPackageItem, withSignature: Foundation.Data, size: Swift.UInt64, paddedSize: Swift.UInt64, itemID: Swift.UInt64, sectionIndex: Swift.UInt64) throws -> ()
0x197e135c4  __TEXT,__text  static (extension in CloudKit):__C.CKReferenceAction.validate.getter : __C.CKReferenceAction
0x197e16514  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestamp.description.getter : Swift.String
0x197c28d74  __TEXT,__text  static (extension in CloudKit):__C.CKServerTimestamp.isSupported.getter : Swift.Bool
0x197ef3dd8  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKServerTimestamp.isSupported : Swift.Bool
0x197e1662c  __TEXT,__text  static (extension in CloudKit):__C.CKServerTimestamp.supportsSecureCoding.getter : Swift.Bool
0x197ef3dd8  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKServerTimestamp.supportsSecureCoding : Swift.Bool
0x197e165d8  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestamp.copy(with: ObjectiveC.NSZone?) -> Any
0x197e1645c  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestamp.hash.getter : Swift.Int
0x197e15d18  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestamp.time.getter : __C.CKServerTimestampTime
0x197ef3dd8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKServerTimestamp.time : __C.CKServerTimestampTime
0x197e16734  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestamp.init(coder: __C.NSCoder) -> __C.CKServerTimestamp?
0x197e16738  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestamp.init(coder: __C.NSCoder) -> __C.CKServerTimestamp?
0x197e15e38  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestamp.init(domain: __C.CKServerTimestampDomain, time: __C.CKServerTimestampTime) -> __C.CKServerTimestamp
0x197e15e90  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestamp.init(domain: __C.CKServerTimestampDomain, time: __C.CKServerTimestampTime) -> __C.CKServerTimestamp
0x197e15c4c  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestamp.domain.getter : __C.CKServerTimestampDomain
0x197ef3dd8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKServerTimestamp.domain : __C.CKServerTimestampDomain
0x197e16630  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestamp.encode(with: __C.NSCoder) -> ()
0x197e160e8  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestamp.isEqual(Any?) -> Swift.Bool
0x197e16964  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestamp.init() -> __C.CKServerTimestamp
0x197e16968  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestamp.init() -> __C.CKServerTimestamp
0x197e18130  __TEXT,__text  type metadata accessor for __C.CKServerTimestamp
0x197ec3f80  __TEXT,__text  (extension in CloudKit):__C.OS_dispatch_queue.ckCallOrDispatchSyncIfNotKey<A where A: Swift.Sendable>(_: Dispatch.DispatchSpecificKey<A>, block: () -> ()) -> ()
0x197df7e10  __TEXT,__text  (extension in CloudKit):__C.CKContainerOptions.supportedDeviceCapabilities.modify : CloudKit.CKDeviceCapabilitySet?
0x197df7acc  __TEXT,__text  (extension in CloudKit):__C.CKContainerOptions.supportedDeviceCapabilities.getter : CloudKit.CKDeviceCapabilitySet?
0x1e0c4133c  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKContainerOptions.supportedDeviceCapabilities : CloudKit.CKDeviceCapabilitySet?
0x197df7ccc  __TEXT,__text  (extension in CloudKit):__C.CKContainerOptions.supportedDeviceCapabilities.setter : CloudKit.CKDeviceCapabilitySet?
0x197dfb844  __TEXT,__text  static (extension in CloudKit):__C.CKDeviceCapability.isCapabilitySet(_: [__C.CKDeviceCapability], equalTo: [__C.CKDeviceCapability]) -> Swift.Bool
0x197dfba74  __TEXT,__text  static (extension in CloudKit):__C.CKDeviceCapability.isCapabilitySet(_: [__C.CKDeviceCapability], subsetOf: [__C.CKDeviceCapability]) -> Swift.Bool
0x197dfc6c0  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.description.getter : Swift.String
0x197dfbd24  __TEXT,__text  static (extension in CloudKit):__C.CKDeviceCapability.pruneAndSort([__C.CKDeviceCapability]) -> [__C.CKDeviceCapability]
0x197dfb470  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.sqliteRepresentation() -> Swift.String
0x197dfc014  __TEXT,__text  static (extension in CloudKit):__C.CKDeviceCapability.supportsSecureCoding.getter : Swift.Bool
0x197ef1fd0  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKDeviceCapability.supportsSecureCoding : Swift.Bool
0x197dfb6c0  __TEXT,__text  static (extension in CloudKit):__C.CKDeviceCapability.sqliteRepresentations([__C.CKDeviceCapability]) -> [Swift.String]
0x197c0e2e8  __TEXT,__text  static (extension in CloudKit):__C.CKDeviceCapability.fromSqliteRepresentation(Swift.String) -> __C.CKDeviceCapability?
0x197c0e1ac  __TEXT,__text  static (extension in CloudKit):__C.CKDeviceCapability.fromSqliteRepresentations([Swift.String]) -> [__C.CKDeviceCapability]
0x197dfc658  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.hash.getter : Swift.Int
0x197dfb04c  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.name.getter : Swift.String
0x197ef1fd0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDeviceCapability.name : Swift.String
0x197dfc074  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.init(coder: __C.NSCoder) -> __C.CKDeviceCapability?
0x197dfc078  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.init(coder: __C.NSCoder) -> __C.CKDeviceCapability?
0x197dfae30  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.init(level: __C.CKDeviceCapabilityLevel, name: Swift.String, value: Swift.String) -> __C.CKDeviceCapability
0x197dfaec8  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.init(level: __C.CKDeviceCapabilityLevel, name: Swift.String, value: Swift.String) -> __C.CKDeviceCapability
0x197dfb100  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.level.getter : __C.CKDeviceCapabilityLevel
0x197ef1fd0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDeviceCapability.level : __C.CKDeviceCapabilityLevel
0x197dfb0a0  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.value.getter : Swift.String
0x197ef1fd0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDeviceCapability.value : Swift.String
0x197c2b798  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.encode(with: __C.NSCoder) -> ()
0x197dfc39c  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.isEqual(Any?) -> Swift.Bool
0x197dfad10  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.wrapped.getter : CloudKit.CKDeviceCapability?
0x197ef1fd0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDeviceCapability.wrapped : CloudKit.CKDeviceCapability?
0x197c0fab4  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapability.init(CloudKit.CKDeviceCapability) -> __C.CKDeviceCapability
0x197c0fb2c  __TEXT,__text  type metadata accessor for __C.CKDeviceCapability
0x197e1ba20  __TEXT,__text  (extension in CloudKit):__C.CKNotificationInfo.desiredKeys.modify : [Swift.String]?
0x197e1b95c  __TEXT,__text  (extension in CloudKit):__C.CKNotificationInfo.desiredKeys.getter : [Swift.String]?
0x1e0c414e0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKNotificationInfo.desiredKeys : [Swift.String]?
0x197e1b9d4  __TEXT,__text  (extension in CloudKit):__C.CKNotificationInfo.desiredKeys.setter : [Swift.String]?
0x197e1b6cc  __TEXT,__text  (extension in CloudKit):__C.CKNotificationInfo.alertLocalizationArgs.modify : [Swift.String]?
0x197e1b608  __TEXT,__text  (extension in CloudKit):__C.CKNotificationInfo.alertLocalizationArgs.getter : [Swift.String]?
0x1e0c414b0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKNotificationInfo.alertLocalizationArgs : [Swift.String]?
0x197e1b680  __TEXT,__text  (extension in CloudKit):__C.CKNotificationInfo.alertLocalizationArgs.setter : [Swift.String]?
0x197e1b7e8  __TEXT,__text  (extension in CloudKit):__C.CKNotificationInfo.titleLocalizationArgs.modify : [Swift.String]?
0x197e1b724  __TEXT,__text  (extension in CloudKit):__C.CKNotificationInfo.titleLocalizationArgs.getter : [Swift.String]?
0x1e0c414c0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKNotificationInfo.titleLocalizationArgs : [Swift.String]?
0x197e1b79c  __TEXT,__text  (extension in CloudKit):__C.CKNotificationInfo.titleLocalizationArgs.setter : [Swift.String]?
0x197e1b904  __TEXT,__text  (extension in CloudKit):__C.CKNotificationInfo.subtitleLocalizationArgs.modify : [Swift.String]?
0x197e1b840  __TEXT,__text  (extension in CloudKit):__C.CKNotificationInfo.subtitleLocalizationArgs.getter : [Swift.String]?
0x1e0c414d0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKNotificationInfo.subtitleLocalizationArgs : [Swift.String]?
0x197e1b8b8  __TEXT,__text  (extension in CloudKit):__C.CKNotificationInfo.subtitleLocalizationArgs.setter : [Swift.String]?
0x197e1badc  __TEXT,__text  (extension in CloudKit):__C.CKNotificationInfo.init(alertBody: Swift.String?, alertLocalizationKey: Swift.String?, alertLocalizationArgs: [Swift.String], title: Swift.String?, titleLocalizationKey: Swift.String?, titleLocalizationArgs: [Swift.String], subtitle: Swift.String?, subtitleLocalizationKey
0x197e10688  __TEXT,__text  (extension in CloudKit):__C.CKRecordValueStore.makeIterator() -> CloudKit.CKRecordValueStoreIterator
0x197ef367c  __TEXT,__const  protocol conformance descriptor for __C.CKRecordValueStore : Swift.Sequence in CloudKit
0x197ea7ef0  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteCacheTable.extendExpiration(entry: __C.CKSQLiteCacheTableEntry) throws -> ()
0x197ea7f3c  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteCacheTable.setEntryExpiration(entry: __C.CKSQLiteCacheTableEntry, date: Foundation.Date) throws -> ()
0x197ea9a7c  __TEXT,__text  static (extension in CloudKit):__C.CKSQLiteTableGroup.purgeGroup(__C.CKSQLiteTableGroup) throws -> ()
0x197ea9b80  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTableGroup.updateGroupData([Swift.String : Any]) throws -> ()
0x197ea9b44  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTableGroup.migrateData(from: __C.CKSQLiteTableGroup) throws -> ()
0x197ea9ad0  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTableGroup.requestCallback(with: Foundation.Date, coalescingInterval: Swift.Double, minimumSeparation: Swift.Double) throws -> ()
0x197ea9efc  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTableGroup.requestCallback(forTarget: __C.CKSQLiteDatabaseManagerActivityTriggering, with: Foundation.Date, coalescingInterval: Swift.Double, minimumSeparation: Swift.Double) throws -> ()
0x197ea9f80  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTableGroup.setLastUsedEpoch(__C.CKSQLiteTOCLastUsedEpoch) throws -> ()
0x197ea9fbc  __TEXT,__text  static (extension in CloudKit):__C.CKSQLiteTableGroup.performValidation(in: __C.CKSQLiteDatabase) throws -> ()
0x197ea9a3c  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTableGroup.finishInitializing() throws -> ()
0x197ea9c0c  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTableGroup.performTransaction(() throws -> ()) throws -> ()
0x197ea9d28  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTableGroup.performInTransaction(() throws -> ()) throws -> ()
0x197ea9e44  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTableGroup.setFlag(__C.CKSQLiteTableGroupEntryFlag) throws -> ()
0x197ea9ebc  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTableGroup.validate(_: __C.CKSQLiteTable, matchesTOCEntry: __C.CKSQLiteTOCTableEntry) throws -> ()
0x197ea9e80  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTableGroup.clearFlag(__C.CKSQLiteTableGroupEntryFlag) throws -> ()
0x197e1925c  __TEXT,__text  (extension in CloudKit):__C.CKShareParticipant.participantID.getter : Swift.String
0x197ef4748  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKShareParticipant.participantID : Swift.String
0x197e0be70  __TEXT,__text  (extension in CloudKit):__C.CKQuerySubscription.init(recordType: Swift.String, predicate: __C.NSPredicate, subscriptionID: Swift.String, options: __C.CKQuerySubscriptionOptions) -> __C.CKQuerySubscription
0x197e0bf28  __TEXT,__text  (extension in CloudKit):__C.CKQuerySubscription.recordType.getter : Swift.String?
0x197ef2a60  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKQuerySubscription.recordType : Swift.String?
0x197c349f8  __TEXT,__text  (extension in CloudKit):__C.CKSyncEngineAccount.description.getter : Swift.String
0x197e93fc4  __TEXT,__text  static (extension in CloudKit):__C.CKSyncEngineAccount.supportsSecureCoding.getter : Swift.Bool
0x197ef7650  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKSyncEngineAccount.supportsSecureCoding : Swift.Bool
0x197e940f0  __TEXT,__text  (extension in CloudKit):__C.CKSyncEngineAccount.copy(with: ObjectiveC.NSZone?) -> Any
0x197e94040  __TEXT,__text  (extension in CloudKit):__C.CKSyncEngineAccount.hash.getter : Swift.Int
0x197e93fcc  __TEXT,__text  (extension in CloudKit):__C.CKSyncEngineAccount.init(coder: __C.NSCoder) -> __C.CKSyncEngineAccount?
0x197c3236c  __TEXT,__text  (extension in CloudKit):__C.CKSyncEngineAccount.init(coder: __C.NSCoder) -> __C.CKSyncEngineAccount?
0x197c358e8  __TEXT,__text  (extension in CloudKit):__C.CKSyncEngineAccount.isEqual(Any?) -> Swift.Bool
0x197c3583c  __TEXT,__text  type metadata accessor for __C.CKSyncEngineAccount
0x197e0b418  __TEXT,__text  (extension in CloudKit):__C.CKRequiredFeatureSet.description.getter : Swift.String
0x197e0af58  __TEXT,__text  (extension in CloudKit):__C.CKRequiredFeatureSet.init(zoneFeatures: [__C.CKZoneFeature], recordFeatures: [__C.CKRecordFeature], fieldFeatures: [__C.CKFieldFeature]) -> __C.CKRequiredFeatureSet
0x197bc80d0  __TEXT,__text  (extension in CloudKit):__C.CKRequiredFeatureSet.init(zoneFeatures: [__C.CKZoneFeature], recordFeatures: [__C.CKRecordFeature], fieldFeatures: [__C.CKFieldFeature]) -> __C.CKRequiredFeatureSet
0x197bbbdd0  __TEXT,__text  (extension in CloudKit):__C.CKRequiredFeatureSet.zoneFeatures.getter : __C.CKFeatureSet<__C.CKZoneFeature>
0x197ef2a20  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRequiredFeatureSet.zoneFeatures : __C.CKFeatureSet<__C.CKZoneFeature>
0x197bd3c50  __TEXT,__text  (extension in CloudKit):__C.CKRequiredFeatureSet.fieldFeatures.getter : __C.CKFeatureSet<__C.CKFieldFeature>
0x197ef2a20  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRequiredFeatureSet.fieldFeatures : __C.CKFeatureSet<__C.CKFieldFeature>
0x197bd38b0  __TEXT,__text  (extension in CloudKit):__C.CKRequiredFeatureSet.recordFeatures.getter : __C.CKFeatureSet<__C.CKRecordFeature>
0x197ef2a20  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRequiredFeatureSet.recordFeatures : __C.CKFeatureSet<__C.CKRecordFeature>
0x197e0b024  __TEXT,__text  static (extension in CloudKit):__C.CKRequiredFeatureSet.supportsSecureCoding.getter : Swift.Bool
0x197ef2a20  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKRequiredFeatureSet.supportsSecureCoding : Swift.Bool
0x197e0b068  __TEXT,__text  (extension in CloudKit):__C.CKRequiredFeatureSet.copy(with: ObjectiveC.NSZone?) -> Any
0x197e0b36c  __TEXT,__text  (extension in CloudKit):__C.CKRequiredFeatureSet.hash.getter : Swift.Int
0x197e0bd44  __TEXT,__text  (extension in CloudKit):__C.CKRequiredFeatureSet.init(coder: __C.NSCoder) -> __C.CKRequiredFeatureSet?
0x197bbc2b8  __TEXT,__text  (extension in CloudKit):__C.CKRequiredFeatureSet.init(coder: __C.NSCoder) -> __C.CKRequiredFeatureSet?
0x197bb8794  __TEXT,__text  (extension in CloudKit):__C.CKRequiredFeatureSet.encode(with: __C.NSCoder) -> ()
0x197e0b13c  __TEXT,__text  (extension in CloudKit):__C.CKRequiredFeatureSet.isEqual(Any?) -> Swift.Bool
0x197e0b4c0  __TEXT,__text  type metadata accessor for __C.CKRequiredFeatureSet
0x197ddb024  __TEXT,__text  static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.CKContainer.AccountChanged>>.accountChanged.getter : (extension in Foundation):__C.NSNo
0x197ef0998  __TEXT,__const  property descriptor for static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.CKContainer.AccountChanged>>.accountChanged : (extension in Fou
0x197ddb0c4  __TEXT,__text  static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.CKContainer.IdentityUpdated>>.identityUpdated.getter : (extension in Foundation):__C.NS
0x197ef0998  __TEXT,__const  property descriptor for static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.CKContainer.IdentityUpdated>>.identityUpdated : (extension in F
0x197e47348  __TEXT,__text  static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic>>.didReceiveMessageForTopic.getter : (extension
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidReceiveMessageForTopic>>.didReceiveMessageForT
0x197e476c4  __TEXT,__text  static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage>>.didSendOutgoingMessage.getter : (extension in Fo
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidSendOutgoingMessage>>.didSendOutgoingMessage :
0x197e46e60  __TEXT,__text  static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage>>.didReceiveIncomingMessage.getter : (extension
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidReceiveIncomingMessage>>.didReceiveIncomingMes
0x197e47b7c  __TEXT,__text  static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage>>.didFailToSendOutgoingMessage.getter : (ext
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidFailToSendOutgoingMessage>>.didFailToSendOutgo
0x197e480bc  __TEXT,__text  static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidReconnect>>.didReconnect.getter : (extension in Foundation):__C.NSNoti
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidReconnect>>.didReconnect : (extension in Found
0x197e46cd0  __TEXT,__text  static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidReceiveToken>>.didReceiveToken.getter : (extension in Foundation):__C.
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidReceiveToken>>.didReceiveToken : (extension in
0x197e465ac  __TEXT,__text  static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidReceivePublicToken>>.didReceivePublicToken.getter : (extension in Foun
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidReceivePublicToken>>.didReceivePublicToken : (
0x197e47e94  __TEXT,__text  static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus>>.didChangeConnectedStatus.getter : (extension i
0x197ef5e50  __TEXT,__const  property descriptor for static (extension in CloudKit):(extension in Foundation):__C.NSNotificationCenter.MessageIdentifier< where A == (extension in Foundation):__C.NSNotificationCenter.BaseMessageIdentifier<(extension in CloudKit):__C.APSConnection.DidChangeConnectedStatus>>.didChangeConnectedStat
0x197c25db4  __TEXT,__text  (extension in CloudKit):__C.CKAccountOverrideInfo.init(sessionConfiguration: CloudCoreInternal.AnySessionConfiguration) -> __C.CKAccountOverrideInfo?
0x197e1325c  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.description.getter : Swift.String
0x197e129d4  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.referenceAction.getter : __C.CKRecordZoneReferenceAction
0x197ef3a58  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRecordZoneReference.referenceAction : __C.CKRecordZoneReferenceAction
0x197e12a10  __TEXT,__text  static (extension in CloudKit):__C.CKRecordZoneReference.supportsSecureCoding.getter : Swift.Bool
0x197ef3a58  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKRecordZoneReference.supportsSecureCoding : Swift.Bool
0x197e12efc  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.copy(with: ObjectiveC.NSZone?) -> Any
0x197e1314c  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.hash.getter : Swift.Int
0x197e127dc  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.init(zone: __C.CKRecordZone, action: __C.CKRecordZoneReferenceAction) -> __C.CKRecordZoneReference
0x197e1282c  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.init(zone: __C.CKRecordZone, action: __C.CKRecordZoneReferenceAction) -> __C.CKRecordZoneReference
0x197e12b74  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.init(coder: __C.NSCoder) -> __C.CKRecordZoneReference?
0x197e12bb4  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.init(coder: __C.NSCoder) -> __C.CKRecordZoneReference?
0x197e12a18  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.encode(with: __C.NSCoder) -> ()
0x197e12740  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.init(zoneID: __C.CKRecordZoneID, action: __C.CKRecordZoneReferenceAction) -> __C.CKRecordZoneReference
0x197e12790  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.init(zoneID: __C.CKRecordZoneID, action: __C.CKRecordZoneReferenceAction) -> __C.CKRecordZoneReference
0x197e1297c  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.zoneID.getter : __C.CKRecordZoneID
0x197ef3a58  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRecordZoneReference.zoneID : __C.CKRecordZoneID
0x197e12fac  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.isEqual(Any?) -> Swift.Bool
0x197e12664  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.wrapped.getter : (extension in CloudKit):__C.CKRecordZone.Reference?
0x197ef3a58  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRecordZoneReference.wrapped : (extension in CloudKit):__C.CKRecordZone.Reference?
0x197e12690  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneReference.init((extension in CloudKit):__C.CKRecordZone.Reference) -> __C.CKRecordZoneReference
0x197e12e6c  __TEXT,__text  type metadata accessor for __C.CKRecordZoneReference
0x197eaa1ac  __TEXT,__text  static (extension in CloudKit):__C.CKSQLiteTOCTableGroup.createNewTOC(in: __C.CKSQLiteDatabase) throws -> ()
0x197eaa240  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTOCTableGroup.resetValidation() throws -> ()
0x197eaa280  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTOCTableGroup.prepareNewlyOpenedDatabase() throws -> ()
0x197eaa200  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTOCTableGroup.isUseable() throws -> ()
0x197e17af8  __TEXT,__text  static (extension in CloudKit):__C.CKServerTimestampTime.supportsSecureCoding.getter : Swift.Bool
0x197ef3dd8  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKServerTimestampTime.supportsSecureCoding : Swift.Bool
0x197e17aa4  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampTime.copy(with: ObjectiveC.NSZone?) -> Any
0x197e17770  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampTime.hash.getter : Swift.Int
0x197e18e40  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampTime.init(coder: __C.NSCoder) -> __C.CKServerTimestampTime?
0x197e17bf4  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampTime.init(coder: __C.NSCoder) -> __C.CKServerTimestampTime?
0x197e17afc  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampTime.encode(with: __C.NSCoder) -> ()
0x197e17924  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampTime.compare(__C.CKServerTimestampTime) -> __C.NSComparisonResult
0x197e177b0  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampTime.isEqual(Any?) -> Swift.Bool
0x197e17624  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampTime.init(version: __C.CKVersion) -> __C.CKServerTimestampTime
0x197e17660  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampTime.init(version: __C.CKVersion) -> __C.CKServerTimestampTime
0x197e18e58  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampTime.init() -> __C.CKServerTimestampTime
0x197e17d20  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampTime.init() -> __C.CKServerTimestampTime
0x197e1811c  __TEXT,__text  type metadata accessor for __C.CKServerTimestampTime
0x197df43e8  __TEXT,__text  (extension in CloudKit):__C.CKDatabaseSubscription.recordType.modify : Swift.String?
0x197df42f0  __TEXT,__text  (extension in CloudKit):__C.CKDatabaseSubscription.recordType.getter : Swift.String?
0x1e0c412d0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKDatabaseSubscription.recordType : Swift.String?
0x197df4390  __TEXT,__text  (extension in CloudKit):__C.CKDatabaseSubscription.recordType.setter : Swift.String?
0x197df4284  __TEXT,__text  (extension in CloudKit):__C.CKDatabaseSubscription.init(subscriptionID: Swift.String) -> __C.CKDatabaseSubscription
0x197e3d040  __TEXT,__text  (extension in CloudKit):__C.CKLeaveSharesOperation.leaveSharesResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3ce80  __TEXT,__text  (extension in CloudKit):__C.CKLeaveSharesOperation.leaveSharesResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c41750  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKLeaveSharesOperation.leaveSharesResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3cb68  __TEXT,__text  (extension in CloudKit):__C.CKLeaveSharesOperation.leaveSharesResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3cdf8  __TEXT,__text  (extension in CloudKit):__C.CKLeaveSharesOperation.perShareResultBlock.modify : ((__C.CKRecordID, Swift.Result<(), Swift.Error>) -> ())?
0x197e3cc64  __TEXT,__text  (extension in CloudKit):__C.CKLeaveSharesOperation.perShareResultBlock.getter : ((__C.CKRecordID, Swift.Result<(), Swift.Error>) -> ())?
0x1e0c41740  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKLeaveSharesOperation.perShareResultBlock : ((__C.CKRecordID, Swift.Result<(), Swift.Error>) -> ())?
0x197e3ca78  __TEXT,__text  (extension in CloudKit):__C.CKLeaveSharesOperation.perShareResultBlock.setter : ((__C.CKRecordID, Swift.Result<(), Swift.Error>) -> ())?
0x197ef35d4  __TEXT,__const  protocol conformance descriptor for __C.CKMergeableRecordValue : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca4bc8  __AUTH_CONST,__const  protocol witness table for __C.CKMergeableRecordValue : CloudKit.CKRecordValueProtocol in CloudKit
0x197e19238  __TEXT,__text  static (extension in CloudKit):__C.CKShareParticipantRole.administrator.getter : __C.CKShareParticipantRole
0x197ec02a4  __TEXT,__text  static (extension in CloudKit):__C.CKSpecialContainerType.allCasesAndNames.getter : [(__C.CKSpecialContainerType, Swift.String)]
0x197ec03e4  __TEXT,__text  static (extension in CloudKit):__C.CKSpecialContainerType.allCases.getter : [__C.CKSpecialContainerType]
0x197e3b640  __TEXT,__text  (extension in CloudKit):__C.CKAcceptSharesOperation.acceptSharesResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3b480  __TEXT,__text  (extension in CloudKit):__C.CKAcceptSharesOperation.acceptSharesResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c416e0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKAcceptSharesOperation.acceptSharesResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3b090  __TEXT,__text  (extension in CloudKit):__C.CKAcceptSharesOperation.acceptSharesResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3b3f8  __TEXT,__text  (extension in CloudKit):__C.CKAcceptSharesOperation.perShareResultBlock.modify : ((__C.CKShareMetadata, Swift.Result<__C.CKShare, Swift.Error>) -> ())?
0x197e3b18c  __TEXT,__text  (extension in CloudKit):__C.CKAcceptSharesOperation.perShareResultBlock.getter : ((__C.CKShareMetadata, Swift.Result<__C.CKShare, Swift.Error>) -> ())?
0x1e0c416d0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKAcceptSharesOperation.perShareResultBlock : ((__C.CKShareMetadata, Swift.Result<__C.CKShare, Swift.Error>) -> ())?
0x197e3afa0  __TEXT,__text  (extension in CloudKit):__C.CKAcceptSharesOperation.perShareResultBlock.setter : ((__C.CKShareMetadata, Swift.Result<__C.CKShare, Swift.Error>) -> ())?
0x197e36cc8  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.fetchRecordsResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3673c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.fetchRecordsResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c415e0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordsOperation.fetchRecordsResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e35850  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.fetchRecordsResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e35d44  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.desiredKeys.modify : [Swift.String]?
0x197e35cc4  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.desiredKeys.getter : [Swift.String]?
0x1e0c415a0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordsOperation.desiredKeys : [Swift.String]?
0x197e356fc  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.desiredKeys.setter : [Swift.String]?
0x197e366b8  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.perRecordResultBlock.modify : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x197e36360  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.perRecordResultBlock.getter : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x1e0c415d0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordsOperation.perRecordResultBlock : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x197e3575c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.perRecordResultBlock.setter : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x197e3615c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.recordFetchConfigurations.modify : [__C.CKRecordID : (extension in CloudKit):__C.CKRecord.FetchConfiguration]?
0x197e35f68  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.recordFetchConfigurations.getter : [__C.CKRecordID : (extension in CloudKit):__C.CKRecord.FetchConfiguration]?
0x1e0c415c0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordsOperation.recordFetchConfigurations : [__C.CKRecordID : (extension in CloudKit):__C.CKRecord.FetchConfiguration]?
0x197e3593c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.recordFetchConfigurations.setter : [__C.CKRecordID : (extension in CloudKit):__C.CKRecord.FetchConfiguration]?
0x197e35ec0  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.defaultRecordFetchConfiguration.modify : (extension in CloudKit):__C.CKRecord.FetchConfiguration?
0x197e35da0  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.defaultRecordFetchConfiguration.getter : (extension in CloudKit):__C.CKRecord.FetchConfiguration?
0x1e0c415b0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordsOperation.defaultRecordFetchConfiguration : (extension in CloudKit):__C.CKRecord.FetchConfiguration?
0x197e35e34  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordsOperation.defaultRecordFetchConfiguration.setter : (extension in CloudKit):__C.CKRecord.FetchConfiguration?
0x197e0ed98  __TEXT,__text  (extension in CloudKit):__C.CKRecordKeyValueSetting.subscript.modify : (Swift.String) -> CloudKit.CKRecordValueProtocol?
0x197e0ec84  __TEXT,__text  (extension in CloudKit):__C.CKRecordKeyValueSetting.subscript.getter : (Swift.String) -> CloudKit.CKRecordValueProtocol?
0x1e0c41464  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKRecordKeyValueSetting.subscript(Swift.String) -> CloudKit.CKRecordValueProtocol?
0x197c0599c  __TEXT,__text  (extension in CloudKit):__C.CKRecordKeyValueSetting.subscript.setter : (Swift.String) -> CloudKit.CKRecordValueProtocol?
0x197e0eaa0  __TEXT,__text  (extension in CloudKit):__C.CKRecordKeyValueSetting.subscript.modify : <A where A1: CloudKit.CKRecordValueProtocol>(Swift.String) -> A1?
0x197c05358  __TEXT,__text  (extension in CloudKit):__C.CKRecordKeyValueSetting.subscript.getter : <A where A1: CloudKit.CKRecordValueProtocol>(Swift.String) -> A1?
0x1e0c41448  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKRecordKeyValueSetting.subscript<A where A1: CloudKit.CKRecordValueProtocol>(Swift.String) -> A1?
0x197e0e9d0  __TEXT,__text  (extension in CloudKit):__C.CKRecordKeyValueSetting.subscript.setter : <A where A1: CloudKit.CKRecordValueProtocol>(Swift.String) -> A1?
0x197ea8510  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteDatabaseManager.registerDatabase(__C.CKSQLiteDatabase) throws -> ()
0x197ea855c  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteDatabaseManager.addActivityTrigger(withTarget: __C.CKSQLiteDatabaseManagerActivityTriggering, date: Foundation.Date, coalescingInterval: Swift.Double, minimumSeparation: Swift.Double) throws -> ()
0x197ea99bc  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTableGroupEntry.setFlag(_: __C.CKSQLiteTableGroupEntryFlag, database: __C.CKSQLiteDatabase) throws -> ()
0x197ea99fc  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTableGroupEntry.clearFlag(_: __C.CKSQLiteTableGroupEntryFlag, database: __C.CKSQLiteDatabase) throws -> ()
0x197de5d3c  __TEXT,__text  (extension in CloudKit):__C.CKDatabaseImplementation.withCheckedThrowingOperationContinuation<A>(database: __C.CKDatabase, convenienceConfiguration: __C.CKConvenienceConfiguration?, _: (Swift.CheckedContinuation<A, Swift.Error>) -> __C.CKDatabaseOperation) async throws -> A
0x197ef0db0  __TEXT,__const  async function pointer to (extension in CloudKit):__C.CKDatabaseImplementation.withCheckedThrowingOperationContinuation<A>(database: __C.CKDatabase, convenienceConfiguration: __C.CKConvenienceConfiguration?, _: (Swift.CheckedContinuation<A, Swift.Error>) -> __C.CKDatabaseOperation) async throws -> A
0x197e3bdc0  __TEXT,__text  (extension in CloudKit):__C.CKDeclineSharesOperation.declineSharesResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3bc00  __TEXT,__text  (extension in CloudKit):__C.CKDeclineSharesOperation.declineSharesResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c41700  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKDeclineSharesOperation.declineSharesResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3b850  __TEXT,__text  (extension in CloudKit):__C.CKDeclineSharesOperation.declineSharesResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3bb78  __TEXT,__text  (extension in CloudKit):__C.CKDeclineSharesOperation.perShareResultBlock.modify : ((__C.CKShareMetadata, Swift.Result<(), Swift.Error>) -> ())?
0x197e3b94c  __TEXT,__text  (extension in CloudKit):__C.CKDeclineSharesOperation.perShareResultBlock.getter : ((__C.CKShareMetadata, Swift.Result<(), Swift.Error>) -> ())?
0x1e0c416f0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKDeclineSharesOperation.perShareResultBlock : ((__C.CKShareMetadata, Swift.Result<(), Swift.Error>) -> ())?
0x197e3b760  __TEXT,__text  (extension in CloudKit):__C.CKDeclineSharesOperation.perShareResultBlock.setter : ((__C.CKShareMetadata, Swift.Result<(), Swift.Error>) -> ())?
0x197e39c98  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordsOperation.undeprecated_modifyRecordsCompletionBlock.modify : (([__C.CKRecord]?, [__C.CKRecordID]?, Swift.Error?) -> ())?
0x197e398c0  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordsOperation.undeprecated_modifyRecordsCompletionBlock.getter : (([__C.CKRecord]?, [__C.CKRecordID]?, Swift.Error?) -> ())?
0x1e0c416a0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifyRecordsOperation.undeprecated_modifyRecordsCompletionBlock : (([__C.CKRecord]?, [__C.CKRecordID]?, Swift.Error?) -> ())?
0x197e39a6c  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordsOperation.undeprecated_modifyRecordsCompletionBlock.setter : (([__C.CKRecord]?, [__C.CKRecordID]?, Swift.Error?) -> ())?
0x197e3a150  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordsOperation.modifyRecordsResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e39d18  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordsOperation.modifyRecordsResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c416b0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifyRecordsOperation.modifyRecordsResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e392dc  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordsOperation.modifyRecordsResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197c273dc  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordsOperation.init(recordsToSave: [__C.CKRecord]?, recordIDsToDelete: [__C.CKRecordID]?) -> __C.CKModifyRecordsOperation
0x197e39630  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordsOperation.perRecordSaveBlock.modify : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x197e394a0  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordsOperation.perRecordSaveBlock.getter : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x1e0c41680  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifyRecordsOperation.perRecordSaveBlock : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x197e39134  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordsOperation.perRecordSaveBlock.setter : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x197e39840  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordsOperation.perRecordDeleteBlock.modify : ((__C.CKRecordID, Swift.Result<(), Swift.Error>) -> ())?
0x197e396b0  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordsOperation.perRecordDeleteBlock.getter : ((__C.CKRecordID, Swift.Result<(), Swift.Error>) -> ())?
0x1e0c41690  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifyRecordsOperation.perRecordDeleteBlock : ((__C.CKRecordID, Swift.Result<(), Swift.Error>) -> ())?
0x197e39208  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordsOperation.perRecordDeleteBlock.setter : ((__C.CKRecordID, Swift.Result<(), Swift.Error>) -> ())?
0x197e134f4  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneSubscription.recordType.modify : Swift.String?
0x197e133fc  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneSubscription.recordType.getter : Swift.String?
0x1e0c414a0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKRecordZoneSubscription.recordType : Swift.String?
0x197e1349c  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneSubscription.recordType.setter : Swift.String?
0x197e13384  __TEXT,__text  (extension in CloudKit):__C.CKRecordZoneSubscription.init(zoneID: __C.CKRecordZoneID, subscriptionID: Swift.String) -> __C.CKRecordZoneSubscription
0x197e431b0  __TEXT,__text  (extension in CloudKit):__C.CKFetchUserQuotaOperation.fetchUserQuotaResultBlock.modify : ((Swift.Result<Swift.UInt64, Swift.Error>) -> ())?
0x197e42f6c  __TEXT,__text  (extension in CloudKit):__C.CKFetchUserQuotaOperation.fetchUserQuotaResultBlock.getter : ((Swift.Result<Swift.UInt64, Swift.Error>) -> ())?
0x1e0c418c0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchUserQuotaOperation.fetchUserQuotaResultBlock : ((Swift.Result<Swift.UInt64, Swift.Error>) -> ())?
0x197e42e54  __TEXT,__text  (extension in CloudKit):__C.CKFetchUserQuotaOperation.fetchUserQuotaResultBlock.setter : ((Swift.Result<Swift.UInt64, Swift.Error>) -> ())?
0x197e1c1a4  __TEXT,__text  (extension in CloudKit):__C.CKSystemSharingUIObserver.systemSharingUIDidSaveShareBlock.modify : ((__C.CKRecordID, Swift.Result<__C.CKShare, Swift.Error>) -> ())?
0x197e1bde0  __TEXT,__text  (extension in CloudKit):__C.CKSystemSharingUIObserver.systemSharingUIDidSaveShareBlock.getter : ((__C.CKRecordID, Swift.Result<__C.CKShare, Swift.Error>) -> ())?
0x1e0c414f0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKSystemSharingUIObserver.systemSharingUIDidSaveShareBlock : ((__C.CKRecordID, Swift.Result<__C.CKShare, Swift.Error>) -> ())?
0x197bd9f0c  __TEXT,__text  (extension in CloudKit):__C.CKSystemSharingUIObserver.systemSharingUIDidSaveShareBlock.setter : ((__C.CKRecordID, Swift.Result<__C.CKShare, Swift.Error>) -> ())?
0x197e1c510  __TEXT,__text  (extension in CloudKit):__C.CKSystemSharingUIObserver.systemSharingUIDidStopSharingBlock.modify : ((__C.CKRecordID, Swift.Result<(), Swift.Error>) -> ())?
0x197e1c22c  __TEXT,__text  (extension in CloudKit):__C.CKSystemSharingUIObserver.systemSharingUIDidStopSharingBlock.getter : ((__C.CKRecordID, Swift.Result<(), Swift.Error>) -> ())?
0x1e0c41500  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKSystemSharingUIObserver.systemSharingUIDidStopSharingBlock : ((__C.CKRecordID, Swift.Result<(), Swift.Error>) -> ())?
0x197bd9e0c  __TEXT,__text  (extension in CloudKit):__C.CKSystemSharingUIObserver.systemSharingUIDidStopSharingBlock.setter : ((__C.CKRecordID, Swift.Result<(), Swift.Error>) -> ())?
0x197e3aa78  __TEXT,__text  (extension in CloudKit):__C.CKRecordFetchConfiguration.description.getter : Swift.String
0x197c3b40c  __TEXT,__text  (extension in CloudKit):__C.CKRecordFetchConfiguration.desiredKeys.getter : [Swift.String]?
0x1e0c416c0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKRecordFetchConfiguration.desiredKeys : [Swift.String]?
0x197e3a70c  __TEXT,__text  (extension in CloudKit):__C.CKRecordFetchConfiguration.desiredKeys.setter : [Swift.String]?
0x197e3abe4  __TEXT,__text  static (extension in CloudKit):__C.CKRecordFetchConfiguration.supportsSecureCoding.getter : Swift.Bool
0x197ef5ae4  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKRecordFetchConfiguration.supportsSecureCoding : Swift.Bool
0x197e3ab28  __TEXT,__text  (extension in CloudKit):__C.CKRecordFetchConfiguration.copy(with: ObjectiveC.NSZone?) -> Any
0x197e3a9a0  __TEXT,__text  (extension in CloudKit):__C.CKRecordFetchConfiguration.hash.getter : Swift.Int
0x197e3acac  __TEXT,__text  (extension in CloudKit):__C.CKRecordFetchConfiguration.init(coder: __C.NSCoder) -> __C.CKRecordFetchConfiguration?
0x197e3acec  __TEXT,__text  (extension in CloudKit):__C.CKRecordFetchConfiguration.init(coder: __C.NSCoder) -> __C.CKRecordFetchConfiguration?
0x197e3abec  __TEXT,__text  (extension in CloudKit):__C.CKRecordFetchConfiguration.encode(with: __C.NSCoder) -> ()
0x197e3a820  __TEXT,__text  (extension in CloudKit):__C.CKRecordFetchConfiguration.isEqual(Any?) -> Swift.Bool
0x197e3a338  __TEXT,__text  (extension in CloudKit):__C.CKRecordFetchConfiguration.wrapped.getter : (extension in CloudKit):__C.CKRecord.FetchConfiguration
0x197ef5ae4  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRecordFetchConfiguration.wrapped : (extension in CloudKit):__C.CKRecord.FetchConfiguration
0x197e3ae54  __TEXT,__text  (extension in CloudKit):__C.CKRecordFetchConfiguration.init() -> __C.CKRecordFetchConfiguration
0x197c2815c  __TEXT,__text  (extension in CloudKit):__C.CKRecordFetchConfiguration.init() -> __C.CKRecordFetchConfiguration
0x197e3ae78  __TEXT,__text  type metadata accessor for __C.CKRecordFetchConfiguration
0x197eaa0bc  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTOCTableGroupTable.makeUniqueGroupName(__C.CKSQLiteTableGroupEntry) throws -> ()
0x197eaa170  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTOCTableGroupTable.updateGroupData(__C.CKSQLiteTableGroupEntry) throws -> ()
0x197eaa0f8  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTOCTableGroupTable.invalidate(__C.CKSQLiteTableGroupEntry) throws -> ()
0x197eaa134  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteTOCTableGroupTable.updateLastUsedDate(__C.CKSQLiteTableGroupEntry) throws -> ()
0x197e411b4  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZonesOperation.undeprecated_fetchRecordZonesCompletionBlock.modify : (([__C.CKRecordZoneID : __C.CKRecordZone]?, Swift.Error?) -> ())?
0x197e40ed4  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZonesOperation.undeprecated_fetchRecordZonesCompletionBlock.getter : (([__C.CKRecordZoneID : __C.CKRecordZone]?, Swift.Error?) -> ())?
0x1e0c41850  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordZonesOperation.undeprecated_fetchRecordZonesCompletionBlock : (([__C.CKRecordZoneID : __C.CKRecordZone]?, Swift.Error?) -> ())?
0x197e4103c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZonesOperation.undeprecated_fetchRecordZonesCompletionBlock.setter : (([__C.CKRecordZoneID : __C.CKRecordZone]?, Swift.Error?) -> ())?
0x197e40e4c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZonesOperation.perRecordZoneResultBlock.modify : ((__C.CKRecordZoneID, Swift.Result<__C.CKRecordZone, Swift.Error>) -> ())?
0x197e40cbc  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZonesOperation.perRecordZoneResultBlock.getter : ((__C.CKRecordZoneID, Swift.Result<__C.CKRecordZone, Swift.Error>) -> ())?
0x1e0c41840  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordZonesOperation.perRecordZoneResultBlock : ((__C.CKRecordZoneID, Swift.Result<__C.CKRecordZone, Swift.Error>) -> ())?
0x197bc8fb4  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZonesOperation.perRecordZoneResultBlock.setter : ((__C.CKRecordZoneID, Swift.Result<__C.CKRecordZone, Swift.Error>) -> ())?
0x197e4164c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZonesOperation.fetchRecordZonesResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e4123c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZonesOperation.fetchRecordZonesResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c41860  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordZonesOperation.fetchRecordZonesResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197bc90a8  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZonesOperation.fetchRecordZonesResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e17264  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampUserDomain.init(userRecordID: __C.CKRecordID) -> __C.CKServerTimestampUserDomain
0x197e172a0  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampUserDomain.init(userRecordID: __C.CKRecordID) -> __C.CKServerTimestampUserDomain
0x197e17228  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampUserDomain.userRecordID.getter : __C.CKRecordID
0x197ef3dd8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKServerTimestampUserDomain.userRecordID : __C.CKRecordID
0x1eba833a0  __DATA,__data  direct field offset for (extension in CloudKit):__C.CKServerTimestampUserDomain.userRecordID : __C.CKRecordID
0x197e174a4  __TEXT,__text  static (extension in CloudKit):__C.CKServerTimestampUserDomain.supportsSecureCoding.getter : Swift.Bool
0x197ef3dd8  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKServerTimestampUserDomain.supportsSecureCoding : Swift.Bool
0x197e17450  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampUserDomain.copy(with: ObjectiveC.NSZone?) -> Any
0x197e17350  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampUserDomain.hash.getter : Swift.Int
0x197e17258  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampUserDomain.type.getter : __C.CKServerTimestampDomainType
0x197ef3dd8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKServerTimestampUserDomain.type : __C.CKServerTimestampDomainType
0x1eba833a8  __DATA,__data  direct field offset for (extension in CloudKit):__C.CKServerTimestampUserDomain.type : __C.CKServerTimestampDomainType
0x197e18e3c  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampUserDomain.init(coder: __C.NSCoder) -> __C.CKServerTimestampUserDomain?
0x197e1756c  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampUserDomain.init(coder: __C.NSCoder) -> __C.CKServerTimestampUserDomain?
0x197e174a8  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampUserDomain.encode(with: __C.NSCoder) -> ()
0x197e17390  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampUserDomain.isEqual(Any?) -> Swift.Bool
0x197e18e54  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampUserDomain.init() -> __C.CKServerTimestampUserDomain
0x197ecbc18  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampUserDomain.init() -> __C.CKServerTimestampUserDomain
0x197e18204  __TEXT,__text  type metadata accessor for __C.CKServerTimestampUserDomain
0x197e436f0  __TEXT,__text  (extension in CloudKit):__C.CKFetchWebAuthTokenOperation.fetchWebAuthTokenResultBlock.modify : ((Swift.Result<Swift.String, Swift.Error>) -> ())?
0x197e43258  __TEXT,__text  (extension in CloudKit):__C.CKFetchWebAuthTokenOperation.fetchWebAuthTokenResultBlock.getter : ((Swift.Result<Swift.String, Swift.Error>) -> ())?
0x1e0c418d0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchWebAuthTokenOperation.fetchWebAuthTokenResultBlock : ((Swift.Result<Swift.String, Swift.Error>) -> ())?
0x197e433f0  __TEXT,__text  (extension in CloudKit):__C.CKFetchWebAuthTokenOperation.fetchWebAuthTokenResultBlock.setter : ((Swift.Result<Swift.String, Swift.Error>) -> ())?
0x197e421ac  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordZonesOperation.undeprecated_modifyRecordZonesCompletionBlock.modify : (([__C.CKRecordZone]?, [__C.CKRecordZoneID]?, Swift.Error?) -> ())?
0x197e41e18  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordZonesOperation.undeprecated_modifyRecordZonesCompletionBlock.getter : (([__C.CKRecordZone]?, [__C.CKRecordZoneID]?, Swift.Error?) -> ())?
0x1e0c41890  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifyRecordZonesOperation.undeprecated_modifyRecordZonesCompletionBlock : (([__C.CKRecordZone]?, [__C.CKRecordZoneID]?, Swift.Error?) -> ())?
0x197e41f80  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordZonesOperation.undeprecated_modifyRecordZonesCompletionBlock.setter : (([__C.CKRecordZone]?, [__C.CKRecordZoneID]?, Swift.Error?) -> ())?
0x197e41b88  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordZonesOperation.perRecordZoneSaveBlock.modify : ((__C.CKRecordZoneID, Swift.Result<__C.CKRecordZone, Swift.Error>) -> ())?
0x197e419f8  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordZonesOperation.perRecordZoneSaveBlock.getter : ((__C.CKRecordZoneID, Swift.Result<__C.CKRecordZone, Swift.Error>) -> ())?
0x1e0c41870  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifyRecordZonesOperation.perRecordZoneSaveBlock : ((__C.CKRecordZoneID, Swift.Result<__C.CKRecordZone, Swift.Error>) -> ())?
0x197e41780  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordZonesOperation.perRecordZoneSaveBlock.setter : ((__C.CKRecordZoneID, Swift.Result<__C.CKRecordZone, Swift.Error>) -> ())?
0x197e41d98  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordZonesOperation.perRecordZoneDeleteBlock.modify : ((__C.CKRecordZoneID, Swift.Result<(), Swift.Error>) -> ())?
0x197e41c08  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordZonesOperation.perRecordZoneDeleteBlock.getter : ((__C.CKRecordZoneID, Swift.Result<(), Swift.Error>) -> ())?
0x1e0c41880  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifyRecordZonesOperation.perRecordZoneDeleteBlock : ((__C.CKRecordZoneID, Swift.Result<(), Swift.Error>) -> ())?
0x197e41854  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordZonesOperation.perRecordZoneDeleteBlock.setter : ((__C.CKRecordZoneID, Swift.Result<(), Swift.Error>) -> ())?
0x197e425e0  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordZonesOperation.modifyRecordZonesResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e4222c  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordZonesOperation.modifyRecordZonesResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c418a0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifyRecordZonesOperation.modifyRecordZonesResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e41928  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordZonesOperation.modifyRecordZonesResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197bd31b4  __TEXT,__text  (extension in CloudKit):__C.CKModifyRecordZonesOperation.init(recordZonesToSave: [__C.CKRecordZone]?, recordZoneIDsToDelete: [__C.CKRecordZoneID]?) -> __C.CKModifyRecordZonesOperation
0x197e19204  __TEXT,__text  static (extension in CloudKit):__C.CKShareParticipantPermission.custom.getter : __C.CKShareParticipantPermission
0x197e4aeac  __TEXT,__text  (extension in CloudKit):__C.CKSymptomDiagnosticsReporter.init() -> __C.CKSymptomDiagnosticsReporter
0x197ecc188  __TEXT,__text  (extension in CloudKit):__C.CKSymptomDiagnosticsReporter.init() -> __C.CKSymptomDiagnosticsReporter
0x197e4b210  __TEXT,__text  type metadata accessor for __C.CKSymptomDiagnosticsReporter
0x197dfda9c  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.description.getter : Swift.String
0x197dfd5ec  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.init(isSupported: Swift.Bool) -> __C.CKDeviceCapabilityCheckResult
0x197dfd620  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.init(isSupported: Swift.Bool) -> __C.CKDeviceCapabilityCheckResult
0x197dfd6a0  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.isSupported.getter : Swift.Bool
0x197ef1fd0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.isSupported : Swift.Bool
0x197dfd6d4  __TEXT,__text  static (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.supportsSecureCoding.getter : Swift.Bool
0x197ef1fd0  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.supportsSecureCoding : Swift.Bool
0x197dfd9c4  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.hash.getter : Swift.Int
0x197dfdd94  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.init(coder: __C.NSCoder) -> __C.CKDeviceCapabilityCheckResult?
0x197dfd7fc  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.init(coder: __C.NSCoder) -> __C.CKDeviceCapabilityCheckResult?
0x197dfd6d8  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.encode(with: __C.NSCoder) -> ()
0x197dfd8c8  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.isEqual(Any?) -> Swift.Bool
0x197dfada0  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.wrapped.getter : CloudKit.CKDeviceCapabilityCheckResult?
0x197ef1fd0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.wrapped : CloudKit.CKDeviceCapabilityCheckResult?
0x197dfadf8  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckResult.init(CloudKit.CKDeviceCapabilityCheckResult) -> __C.CKDeviceCapabilityCheckResult
0x197dfdc00  __TEXT,__text  type metadata accessor for __C.CKDeviceCapabilityCheckResult
0x197e3c68c  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareMetadataOperation.perShareMetadataResultBlock.modify : ((Foundation.URL, Swift.Result<__C.CKShareMetadata, Swift.Error>) -> ())?
0x197e3c240  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareMetadataOperation.perShareMetadataResultBlock.getter : ((Foundation.URL, Swift.Result<__C.CKShareMetadata, Swift.Error>) -> ())?
0x1e0c41720  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchShareMetadataOperation.perShareMetadataResultBlock : ((Foundation.URL, Swift.Result<__C.CKShareMetadata, Swift.Error>) -> ())?
0x197e3bee0  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareMetadataOperation.perShareMetadataResultBlock.setter : ((Foundation.URL, Swift.Result<__C.CKShareMetadata, Swift.Error>) -> ())?
0x197e3c8e4  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareMetadataOperation.fetchShareMetadataResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3c714  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareMetadataOperation.fetchShareMetadataResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c41730  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchShareMetadataOperation.fetchShareMetadataResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3bfd0  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareMetadataOperation.fetchShareMetadataResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3c1ac  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareMetadataOperation.rootRecordDesiredKeys.modify : [Swift.String]?
0x197e3c0cc  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareMetadataOperation.rootRecordDesiredKeys.getter : [Swift.String]?
0x1e0c41710  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchShareMetadataOperation.rootRecordDesiredKeys : [Swift.String]?
0x197e3c14c  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareMetadataOperation.rootRecordDesiredKeys.setter : [Swift.String]?
0x197e3eb40  __TEXT,__text  (extension in CloudKit):__C.CKFetchSubscriptionsOperation.fetchSubscriptionsResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3e74c  __TEXT,__text  (extension in CloudKit):__C.CKFetchSubscriptionsOperation.fetchSubscriptionsResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c417b0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchSubscriptionsOperation.fetchSubscriptionsResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3dc5c  __TEXT,__text  (extension in CloudKit):__C.CKFetchSubscriptionsOperation.fetchSubscriptionsResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3dd4c  __TEXT,__text  (extension in CloudKit):__C.CKFetchSubscriptionsOperation.init(subscriptionIDs: [Swift.String]) -> __C.CKFetchSubscriptionsOperation
0x197e3de98  __TEXT,__text  (extension in CloudKit):__C.CKFetchSubscriptionsOperation.subscriptionIDs.modify : [Swift.String]?
0x197e3ddb8  __TEXT,__text  (extension in CloudKit):__C.CKFetchSubscriptionsOperation.subscriptionIDs.getter : [Swift.String]?
0x1e0c41780  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchSubscriptionsOperation.subscriptionIDs : [Swift.String]?
0x197e3de38  __TEXT,__text  (extension in CloudKit):__C.CKFetchSubscriptionsOperation.subscriptionIDs.setter : [Swift.String]?
0x197e3e308  __TEXT,__text  (extension in CloudKit):__C.CKFetchSubscriptionsOperation.perSubscriptionResultBlock.modify : ((Swift.String, Swift.Result<__C.CKSubscription, Swift.Error>) -> ())?
0x197e3df28  __TEXT,__text  (extension in CloudKit):__C.CKFetchSubscriptionsOperation.perSubscriptionResultBlock.getter : ((Swift.String, Swift.Result<__C.CKSubscription, Swift.Error>) -> ())?
0x1e0c41790  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchSubscriptionsOperation.perSubscriptionResultBlock : ((Swift.String, Swift.Result<__C.CKSubscription, Swift.Error>) -> ())?
0x197e3db68  __TEXT,__text  (extension in CloudKit):__C.CKFetchSubscriptionsOperation.perSubscriptionResultBlock.setter : ((Swift.String, Swift.Result<__C.CKSubscription, Swift.Error>) -> ())?
0x197e3e6c8  __TEXT,__text  (extension in CloudKit):__C.CKFetchSubscriptionsOperation.fetchSubscriptionCompletionBlock.modify : (([Swift.String : __C.CKSubscription]?, Swift.Error?) -> ())?
0x197e3e38c  __TEXT,__text  (extension in CloudKit):__C.CKFetchSubscriptionsOperation.fetchSubscriptionCompletionBlock.getter : (([Swift.String : __C.CKSubscription]?, Swift.Error?) -> ())?
0x1e0c417a0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchSubscriptionsOperation.fetchSubscriptionCompletionBlock : (([Swift.String : __C.CKSubscription]?, Swift.Error?) -> ())?
0x197e3e4f4  __TEXT,__text  (extension in CloudKit):__C.CKFetchSubscriptionsOperation.fetchSubscriptionCompletionBlock.setter : (([Swift.String : __C.CKSubscription]?, Swift.Error?) -> ())?
0x197ea8630  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteReferencedObjectTable.lookUpEntry(Swift.AnyObject) throws -> ()
0x197ea85ec  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteReferencedObjectTable.fetchPrimaryKey(forEntry: Swift.AnyObject) throws -> ()
0x197ea8750  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteReferencedObjectTable.referenceWasDeleted(Swift.Int) throws -> ()
0x197ea8674  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteReferencedObjectTable.willStoreReferenceToUnsavedEntry(Swift.AnyObject) throws -> ()
0x197e16c9c  __TEXT,__text  static (extension in CloudKit):__C.CKServerTimestampRecordDomain.supportsSecureCoding.getter : Swift.Bool
0x197ef3dd8  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKServerTimestampRecordDomain.supportsSecureCoding : Swift.Bool
0x197e16bec  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordDomain.copy(with: ObjectiveC.NSZone?) -> Any
0x197e16aec  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordDomain.hash.getter : Swift.Int
0x197e16a28  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordDomain.type.getter : __C.CKServerTimestampDomainType
0x197ef3dd8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKServerTimestampRecordDomain.type : __C.CKServerTimestampDomainType
0x1eba83388  __DATA,__data  direct field offset for (extension in CloudKit):__C.CKServerTimestampRecordDomain.type : __C.CKServerTimestampDomainType
0x197e18e34  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordDomain.init(coder: __C.NSCoder) -> __C.CKServerTimestampRecordDomain?
0x197e16d50  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordDomain.init(coder: __C.NSCoder) -> __C.CKServerTimestampRecordDomain?
0x197e16ca0  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordDomain.encode(with: __C.NSCoder) -> ()
0x197e16b2c  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordDomain.isEqual(Any?) -> Swift.Bool
0x197e16a34  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordDomain.init(recordID: __C.CKRecordID) -> __C.CKServerTimestampRecordDomain
0x197e16a70  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordDomain.init(recordID: __C.CKRecordID) -> __C.CKServerTimestampRecordDomain
0x197e169f8  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordDomain.recordID.getter : __C.CKRecordID
0x197ef3dd8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKServerTimestampRecordDomain.recordID : __C.CKRecordID
0x1eba83380  __DATA,__data  direct field offset for (extension in CloudKit):__C.CKServerTimestampRecordDomain.recordID : __C.CKRecordID
0x197e18e4c  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordDomain.init() -> __C.CKServerTimestampRecordDomain
0x197ecbbb8  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordDomain.init() -> __C.CKServerTimestampRecordDomain
0x197e181dc  __TEXT,__text  type metadata accessor for __C.CKServerTimestampRecordDomain
0x197e3da40  __TEXT,__text  (extension in CloudKit):__C.CKShareRequestAccessOperation.shareAccessRequestResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3d7f4  __TEXT,__text  (extension in CloudKit):__C.CKShareRequestAccessOperation.shareAccessRequestResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c41770  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKShareRequestAccessOperation.shareAccessRequestResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3d160  __TEXT,__text  (extension in CloudKit):__C.CKShareRequestAccessOperation.shareAccessRequestResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3d76c  __TEXT,__text  (extension in CloudKit):__C.CKShareRequestAccessOperation.perShareAccessRequestResultBlock.modify : ((Foundation.URL, Swift.Result<(), Swift.Error>) -> ())?
0x197e3d25c  __TEXT,__text  (extension in CloudKit):__C.CKShareRequestAccessOperation.perShareAccessRequestResultBlock.getter : ((Foundation.URL, Swift.Result<(), Swift.Error>) -> ())?
0x1e0c41760  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKShareRequestAccessOperation.perShareAccessRequestResultBlock : ((Foundation.URL, Swift.Result<(), Swift.Error>) -> ())?
0x197e3d3f0  __TEXT,__text  (extension in CloudKit):__C.CKShareRequestAccessOperation.perShareAccessRequestResultBlock.setter : ((Foundation.URL, Swift.Result<(), Swift.Error>) -> ())?
0x197dfc868  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.init(excludeDevicesWithoutCapabilityCheckingSupport: Swift.Bool, excludeZoneAccessBefore: Foundation.Date?) -> __C.CKDeviceCapabilityCheckOptions
0x197dfc920  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.init(excludeDevicesWithoutCapabilityCheckingSupport: Swift.Bool, excludeZoneAccessBefore: Foundation.Date?) -> __C.CKDeviceCapabilityCheckOptions
0x197dfcab4  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.excludeDevicesWithoutCapabilityCheckingSupport.getter : Swift.Bool
0x197ef1fd0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.excludeDevicesWithoutCapabilityCheckingSupport : Swift.Bool
0x197dfd4b8  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.description.getter : Swift.String
0x197dfcc54  __TEXT,__text  static (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.supportsSecureCoding.getter : Swift.Bool
0x197ef1fd0  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.supportsSecureCoding : Swift.Bool
0x197dfcbd0  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.excludeZoneAccessBefore.getter : Foundation.Date?
0x197ef1fd0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.excludeZoneAccessBefore : Foundation.Date?
0x197dfd140  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.copy(with: ObjectiveC.NSZone?) -> Any
0x197dfd414  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.hash.getter : Swift.Int
0x197dfdd90  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.init(coder: __C.NSCoder) -> __C.CKDeviceCapabilityCheckOptions?
0x197dfce88  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.init(coder: __C.NSCoder) -> __C.CKDeviceCapabilityCheckOptions?
0x197dfcc58  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.encode(with: __C.NSCoder) -> ()
0x197dfd214  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.isEqual(Any?) -> Swift.Bool
0x197dfadb4  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.wrapped.getter : CloudKit.CKDeviceCapabilityCheckOptions?
0x197ef1fd0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.wrapped : CloudKit.CKDeviceCapabilityCheckOptions?
0x197dfad38  __TEXT,__text  (extension in CloudKit):__C.CKDeviceCapabilityCheckOptions.init(CloudKit.CKDeviceCapabilityCheckOptions) -> __C.CKDeviceCapabilityCheckOptions
0x197dfdbec  __TEXT,__text  type metadata accessor for __C.CKDeviceCapabilityCheckOptions
0x197e3fd6c  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.undeprecated_modifySubscriptionsCompletionBlock.modify : (([__C.CKSubscription]?, [Swift.String]?, Swift.Error?) -> ())?
0x197e3fb78  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.undeprecated_modifySubscriptionsCompletionBlock.getter : (([__C.CKSubscription]?, [Swift.String]?, Swift.Error?) -> ())?
0x1e0c41800  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifySubscriptionsOperation.undeprecated_modifySubscriptionsCompletionBlock : (([__C.CKSubscription]?, [Swift.String]?, Swift.Error?) -> ())?
0x197e3fce0  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.undeprecated_modifySubscriptionsCompletionBlock.setter : (([__C.CKSubscription]?, [Swift.String]?, Swift.Error?) -> ())?
0x197e401dc  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.modifySubscriptionsResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3fdec  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.modifySubscriptionsResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c41810  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifySubscriptionsOperation.modifySubscriptionsResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3ef90  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.modifySubscriptionsResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e3faf8  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.modifySubscriptionsCompletionBlock.modify : (([__C.CKSubscription]?, [Swift.String]?, Swift.Error?) -> ())?
0x197e3f828  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.modifySubscriptionsCompletionBlock.getter : (([__C.CKSubscription]?, [Swift.String]?, Swift.Error?) -> ())?
0x1e0c417f0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifySubscriptionsOperation.modifySubscriptionsCompletionBlock : (([__C.CKSubscription]?, [Swift.String]?, Swift.Error?) -> ())?
0x197e3f990  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.modifySubscriptionsCompletionBlock.setter : (([__C.CKSubscription]?, [Swift.String]?, Swift.Error?) -> ())?
0x197e3ed2c  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.init(subscriptionsToSave: [__C.CKSubscription]?, subscriptionIDsToDelete: [Swift.String]?) -> __C.CKModifySubscriptionsOperation
0x197e3f1b4  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.subscriptionIDsToDelete.modify : [Swift.String]?
0x197e3f0d4  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.subscriptionIDsToDelete.getter : [Swift.String]?
0x1e0c417c0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifySubscriptionsOperation.subscriptionIDsToDelete : [Swift.String]?
0x197e3f154  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.subscriptionIDsToDelete.setter : [Swift.String]?
0x197e3f3d4  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.perSubscriptionSaveBlock.modify : ((Swift.String, Swift.Result<__C.CKSubscription, Swift.Error>) -> ())?
0x197e3f244  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.perSubscriptionSaveBlock.getter : ((Swift.String, Swift.Result<__C.CKSubscription, Swift.Error>) -> ())?
0x1e0c417d0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifySubscriptionsOperation.perSubscriptionSaveBlock : ((Swift.String, Swift.Result<__C.CKSubscription, Swift.Error>) -> ())?
0x197e3ede8  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.perSubscriptionSaveBlock.setter : ((Swift.String, Swift.Result<__C.CKSubscription, Swift.Error>) -> ())?
0x197e3f720  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.perSubscriptionDeleteBlock.modify : ((Swift.String, Swift.Result<(), Swift.Error>) -> ())?
0x197e3f454  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.perSubscriptionDeleteBlock.getter : ((Swift.String, Swift.Result<(), Swift.Error>) -> ())?
0x1e0c417e0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKModifySubscriptionsOperation.perSubscriptionDeleteBlock : ((Swift.String, Swift.Result<(), Swift.Error>) -> ())?
0x197e3eebc  __TEXT,__text  (extension in CloudKit):__C.CKModifySubscriptionsOperation.perSubscriptionDeleteBlock.setter : ((Swift.String, Swift.Result<(), Swift.Error>) -> ())?
0x197e40768  __TEXT,__text  (extension in CloudKit):__C.CKFetchDatabaseChangesOperation.undeprecated_fetchDatabaseChangesCompletionBlock.modify : ((__C.CKServerChangeToken?, Swift.Bool, Swift.Error?) -> ())?
0x197e40420  __TEXT,__text  (extension in CloudKit):__C.CKFetchDatabaseChangesOperation.undeprecated_fetchDatabaseChangesCompletionBlock.getter : ((__C.CKServerChangeToken?, Swift.Bool, Swift.Error?) -> ())?
0x1e0c41820  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchDatabaseChangesOperation.undeprecated_fetchDatabaseChangesCompletionBlock : ((__C.CKServerChangeToken?, Swift.Bool, Swift.Error?) -> ())?
0x197e405d4  __TEXT,__text  (extension in CloudKit):__C.CKFetchDatabaseChangesOperation.undeprecated_fetchDatabaseChangesCompletionBlock.setter : ((__C.CKServerChangeToken?, Swift.Bool, Swift.Error?) -> ())?
0x197e40ae4  __TEXT,__text  (extension in CloudKit):__C.CKFetchDatabaseChangesOperation.fetchDatabaseChangesResultBlock.modify : ((Swift.Result<(serverChangeToken: __C.CKServerChangeToken, moreComing: Swift.Bool), Swift.Error>) -> ())?
0x197e407f0  __TEXT,__text  (extension in CloudKit):__C.CKFetchDatabaseChangesOperation.fetchDatabaseChangesResultBlock.getter : ((Swift.Result<(serverChangeToken: __C.CKServerChangeToken, moreComing: Swift.Bool), Swift.Error>) -> ())?
0x1e0c41830  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchDatabaseChangesOperation.fetchDatabaseChangesResultBlock : ((Swift.Result<(serverChangeToken: __C.CKServerChangeToken, moreComing: Swift.Bool), Swift.Error>) -> ())?
0x197e40338  __TEXT,__text  (extension in CloudKit):__C.CKFetchDatabaseChangesOperation.fetchDatabaseChangesResultBlock.setter : ((Swift.Result<(serverChangeToken: __C.CKServerChangeToken, moreComing: Swift.Bool), Swift.Error>) -> ())?
0x197ea8834  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteReferencedDataArrayTable.addData(data: Foundation.Data, toReferencedDataArray: Swift.Int) throws -> ()
0x197e43e68  __TEXT,__text  (extension in CloudKit):__C.CKDiscoverUserIdentitiesOperation.discoverUserIdentitiesResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e43cd0  __TEXT,__text  (extension in CloudKit):__C.CKDiscoverUserIdentitiesOperation.discoverUserIdentitiesResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c418f0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKDiscoverUserIdentitiesOperation.discoverUserIdentitiesResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e43bb8  __TEXT,__text  (extension in CloudKit):__C.CKDiscoverUserIdentitiesOperation.discoverUserIdentitiesResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e389a4  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.undeprecated_fetchRecordZoneChangesCompletionBlock.modify : ((Swift.Error?) -> ())?
0x197e387c0  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.undeprecated_fetchRecordZoneChangesCompletionBlock.getter : ((Swift.Error?) -> ())?
0x1e0c41650  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.undeprecated_fetchRecordZoneChangesCompletionBlock : ((Swift.Error?) -> ())?
0x197e38924  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.undeprecated_fetchRecordZoneChangesCompletionBlock.setter : ((Swift.Error?) -> ())?
0x197e38274  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.undeprecated_recordZoneFetchCompletionBlock.modify : ((__C.CKRecordZoneID, __C.CKServerChangeToken?, Foundation.Data?, Swift.Bool, Swift.Error?) -> ())?
0x197e37ea0  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.undeprecated_recordZoneFetchCompletionBlock.getter : ((__C.CKRecordZoneID, __C.CKServerChangeToken?, Foundation.Data?, Swift.Bool, Swift.Error?) -> ())?
0x1e0c41630  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.undeprecated_recordZoneFetchCompletionBlock : ((__C.CKRecordZoneID, __C.CKServerChangeToken?, Foundation.Data?, Swift.Bool, Swift.Error?) -> ())?
0x197e3805c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.undeprecated_recordZoneFetchCompletionBlock.setter : ((__C.CKRecordZoneID, __C.CKServerChangeToken?, Foundation.Data?, Swift.Bool, Swift.Error?) -> ())?
0x197e38c2c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.fetchRecordZoneChangesResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e38a24  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.fetchRecordZoneChangesResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c41660  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.fetchRecordZoneChangesResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e37440  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.fetchRecordZoneChangesResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e38740  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.recordZoneFetchResultBlock.modify : ((__C.CKRecordZoneID, Swift.Result<(serverChangeToken: __C.CKServerChangeToken, clientChangeTokenData: Foundation.Data?, moreComing: Swift.Bool), Swift.Error>) -> ())?
0x197e382f4  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.recordZoneFetchResultBlock.getter : ((__C.CKRecordZoneID, Swift.Result<(serverChangeToken: __C.CKServerChangeToken, clientChangeTokenData: Foundation.Data?, moreComing: Swift.Bool), Swift.Error>) -> ())?
0x1e0c41640  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.recordZoneFetchResultBlock : ((__C.CKRecordZoneID, Swift.Result<(serverChangeToken: __C.CKServerChangeToken, clientChangeTokenData: Foundation.Data?, moreComing: Swift.Bool), Swift.Error>) -> ())?
0x197e37374  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.recordZoneFetchResultBlock.setter : ((__C.CKRecordZoneID, Swift.Result<(serverChangeToken: __C.CKServerChangeToken, clientChangeTokenData: Foundation.Data?, moreComing: Swift.Bool), Swift.Error>) -> ())?
0x197e37138  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.init(recordZoneIDs: [__C.CKRecordZoneID]?, configurationsByRecordZoneID: [__C.CKRecordZoneID : __C.CKFetchRecordZoneChangesConfiguration]?) -> __C.CKFetchRecordZoneChangesOperation
0x197e37e20  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.recordWasChangedBlock.modify : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x197e37c90  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.recordWasChangedBlock.getter : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x1e0c41620  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.recordWasChangedBlock : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x197e3721c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.recordWasChangedBlock.setter : ((__C.CKRecordID, Swift.Result<__C.CKRecord, Swift.Error>) -> ())?
0x197e37c10  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.zoneAttributesChangedBlock.modify : ((__C.CKRecordZone) -> ())?
0x197e37aac  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.zoneAttributesChangedBlock.getter : ((__C.CKRecordZone) -> ())?
0x1e0c41610  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.zoneAttributesChangedBlock : ((__C.CKRecordZone) -> ())?
0x197e37500  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.zoneAttributesChangedBlock.setter : ((__C.CKRecordZone) -> ())?
0x197e37a2c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.recordWithIDWasDeletedBlock.modify : ((__C.CKRecordID, Swift.String) -> ())?
0x197e377fc  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.recordWithIDWasDeletedBlock.getter : ((__C.CKRecordID, Swift.String) -> ())?
0x1e0c41600  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.recordWithIDWasDeletedBlock : ((__C.CKRecordID, Swift.String) -> ())?
0x197e372e8  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.recordWithIDWasDeletedBlock.setter : ((__C.CKRecordID, Swift.String) -> ())?
0x197e3777c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.undeprecated_recordChangedBlock.modify : ((__C.CKRecord) -> ())?
0x197e3758c  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.undeprecated_recordChangedBlock.getter : ((__C.CKRecord) -> ())?
0x1e0c415f0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.undeprecated_recordChangedBlock : ((__C.CKRecord) -> ())?
0x197e376f0  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesOperation.undeprecated_recordChangedBlock.setter : ((__C.CKRecord) -> ())?
0x197e44304  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareParticipantsOperation.perShareParticipantResultBlock.modify : ((__C.CKUserIdentityLookupInfo, Swift.Result<__C.CKShareParticipant, Swift.Error>) -> ())?
0x197e44170  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareParticipantsOperation.perShareParticipantResultBlock.getter : ((__C.CKUserIdentityLookupInfo, Swift.Result<__C.CKShareParticipant, Swift.Error>) -> ())?
0x1e0c41900  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchShareParticipantsOperation.perShareParticipantResultBlock : ((__C.CKUserIdentityLookupInfo, Swift.Result<__C.CKShareParticipant, Swift.Error>) -> ())?
0x197e43f10  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareParticipantsOperation.perShareParticipantResultBlock.setter : ((__C.CKUserIdentityLookupInfo, Swift.Result<__C.CKShareParticipant, Swift.Error>) -> ())?
0x197e4454c  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareParticipantsOperation.fetchShareParticipantsResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e4438c  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareParticipantsOperation.fetchShareParticipantsResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c41910  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchShareParticipantsOperation.fetchShareParticipantsResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e44000  __TEXT,__text  (extension in CloudKit):__C.CKFetchShareParticipantsOperation.fetchShareParticipantsResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197ea87c4  __TEXT,__text  (extension in CloudKit):__C.CKSQLiteReferencedCollectionTable.addElement(_: Swift.AnyObject, toCollection: Swift.Int) throws -> ()
0x197e16e64  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.init(recordZoneID: __C.CKRecordZoneID) -> __C.CKServerTimestampRecordZoneDomain
0x197e16ea0  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.init(recordZoneID: __C.CKRecordZoneID) -> __C.CKServerTimestampRecordZoneDomain
0x197e16e28  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.recordZoneID.getter : __C.CKRecordZoneID
0x197ef3dd8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.recordZoneID : __C.CKRecordZoneID
0x1eba83390  __DATA,__data  direct field offset for (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.recordZoneID : __C.CKRecordZoneID
0x197e17070  __TEXT,__text  static (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.supportsSecureCoding.getter : Swift.Bool
0x197ef3dd8  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.supportsSecureCoding : Swift.Bool
0x197e1701c  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.copy(with: ObjectiveC.NSZone?) -> Any
0x197e16f1c  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.hash.getter : Swift.Int
0x197e16e58  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.type.getter : __C.CKServerTimestampDomainType
0x197ef3dd8  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.type : __C.CKServerTimestampDomainType
0x1eba83398  __DATA,__data  direct field offset for (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.type : __C.CKServerTimestampDomainType
0x197e18e38  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.init(coder: __C.NSCoder) -> __C.CKServerTimestampRecordZoneDomain?
0x197e1712c  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.init(coder: __C.NSCoder) -> __C.CKServerTimestampRecordZoneDomain?
0x197e17074  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.encode(with: __C.NSCoder) -> ()
0x197e16f5c  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.isEqual(Any?) -> Swift.Bool
0x197e18e50  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.init() -> __C.CKServerTimestampRecordZoneDomain
0x197ecbbe8  __TEXT,__text  (extension in CloudKit):__C.CKServerTimestampRecordZoneDomain.init() -> __C.CKServerTimestampRecordZoneDomain
0x197e181f0  __TEXT,__text  type metadata accessor for __C.CKServerTimestampRecordZoneDomain
0x197e191d0  __TEXT,__text  static (extension in CloudKit):__C.CKShareParticipantAcceptanceStatus.unsubscribed.getter : __C.CKShareParticipantAcceptanceStatus
0x197e42dac  __TEXT,__text  (extension in CloudKit):__C.CKFetchRegisteredBundleIDsOperation.fetchRegisteredBundleIDsResultBlock.modify : ((Swift.Result<[Swift.String], Swift.Error>) -> ())?
0x197e42848  __TEXT,__text  (extension in CloudKit):__C.CKFetchRegisteredBundleIDsOperation.fetchRegisteredBundleIDsResultBlock.getter : ((Swift.Result<[Swift.String], Swift.Error>) -> ())?
0x1e0c418b0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRegisteredBundleIDsOperation.fetchRegisteredBundleIDsResultBlock : ((Swift.Result<[Swift.String], Swift.Error>) -> ())?
0x197e42730  __TEXT,__text  (extension in CloudKit):__C.CKFetchRegisteredBundleIDsOperation.fetchRegisteredBundleIDsResultBlock.setter : ((Swift.Result<[Swift.String], Swift.Error>) -> ())?
0x197e43b10  __TEXT,__text  (extension in CloudKit):__C.CKDiscoverAllUserIdentitiesOperation.discoverAllUserIdentitiesResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e43978  __TEXT,__text  (extension in CloudKit):__C.CKDiscoverAllUserIdentitiesOperation.discoverAllUserIdentitiesResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c418e0  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKDiscoverAllUserIdentitiesOperation.discoverAllUserIdentitiesResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e43808  __TEXT,__text  (extension in CloudKit):__C.CKDiscoverAllUserIdentitiesOperation.discoverAllUserIdentitiesResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197e38e84  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesConfiguration.desiredKeys.modify : [Swift.String]?
0x197e38d34  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesConfiguration.desiredKeys.getter : [Swift.String]?
0x1e0c41670  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKFetchRecordZoneChangesConfiguration.desiredKeys : [Swift.String]?
0x197e38db4  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesConfiguration.desiredKeys.setter : [Swift.String]?
0x197e370a8  __TEXT,__text  (extension in CloudKit):__C.CKFetchRecordZoneChangesConfiguration.init(previousServerChangeToken: __C.CKServerChangeToken?, resultsLimit: Swift.Int?, desiredKeys: [Swift.String]?) -> __C.CKFetchRecordZoneChangesConfiguration
0x197df9ca4  __TEXT,__text  (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.checkSupportedDeviceCapabilitiesResultBlock.modify : ((Swift.Result<(), Swift.Error>) -> ())?
0x197df9648  __TEXT,__text  (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.checkSupportedDeviceCapabilitiesResultBlock.getter : ((Swift.Result<(), Swift.Error>) -> ())?
0x1e0c4135c  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.checkSupportedDeviceCapabilitiesResultBlock : ((Swift.Result<(), Swift.Error>) -> ())?
0x197df97dc  __TEXT,__text  (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.checkSupportedDeviceCapabilitiesResultBlock.setter : ((Swift.Result<(), Swift.Error>) -> ())?
0x197df84d0  __TEXT,__text  (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.init(desiredCapabilities: CloudKit.CKDeviceCapabilitySet, zoneIDs: [__C.CKRecordZoneID], options: CloudKit.CKDeviceCapabilityCheckOptions?) -> __C.CKCheckSupportedDeviceCapabilitiesOperation
0x197df8b94  __TEXT,__text  (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.desiredCapabilities.getter : CloudKit.CKDeviceCapabilitySet?
0x197ef1e88  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.desiredCapabilities : CloudKit.CKDeviceCapabilitySet?
0x197df95c4  __TEXT,__text  (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.perResultBlock.modify : ((__C.CKRecordZoneID, CloudKit.CKDeviceCapabilitySet, Swift.Result<CloudKit.CKDeviceCapabilityCheckResult, Swift.Error>) -> ())?
0x197df8cd0  __TEXT,__text  (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.perResultBlock.getter : ((__C.CKRecordZoneID, CloudKit.CKDeviceCapabilitySet, Swift.Result<CloudKit.CKDeviceCapabilityCheckResult, Swift.Error>) -> ())?
0x1e0c4134c  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.perResultBlock : ((__C.CKRecordZoneID, CloudKit.CKDeviceCapabilitySet, Swift.Result<CloudKit.CKDeviceCapabilityCheckResult, Swift.Error>) -> ())?
0x197df8e64  __TEXT,__text  (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.perResultBlock.setter : ((__C.CKRecordZoneID, CloudKit.CKDeviceCapabilitySet, Swift.Result<CloudKit.CKDeviceCapabilityCheckResult, Swift.Error>) -> ())?
0x197df8684  __TEXT,__text  (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.init(desiredCapabilitySets: [CloudKit.CKDeviceCapabilitySet], zoneIDs: [__C.CKRecordZoneID], options: CloudKit.CKDeviceCapabilityCheckOptions?) -> __C.CKCheckSupportedDeviceCapabilitiesOperation
0x197df88f4  __TEXT,__text  (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.desiredCapabilitySets.getter : [CloudKit.CKDeviceCapabilitySet]
0x197ef1e88  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.desiredCapabilitySets : [CloudKit.CKDeviceCapabilitySet]
0x197df8c60  __TEXT,__text  (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.options.getter : CloudKit.CKDeviceCapabilityCheckOptions?
0x197ef1e88  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.options : CloudKit.CKDeviceCapabilityCheckOptions?
0x197df8c08  __TEXT,__text  (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.zoneIDs.getter : [__C.CKRecordZoneID]
0x197ef1e88  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKCheckSupportedDeviceCapabilitiesOperation.zoneIDs : [__C.CKRecordZoneID]
0x197ef34bc  __TEXT,__const  protocol conformance descriptor for __C.NSData : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca4b80  __AUTH_CONST,__const  protocol witness table for __C.NSData : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef3494  __TEXT,__const  protocol conformance descriptor for __C.NSDate : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca4b68  __AUTH_CONST,__const  protocol witness table for __C.NSDate : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef3554  __TEXT,__const  protocol conformance descriptor for __C.CKAsset : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca4b50  __AUTH_CONST,__const  protocol witness table for __C.CKAsset : CloudKit.CKRecordValueProtocol in CloudKit
0x197dc3878  __TEXT,__text  (extension in CloudKit):__C.CKAsset.ExportedAssetID.description.getter : Swift.String
0x197eef4d0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAsset.ExportedAssetID.description : Swift.String
0x197dc3a84  __TEXT,__text  (extension in CloudKit):__C.CKAsset.ExportedAssetID.customMirror.getter : Swift.Mirror
0x197eef4d0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAsset.ExportedAssetID.customMirror : Swift.Mirror
0x197dc3a50  __TEXT,__text  (extension in CloudKit):__C.CKAsset.ExportedAssetID.debugDescription.getter : Swift.String
0x197eef4d0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAsset.ExportedAssetID.debugDescription : Swift.String
0x197dc33d4  __TEXT,__text  (extension in CloudKit):__C.CKAsset.ExportedAssetID.init(from: Swift.Decoder) throws -> (extension in CloudKit):__C.CKAsset.ExportedAssetID
0x197dc3658  __TEXT,__text  (extension in CloudKit):__C.CKAsset.ExportedAssetID.encode(to: Swift.Encoder) throws -> ()
0x197dc730c  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKAsset.ExportedAssetID
0x197f27ecc  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKAsset.ExportedAssetID
0x1e3ca49e0  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKAsset.ExportedAssetID
0x197eef458  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.ExportedAssetID : Swift.Encodable in CloudKit
0x197eef430  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.ExportedAssetID : Swift.Decodable in CloudKit
0x197eef4a8  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.ExportedAssetID : Swift.CustomReflectable in CloudKit
0x197eef480  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.ExportedAssetID : Swift.CustomStringConvertible in CloudKit
0x197dc8fd0  __TEXT,__text  (extension in CloudKit):__C.CKAsset.ID.description.getter : Swift.String
0x197eefd04  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAsset.ID.description : Swift.String
0x197dc8244  __TEXT,__text  static (extension in CloudKit):__C.CKAsset.ID.== infix((extension in CloudKit):__C.CKAsset.ID, (extension in CloudKit):__C.CKAsset.ID) -> Swift.Bool
0x197dc8ad0  __TEXT,__text  (extension in CloudKit):__C.CKAsset.ID.init(from: Swift.Decoder) throws -> (extension in CloudKit):__C.CKAsset.ID
0x197dc8098  __TEXT,__text  (extension in CloudKit):__C.CKAsset.ID.hash(into: inout Swift.Hasher) -> ()
0x197dc8670  __TEXT,__text  (extension in CloudKit):__C.CKAsset.ID.encode(to: Swift.Encoder) throws -> ()
0x197dc8130  __TEXT,__text  (extension in CloudKit):__C.CKAsset.ID.hashValue.getter : Swift.Int
0x197eefd04  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAsset.ID.hashValue : Swift.Int
0x197dc7fc8  __TEXT,__text  (extension in CloudKit):__C.CKAsset.ID.signature.getter : (extension in CloudKit):__C.CKAsset.Signature
0x197eefd00  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAsset.ID.signature : (extension in CloudKit):__C.CKAsset.Signature
0x197dcd7bc  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKAsset.ID
0x197f27fa8  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKAsset.ID
0x1e3ca4810  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKAsset.ID
0x197eefcb0  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.ID : Swift.Encodable in CloudKit
0x197eefc20  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.ID : Swift.Hashable in CloudKit
0x197eefc60  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.ID : Swift.Equatable in CloudKit
0x197eefc88  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.ID : Swift.Decodable in CloudKit
0x197eefcd8  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.ID : Swift.CustomStringConvertible in CloudKit
0x197dc7fd4  __TEXT,__text  (extension in CloudKit):__C.CKAsset.assetID.getter : (extension in CloudKit):__C.CKAsset.ID?
0x197eefd04  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAsset.assetID : (extension in CloudKit):__C.CKAsset.ID?
0x197dc3c24  __TEXT,__text  (extension in CloudKit):__C.CKAsset.init(copying: (extension in CloudKit):__C.CKAsset.ID) -> __C.CKAsset
0x197dcdf3c  __TEXT,__text  (extension in CloudKit):__C.CKAsset.Signature.description.getter : Swift.String
0x197ef0250  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAsset.Signature.description : Swift.String
0x197dcdaac  __TEXT,__text  static (extension in CloudKit):__C.CKAsset.Signature.== infix((extension in CloudKit):__C.CKAsset.Signature, (extension in CloudKit):__C.CKAsset.Signature) -> Swift.Bool
0x197dcdd78  __TEXT,__text  (extension in CloudKit):__C.CKAsset.Signature.init(from: Swift.Decoder) throws -> (extension in CloudKit):__C.CKAsset.Signature
0x197dcdd24  __TEXT,__text  (extension in CloudKit):__C.CKAsset.Signature.hash(into: inout Swift.Hasher) -> ()
0x197dcdbc0  __TEXT,__text  (extension in CloudKit):__C.CKAsset.Signature.encode(to: Swift.Encoder) throws -> ()
0x197dcdd2c  __TEXT,__text  (extension in CloudKit):__C.CKAsset.Signature.hashValue.getter : Swift.Int
0x197ef0250  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAsset.Signature.hashValue : Swift.Int
0x197dce9d0  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKAsset.Signature
0x197f27fe0  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKAsset.Signature
0x1e3ca4338  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKAsset.Signature
0x197ef0198  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.Signature : Swift.Encodable in CloudKit
0x197ef01e8  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.Signature : Swift.Hashable in CloudKit
0x197ef01c0  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.Signature : Swift.Equatable in CloudKit
0x197ef0170  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.Signature : Swift.Decodable in CloudKit
0x197ef0228  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKAsset.Signature : Swift.CustomStringConvertible in CloudKit
0x197dc3838  __TEXT,__text  (extension in CloudKit):__C.CKAsset.init(importing: (extension in CloudKit):__C.CKAsset.ExportedAssetID) -> __C.CKAsset
0x197e0bda8  __TEXT,__text  (extension in CloudKit):__C.CKQuery.init(recordType: Swift.String, predicate: __C.NSPredicate) -> __C.CKQuery
0x197e0be20  __TEXT,__text  (extension in CloudKit):__C.CKQuery.recordType.getter : Swift.String
0x197ef2a5c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKQuery.recordType : Swift.String
0x197e1908c  __TEXT,__text  (extension in CloudKit):__C.CKShare.oneTimeURL(for: Swift.String) -> Foundation.URL?
0x197e18edc  __TEXT,__text  static (extension in CloudKit):__C.CKShare.SystemFieldKey.thumbnailImageData.getter : Swift.String
0x197ef4734  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKShare.SystemFieldKey.thumbnailImageData : Swift.String
0x197e18e8c  __TEXT,__text  static (extension in CloudKit):__C.CKShare.SystemFieldKey.title.getter : Swift.String
0x197ef4734  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKShare.SystemFieldKey.title : Swift.String
0x197e18f2c  __TEXT,__text  static (extension in CloudKit):__C.CKShare.SystemFieldKey.shareType.getter : Swift.String
0x197ef4734  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKShare.SystemFieldKey.shareType : Swift.String
0x197e191b0  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKShare.SystemFieldKey
0x197f288cc  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKShare.SystemFieldKey
0x1e3ca42c0  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKShare.SystemFieldKey
0x197ef3510  __TEXT,__const  protocol conformance descriptor for __C.NSArray : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca4238  __AUTH_CONST,__const  protocol witness table for __C.NSArray : CloudKit.CKRecordValueProtocol in CloudKit
0x197e0d0d8  __TEXT,__text  static (extension in CloudKit):__C.CKRecord.SystemType.userRecord.getter : Swift.String
0x197ef2b24  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKRecord.SystemType.userRecord : Swift.String
0x197e0d128  __TEXT,__text  static (extension in CloudKit):__C.CKRecord.SystemType.share.getter : Swift.String
0x197ef2b24  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKRecord.SystemType.share : Swift.String
0x197e0d8c4  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKRecord.SystemType
0x197f2851c  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKRecord.SystemType
0x1e3ca4218  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKRecord.SystemType
0x197c34514  __TEXT,__text  (extension in CloudKit):__C.CKRecord.init(recordType: Swift.String, recordID: __C.CKRecordID) -> __C.CKRecord
0x197e0d224  __TEXT,__text  (extension in CloudKit):__C.CKRecord.init(recordType: Swift.String, zoneID: __C.CKRecordZoneID) -> __C.CKRecord
0x197e0d354  __TEXT,__text  (extension in CloudKit):__C.CKRecord.recordType.getter : Swift.String
0x197ef2b24  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRecord.recordType : Swift.String
0x197e0d5dc  __TEXT,__text  (extension in CloudKit):__C.CKRecord.changedKeys() -> [Swift.String]
0x197e0c178  __TEXT,__text  (extension in CloudKit):__C.CKRecord.makeIterator() -> CloudKit.CKRecordKeyValueIterator
0x197e0d160  __TEXT,__text  static (extension in CloudKit):__C.CKRecord.SystemFieldKey.creationDate.getter : Swift.String
0x197ef2b24  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKRecord.SystemFieldKey.creationDate : Swift.String
0x197e0d178  __TEXT,__text  static (extension in CloudKit):__C.CKRecord.SystemFieldKey.modificationDate.getter : Swift.String
0x197ef2b24  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKRecord.SystemFieldKey.modificationDate : Swift.String
0x197e0d154  __TEXT,__text  static (extension in CloudKit):__C.CKRecord.SystemFieldKey.creatorUserRecordID.getter : Swift.String
0x197ef2b24  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKRecord.SystemFieldKey.creatorUserRecordID : Swift.String
0x197e0d16c  __TEXT,__text  static (extension in CloudKit):__C.CKRecord.SystemFieldKey.lastModifiedUserRecordID.getter : Swift.String
0x197ef2b24  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKRecord.SystemFieldKey.lastModifiedUserRecordID : Swift.String
0x197e0d204  __TEXT,__text  static (extension in CloudKit):__C.CKRecord.SystemFieldKey.share.getter : Swift.String
0x197ef2b24  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKRecord.SystemFieldKey.share : Swift.String
0x197e0d1b4  __TEXT,__text  static (extension in CloudKit):__C.CKRecord.SystemFieldKey.parent.getter : Swift.String
0x197ef2b24  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKRecord.SystemFieldKey.parent : Swift.String
0x197e0d148  __TEXT,__text  static (extension in CloudKit):__C.CKRecord.SystemFieldKey.recordID.getter : Swift.String
0x197ef2b24  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKRecord.SystemFieldKey.recordID : Swift.String
0x197e0d8d4  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKRecord.SystemFieldKey
0x197f28538  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKRecord.SystemFieldKey
0x1e3ca4188  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKRecord.SystemFieldKey
0x197e0d624  __TEXT,__text  (extension in CloudKit):__C.CKRecord.creationTimestamp.getter : CloudKit.CKServerTimestamp?
0x197ef2b24  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRecord.creationTimestamp : CloudKit.CKServerTimestamp?
0x197e3a5a8  __TEXT,__text  (extension in CloudKit):__C.CKRecord.FetchConfiguration.description.getter : Swift.String
0x197ef5ae4  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRecord.FetchConfiguration.description : Swift.String
0x197e3a308  __TEXT,__text  (extension in CloudKit):__C.CKRecord.FetchConfiguration.init(desiredKeys: [Swift.String]?) -> (extension in CloudKit):__C.CKRecord.FetchConfiguration
0x197e3a414  __TEXT,__text  (extension in CloudKit):__C.CKRecord.FetchConfiguration.desiredKeys.modify : [Swift.String]?
0x197e3a3e0  __TEXT,__text  (extension in CloudKit):__C.CKRecord.FetchConfiguration.desiredKeys.getter : [Swift.String]?
0x197ef5ae0  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRecord.FetchConfiguration.desiredKeys : [Swift.String]?
0x197e3a3e8  __TEXT,__text  (extension in CloudKit):__C.CKRecord.FetchConfiguration.desiredKeys.setter : [Swift.String]?
0x197e3a434  __TEXT,__text  static (extension in CloudKit):__C.CKRecord.FetchConfiguration.== infix((extension in CloudKit):__C.CKRecord.FetchConfiguration, (extension in CloudKit):__C.CKRecord.FetchConfiguration) -> Swift.Bool
0x197e3a474  __TEXT,__text  (extension in CloudKit):__C.CKRecord.FetchConfiguration.hash(into: inout Swift.Hasher) -> ()
0x197e3a4d8  __TEXT,__text  (extension in CloudKit):__C.CKRecord.FetchConfiguration.hashValue.getter : Swift.Int
0x197ef5ae4  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRecord.FetchConfiguration.hashValue : Swift.Int
0x197e3af90  __TEXT,__text  type metadata accessor for (extension in CloudKit):__C.CKRecord.FetchConfiguration
0x197f29084  __TEXT,__constg_swiftt  nominal type descriptor for (extension in CloudKit):__C.CKRecord.FetchConfiguration
0x1e3ca40f0  __AUTH_CONST,__const  type metadata for (extension in CloudKit):__C.CKRecord.FetchConfiguration
0x197ef5a78  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKRecord.FetchConfiguration : Swift.Hashable in CloudKit
0x197ef5a50  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKRecord.FetchConfiguration : Swift.Equatable in CloudKit
0x197ef5ab8  __TEXT,__const  protocol conformance descriptor for (extension in CloudKit):__C.CKRecord.FetchConfiguration : Swift.CustomStringConvertible in CloudKit
0x197e0d6a0  __TEXT,__text  (extension in CloudKit):__C.CKRecord.modificationTimestamp.getter : CloudKit.CKServerTimestamp?
0x197ef2b24  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKRecord.modificationTimestamp : CloudKit.CKServerTimestamp?
0x197bb8d1c  __TEXT,__text  (extension in CloudKit):__C.CKRecord.object(forKey: Swift.String) -> __C.CKRecordValue?
0x197e0c034  __TEXT,__text  (extension in CloudKit):__C.CKRecord.allKeys() -> [Swift.String]
0x197e0d3a4  __TEXT,__text  (extension in CloudKit):__C.CKRecord.setObject(_: __C.CKRecordValue?, forKey: Swift.String) -> ()
0x197e0d4e0  __TEXT,__text  (extension in CloudKit):__C.CKRecord.subscript.modify : (Swift.String) -> __C.CKRecordValue?
0x197bb8d18  __TEXT,__text  (extension in CloudKit):__C.CKRecord.subscript.getter : (Swift.String) -> __C.CKRecordValue?
0x1e0c41428  __DATA_CONST,__const  property descriptor for (extension in CloudKit):__C.CKRecord.subscript(Swift.String) -> __C.CKRecordValue?
0x197e0d474  __TEXT,__text  (extension in CloudKit):__C.CKRecord.subscript.setter : (Swift.String) -> __C.CKRecordValue?
0x197ef2abc  __TEXT,__const  protocol conformance descriptor for __C.CKRecord : Swift.Sequence in CloudKit
0x197ea7bc8  __TEXT,__text  (extension in CloudKit):__C.CKSQLite.performDatabaseOperation(_: (__C.CKSQLiteDB, () -> Swift.Bool) -> (), errorHandler: ((Swift.Error) -> __C.CKSQLiteErrorResponse)?) throws -> ()
0x197ef34e4  __TEXT,__const  protocol conformance descriptor for __C.NSNumber : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca3e40  __AUTH_CONST,__const  protocol witness table for __C.NSNumber : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef3468  __TEXT,__const  protocol conformance descriptor for __C.NSString : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca3e28  __AUTH_CONST,__const  protocol witness table for __C.NSString : CloudKit.CKRecordValueProtocol in CloudKit
0x197ec22a0  __TEXT,__text  (extension in CloudKit):__C.ACAccount.persona.getter : __C.CKPersona?
0x197efb20c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.ACAccount.persona : __C.CKPersona?
0x197ec3250  __TEXT,__text  (extension in CloudKit):__C.ACAccount.__ck_get(Swift.AutoreleasingUnsafeMutablePointer<__C.CKPersona?>?) throws -> ()
0x197dc9d14  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.mergeableDeltaID.getter : __C.CKMergeableDeltaID?
0x197eefd04  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAssetID.mergeableDeltaID : __C.CKMergeableDeltaID?
0x197dc9ad4  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.recordID.getter : __C.CKRecordID
0x197eefd04  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAssetID.recordID : __C.CKRecordID
0x197dcaa58  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.init(containerID: __C.CKContainerID?, recordID: __C.CKRecordID, mergeableDeltaID: __C.CKMergeableDeltaID, signature: __C.CKAssetSignature, referenceSignature: Foundation.Data?, size: Foundation.Measurement<__C.NSUnitInformationStorage>?, paddedSize: Foundation.M
0x197dcabcc  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.init(containerID: __C.CKContainerID?, recordID: __C.CKRecordID, mergeableDeltaID: __C.CKMergeableDeltaID, signature: __C.CKAssetSignature, referenceSignature: Foundation.Data?, size: Foundation.Measurement<__C.NSUnitInformationStorage>?, paddedSize: Foundation.M
0x197dca098  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.init(containerID: __C.CKContainerID?, recordID: __C.CKRecordID, fieldKey: Swift.String, index: Swift.Int, signature: __C.CKAssetSignature, referenceSignature: Foundation.Data?, size: Foundation.Measurement<__C.NSUnitInformationStorage>?, paddedSize: Foundation.M
0x197dca244  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.init(containerID: __C.CKContainerID?, recordID: __C.CKRecordID, fieldKey: Swift.String, index: Swift.Int, signature: __C.CKAssetSignature, referenceSignature: Foundation.Data?, size: Foundation.Measurement<__C.NSUnitInformationStorage>?, paddedSize: Foundation.M
0x197dc9a80  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.containerID.getter : __C.CKContainerID?
0x197eefd04  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAssetID.containerID : __C.CKContainerID?
0x197dca014  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.paddedSize.getter : Foundation.Measurement<__C.NSUnitInformationStorage>?
0x197eefd04  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAssetID.paddedSize : Foundation.Measurement<__C.NSUnitInformationStorage>?
0x197dcb344  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.description.getter : Swift.String
0x197dc9e44  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.referenceSignature.getter : Foundation.Data?
0x197eefd04  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAssetID.referenceSignature : Foundation.Data?
0x197dcb4c4  __TEXT,__text  static (extension in CloudKit):__C.CKAssetID.supportsSecureCoding.getter : Swift.Bool
0x197eefd04  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKAssetID.supportsSecureCoding : Swift.Bool
0x197dcb424  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.copy(with: ObjectiveC.NSZone?) -> Any
0x197dcb238  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.hash.getter : Swift.Int
0x197dc9e8c  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.size.getter : Foundation.Measurement<__C.NSUnitInformationStorage>?
0x197eefd04  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAssetID.size : Foundation.Measurement<__C.NSUnitInformationStorage>?
0x197dcb8b8  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.init(coder: __C.NSCoder) -> __C.CKAssetID?
0x197dcb8f8  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.init(coder: __C.NSCoder) -> __C.CKAssetID?
0x197dc9c70  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.index.getter : Swift.Int
0x197eefd04  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAssetID.index : Swift.Int
0x197dcb4cc  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.encode(with: __C.NSCoder) -> ()
0x197dcb0c8  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.isEqual(Any?) -> Swift.Bool
0x197dc9b5c  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.fieldKey.getter : Swift.String?
0x197eefd04  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAssetID.fieldKey : Swift.String?
0x197dc9d94  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.signature.getter : __C.CKAssetSignature
0x197eefd04  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKAssetID.signature : __C.CKAssetSignature
0x197dcc140  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.init() -> __C.CKAssetID
0x197ecbb58  __TEXT,__text  (extension in CloudKit):__C.CKAssetID.init() -> __C.CKAssetID
0x197dcd618  __TEXT,__text  type metadata accessor for __C.CKAssetID
0x197ef3588  __TEXT,__const  protocol conformance descriptor for __C.CKPackage : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca3e10  __AUTH_CONST,__const  protocol witness table for __C.CKPackage : CloudKit.CKRecordValueProtocol in CloudKit
0x197db2e48  __TEXT,__text  (extension in CloudKit):__C.CKPackage.setBoundaryKey(Foundation.Data) throws -> ()
0x197db2dfc  __TEXT,__text  (extension in CloudKit):__C.CKPackage.add(__C.CKPackageItem) throws -> ()
0x197ec0d4c  __TEXT,__text  (extension in CloudKit):__C.CKPersona.init(identifier: Swift.String, type: __C.CKPersonaType) -> __C.CKPersona
0x197b8c454  __TEXT,__text  (extension in CloudKit):__C.CKPersona.init(identifier: Swift.String, type: __C.CKPersonaType) -> __C.CKPersona
0x197b848b8  __TEXT,__text  (extension in CloudKit):__C.CKPersona.identifier.getter : Swift.String
0x197efb20c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKPersona.identifier : Swift.String
0x197ec1eec  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.originator.getter : __C.CKPersona?
0x197efb20c  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKPersona.originator : __C.CKPersona?
0x197c34604  __TEXT,__text  (extension in CloudKit):__C.CKPersona.description.getter : Swift.String
0x197b8c624  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.isSupported.getter : Swift.Bool
0x197efb20c  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKPersona.isSupported : Swift.Bool
0x197b8e7e4  __TEXT,__text  (extension in CloudKit):__C.CKPersona.isEquivalent(to: __C.CKPersona) -> Swift.Bool
0x197ec1f90  __TEXT,__text  (extension in CloudKit):__C.CKPersona.isDataSeparated.getter : Swift.Bool?
0x197efb20c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKPersona.isDataSeparated : Swift.Bool?
0x197bb35c8  __TEXT,__text  (extension in CloudKit):__C.CKPersona.isLaunchPersona.getter : Swift.Bool
0x197efb20c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKPersona.isLaunchPersona : Swift.Bool
0x197b8cb9c  __TEXT,__text  (extension in CloudKit):__C.CKPersona.isCurrentPersona.getter : Swift.Bool
0x197efb20c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKPersona.isCurrentPersona : Swift.Bool
0x197bb30b4  __TEXT,__text  (extension in CloudKit):__C.CKPersona.__isDataSeparated.getter : __C.CKTernary
0x197efb20c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKPersona.__isDataSeparated : __C.CKTernary
0x197bb329c  __TEXT,__text  (extension in CloudKit):__C.CKPersona.redactedDescription.getter : Swift.String
0x197bb3348  __TEXT,__text  (extension in CloudKit):__C.CKPersona.ckDescribeProperties(using: __C.CKObjectDescription) -> ()
0x197ec1760  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.supportsSecureCoding.getter : Swift.Bool
0x197efb20c  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKPersona.supportsSecureCoding : Swift.Bool
0x197bcc844  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.__getProximatePersona(Swift.AutoreleasingUnsafeMutablePointer<__C.CKPersona?>?) throws -> ()
0x197ec1f18  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.__getOriginatorPersona(Swift.AutoreleasingUnsafeMutablePointer<__C.CKPersona?>?) throws -> ()
0x197ec0ddc  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.canUseArbitraryPersonas.getter : Swift.Bool
0x197efb20c  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKPersona.canUseArbitraryPersonas : Swift.Bool
0x197bbd52c  __TEXT,__text  (extension in CloudKit):__C.CKPersona.ckShortDescriptionRedact(Swift.Bool) -> Swift.String
0x197b8bbe0  __TEXT,__text  (extension in CloudKit):__C.CKPersona.copy(with: ObjectiveC.NSZone?) -> Any
0x197ec1078  __TEXT,__text  (extension in CloudKit):__C.CKPersona.hash.getter : Swift.Int
0x197b8553c  __TEXT,__text  (extension in CloudKit):__C.CKPersona.type.getter : __C.CKPersonaType
0x197efb20c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKPersona.type : __C.CKPersonaType
0x197baeb80  __TEXT,__text  (extension in CloudKit):__C.CKPersona.adopt() throws -> __C.NSObject
0x197ec195c  __TEXT,__text  (extension in CloudKit):__C.CKPersona.init(coder: __C.NSCoder) -> __C.CKPersona?
0x197ec199c  __TEXT,__text  (extension in CloudKit):__C.CKPersona.init(coder: __C.NSCoder) -> __C.CKPersona?
0x197ec1768  __TEXT,__text  (extension in CloudKit):__C.CKPersona.encode(with: __C.NSCoder) -> ()
0x197b8bf98  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.launch.getter : __C.CKPersona?
0x197efb20c  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKPersona.launch : __C.CKPersona?
0x197b8c5f0  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.current.getter : __C.CKPersona?
0x197efb20c  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKPersona.current : __C.CKPersona?
0x197b8ed7c  __TEXT,__text  (extension in CloudKit):__C.CKPersona.isEqual(Any?) -> Swift.Bool
0x197ba9dd0  __TEXT,__text  (extension in CloudKit):__C.CKPersona.perform((Swift.Error?) -> ()) -> ()
0x197bc4ee0  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.resolve(withIdentifier: Swift.String) throws -> __C.CKPersona
0x197ec200c  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.resolve(__C.UMUserPersona) -> __C.CKPersona?
0x197ec205c  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.resolve(__C.UMUserPersonaAttributes) -> __C.CKPersona?
0x197ec122c  __TEXT,__text  (extension in CloudKit):__C.CKPersona.restore(__C.NSObject) -> ()
0x197ec1148  __TEXT,__text  (extension in CloudKit):__C.CKPersona.canAdopt.getter : Swift.Bool
0x197efb20c  __TEXT,__const  property descriptor for (extension in CloudKit):__C.CKPersona.canAdopt : Swift.Bool
0x197bea448  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.personas(with: __C.CKPersonaType) throws -> [__C.CKPersona]
0x197ec0df4  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.personas() throws -> [__C.CKPersona]
0x197bcc7dc  __TEXT,__text  static (extension in CloudKit):__C.CKPersona.proximate.getter : __C.CKPersona?
0x197efb20c  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKPersona.proximate : __C.CKPersona?
0x197ec1f5c  __TEXT,__text  (extension in CloudKit):__C.CKPersona.init() -> __C.CKPersona
0x197ecc1e8  __TEXT,__text  (extension in CloudKit):__C.CKPersona.init() -> __C.CKPersona
0x197b8c368  __TEXT,__text  (extension in CloudKit):__C.CKPersona.init(CloudCoreInternal.PersonaID) -> __C.CKPersona
0x197b85804  __TEXT,__text  type metadata accessor for __C.CKPersona
0x197ec3ab8  __TEXT,__text  (extension in CloudKit):__C.CKTernary.init(Swift.Bool?) -> __C.CKTernary
0x197e1e5ac  __TEXT,__text  (extension in CloudKit):__C.CKVersion.description.getter : Swift.String
0x197e1e708  __TEXT,__text  static (extension in CloudKit):__C.CKVersion.supportsSecureCoding.getter : Swift.Bool
0x197ef4a78  __TEXT,__const  property descriptor for static (extension in CloudKit):__C.CKVersion.supportsSecureCoding : Swift.Bool
0x197e1e668  __TEXT,__text  (extension in CloudKit):__C.CKVersion.copy(with: ObjectiveC.NSZone?) -> Any
0x197e1e510  __TEXT,__text  (extension in CloudKit):__C.CKVersion.hash.getter : Swift.Int
0x197e1e8d0  __TEXT,__text  (extension in CloudKit):__C.CKVersion.init(coder: __C.NSCoder) -> __C.CKVersion?
0x197e1e910  __TEXT,__text  (extension in CloudKit):__C.CKVersion.init(coder: __C.NSCoder) -> __C.CKVersion?
0x197e1e710  __TEXT,__text  (extension in CloudKit):__C.CKVersion.encode(with: __C.NSCoder) -> ()
0x197e1e1c4  __TEXT,__text  (extension in CloudKit):__C.CKVersion.compare(__C.CKVersion) -> __C.NSComparisonResult
0x197e1e350  __TEXT,__text  (extension in CloudKit):__C.CKVersion.isEqual(Any?) -> Swift.Bool
0x197e1dfb4  __TEXT,__text  (extension in CloudKit):__C.CKVersion.init(pVersion: __C.CKDPVersion) -> __C.CKVersion
0x197e1dff4  __TEXT,__text  (extension in CloudKit):__C.CKVersion.init(pVersion: __C.CKDPVersion) -> __C.CKVersion
0x197e1df20  __TEXT,__text  (extension in CloudKit):__C.CKVersion.init() -> __C.CKVersion
0x197e1df44  __TEXT,__text  (extension in CloudKit):__C.CKVersion.init() -> __C.CKVersion
0x197e1ebe8  __TEXT,__text  type metadata accessor for __C.CKVersion
0x197ec4814  __TEXT,__text  (extension in CloudKit):Swift.Optional<A where A == Swift.Bool>.init(__C.CKTernary) -> Swift.Bool?
0x197ef32d8  __TEXT,__const  protocol conformance descriptor for Swift.UInt : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca3de8  __AUTH_CONST,__const  protocol witness table for Swift.UInt : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef32f8  __TEXT,__const  protocol conformance descriptor for Swift.Int8 : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca3d98  __AUTH_CONST,__const  protocol witness table for Swift.Int8 : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef3338  __TEXT,__const  protocol conformance descriptor for Swift.Int16 : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca3d70  __AUTH_CONST,__const  protocol witness table for Swift.Int16 : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef3378  __TEXT,__const  protocol conformance descriptor for Swift.Int32 : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca3d48  __AUTH_CONST,__const  protocol witness table for Swift.Int32 : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef33b8  __TEXT,__const  protocol conformance descriptor for Swift.Int64 : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca3d20  __AUTH_CONST,__const  protocol witness table for Swift.Int64 : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef3318  __TEXT,__const  protocol conformance descriptor for Swift.UInt8 : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca3cf8  __AUTH_CONST,__const  protocol witness table for Swift.UInt8 : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef3358  __TEXT,__const  protocol conformance descriptor for Swift.UInt16 : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca3cd0  __AUTH_CONST,__const  protocol witness table for Swift.UInt16 : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef3398  __TEXT,__const  protocol conformance descriptor for Swift.UInt32 : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca3ca8  __AUTH_CONST,__const  protocol witness table for Swift.UInt32 : CloudKit.CKRecordValueProtocol in CloudKit
0x197ef33d8  __TEXT,__const  protocol conformance descriptor for Swift.UInt64 : CloudKit.CKRecordValueProtocol in CloudKit
0x1e3ca3c80  __AUTH_CONST,__const  protocol witness table for Swift.UInt64 : CloudKit.CKRecordValueProtocol in CloudKit
0x1e0c41140  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidChangeConnectedStatusNotification
0x1e0c41138  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidChangeConnectedStatusNotificationConnectedUserInfoKey
0x1e0c41130  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidFailToSendOutgoingMessageNotification
0x1e0c41128  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidFailToSendOutgoingMessageNotificationErrorUserInfoKey
0x1e0c41120  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidFailToSendOutgoingMessageNotificationMessageUserInfoKey
0x1e0c41118  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidReceiveIncomingMessageNotification
0x1e0c41110  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidReceiveIncomingMessageNotificationMessageUserInfoKey
0x1e0c41108  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidReceiveMessageForTopicNotification
0x1e0c41100  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidReceiveMessageForTopicNotificationTopicUserInfoKey
0x1e0c410f8  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidReceiveMessageForTopicNotificationUserInfoUserInfoKey
0x1e0c410f0  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidReceivePublicTokenNotification
0x1e0c410e8  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidReceivePublicTokenNotificationPublicTokenUserInfoKey
0x1e0c410e0  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidReceiveTokenNotification
0x1e0c410d8  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidReceiveTokenNotificationIdentifierUserInfoKey
0x1e0c410d0  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidReceiveTokenNotificationTokenUserInfoKey
0x1e0c410c8  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidReceiveTokenNotificationTopicUserInfoKey
0x1e0c410c0  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidReconnectNotification
0x1e0c410b8  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidSendOutgoingMessageNotification
0x1e0c410b0  __DATA_CONST,__const  _CKAPSMachServiceConnectionDidSendOutgoingMessageNotificationMessageUserInfoKey
0x1e0c410a8  __DATA_CONST,__const  _CKAPSMachServiceConnectionNotificationEnvironmentNameUserInfoKey
0x1e0c410a0  __DATA_CONST,__const  _CKAPSMachServiceConnectionNotificationNamedDelegatePortUserInfoKey
0x1e0c41098  __DATA_CONST,__const  _CKAcceptSharesOperationDidAcceptShareNotification
0x197bc520c  __TEXT,__text  _CKAcceptablePredicateValueClasses
0x197bb5358  __TEXT,__text  _CKAcceptableValueClasses
0x1e0c41090  __DATA_CONST,__const  _CKAccountChangedNotification
0x197c285ec  __TEXT,__text  _CKAccountChangedNotificationName
0x197c81ad0  __TEXT,__text  _CKAddResponseHeaderValuesToUserInfoDictionary
0x1e0c41088  __DATA_CONST,__const  _CKAllTokensKey
0x197bb0120  __TEXT,__text  _CKAppIdentifierFromTeamAppTuple
0x197c37374  __TEXT,__text  _CKApplicationBundleIDForPush
0x1e0c41080  __DATA_CONST,__const  _CKAssetRepairContainerFormat
0x1e0c41078  __DATA_CONST,__const  _CKAssetRepairMissingAssetOrPackageRecordFieldHasRecovered
0x1e0c41070  __DATA_CONST,__const  _CKAssetRepairMissingAssetOrPackageRecordFieldRecoveredByDevice
0x1e0c41068  __DATA_CONST,__const  _CKAssetRepairMissingAssetOrPackageRecordFieldUnrecoverableDevices
0x1e0c41060  __DATA_CONST,__const  _CKAssetRepairMissingAssetRecordFieldAffectedRecordName
0x1e0c41058  __DATA_CONST,__const  _CKAssetRepairMissingAssetRecordFieldAffectedRecordType
0x1e0c41050  __DATA_CONST,__const  _CKAssetRepairMissingAssetRecordFieldFieldName
0x1e0c41048  __DATA_CONST,__const  _CKAssetRepairMissingAssetRecordFieldFileSignature
0x1e0c41040  __DATA_CONST,__const  _CKAssetRepairMissingAssetRecordFieldListIndex
0x1e0c41038  __DATA_CONST,__const  _CKAssetRepairMissingAssetRecordFieldReferenceSignature
0x1e0c41030  __DATA_CONST,__const  _CKAssetRepairMissingAssetRecordFieldZone
0x1e0c41028  __DATA_CONST,__const  _CKAssetRepairMissingAssetRecordType
0x1e0c41020  __DATA_CONST,__const  _CKAssetRepairMissingPackageRecordFieldAffectedRecordName
0x1e0c41018  __DATA_CONST,__const  _CKAssetRepairMissingPackageRecordFieldAffectedRecordType
0x1e0c41010  __DATA_CONST,__const  _CKAssetRepairMissingPackageRecordFieldFieldName
0x1e0c41008  __DATA_CONST,__const  _CKAssetRepairMissingPackageRecordFieldFileSignatures
0x1e0c41000  __DATA_CONST,__const  _CKAssetRepairMissingPackageRecordFieldReferenceSignatures
0x1e0c40ff8  __DATA_CONST,__const  _CKAssetRepairMissingPackageRecordFieldZone
0x1e0c40ff0  __DATA_CONST,__const  _CKAssetRepairMissingPackageRecordType
0x1e0c40fe8  __DATA_CONST,__const  _CKAssetRepairPushProxyFormat
0x1e0c40fe0  __DATA_CONST,__const  _CKAssetRepairZoneName
```
First 3,000 of 4,503.

