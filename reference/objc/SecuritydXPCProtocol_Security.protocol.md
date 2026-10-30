# `SecuritydXPCProtocol` (protocol)

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance methods

```
-[SecuritydXPCProtocol SecItemAddAndNotifyOnSync:syncCallback:complete:];
-[SecuritydXPCProtocol secAssociateIndirectUnlockKey:handle:completion:];
-[SecuritydXPCProtocol secItemDeleteForAppClipApplicationIdentifier:completion:];
-[SecuritydXPCProtocol secItemDigest:accessGroup:complete:];
-[SecuritydXPCProtocol secItemFetchCurrentItemAcrossAllDevices:identifier:viewHint:fetchCloudValue:complete:];
-[SecuritydXPCProtocol secItemFetchCurrentItemOutOfBand:forceFetch:complete:];
-[SecuritydXPCProtocol secItemFetchPCSIdentityByKeyOutOfBand:forceFetch:complete:];
-[SecuritydXPCProtocol secItemPersistKeychainWritesAtHighPerformanceCost:];
-[SecuritydXPCProtocol secItemPromoteItemsForAppClip:toParentApp:completion:];
-[SecuritydXPCProtocol secItemSetCurrentItemAcrossAllDevices:newCurrentItemHash:accessGroup:identifier:viewHint:oldCurrentItemReference:oldCurrentItemHash:complete:];
-[SecuritydXPCProtocol secItemUnsetCurrentItemsAcrossAllDevices:identifiers:viewHint:complete:];
-[SecuritydXPCProtocol secKeychainCopyDatabasePath:];
-[SecuritydXPCProtocol secKeychainDeleteMultiuser:complete:];
-[SecuritydXPCProtocol secKeychainForceUpgradeIfNeeded:];
-[SecuritydXPCProtocol secLookupIndirectUnlockKey:completion:];
```
