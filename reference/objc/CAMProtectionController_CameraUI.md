# `CAMProtectionController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 32 instance methods, 2 class methods

## Instance variables

```
i __nebulaDaemonWriteProtectionFileDescriptor;
@"NSObject<OS_dispatch_queue>" __protectionQueue;
@"NSCountedSet" __persistenceProtectionInflightRequestsByType;
@"NSMutableDictionary" __persistenceProtectionFileDescriptorsByType;
@"NSMutableDictionary" __burstProcessingProtectionFileDescriptorsByIdentifier;
@"NSMutableSet" __nebulaDaemonWriteProtectionInflightIdentifiers;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__protectionQueue) _protectionQueue;
@property (T@"NSCountedSet",R,N,V__persistenceProtectionInflightRequestsByType) _persistenceProtectionInflightRequestsByType;
@property (T@"NSMutableDictionary",R,N,V__persistenceProtectionFileDescriptorsByType) _persistenceProtectionFileDescriptorsByType;
@property (T@"NSMutableDictionary",R,N,V__burstProcessingProtectionFileDescriptorsByIdentifier) _burstProcessingProtectionFileDescriptorsByIdentifier;
@property (T@"NSMutableSet",R,N,V__nebulaDaemonWriteProtectionInflightIdentifiers) _nebulaDaemonWriteProtectionInflightIdentifiers;
@property (Ti,R,N,V__nebulaDaemonWriteProtectionFileDescriptor) _nebulaDaemonWriteProtectionFileDescriptor;
```

## Class methods

```
+[CAMProtectionController isCameraPerformingHighPriorityDiskActivity];
+[CAMProtectionController pathForProtectNebulaDaemonWritesIndicator];
```

## Instance methods

```
-[CAMProtectionController stopProtectingPersistenceForRequest:];
-[CAMProtectionController _nebulaDaemonWriteProtectionFileDescriptor];
-[CAMProtectionController _persistenceProtectionTypeForRequest:];
-[CAMProtectionController _protectionQueueStopProtectingPersistenceForType:logIdentifier:];
-[CAMProtectionController _protectionQueueAbortProtectionForBurstProcessing];
-[CAMProtectionController _protectionQueueStartProtectingNebulaDaemonWritesForIdentifier:];
-[CAMProtectionController _burstProcessingProtectionFileDescriptorsByIdentifier];
-[CAMProtectionController init];
-[CAMProtectionController _allowSuspensionWhileFileLockedForPath:];
-[CAMProtectionController _persistenceProtectionFileDescriptorsByType];
-[CAMProtectionController _protectionQueueAbortProtectionForProtectionTypes];
-[CAMProtectionController dealloc];
-[CAMProtectionController _persistenceProtectionFileDescriptorForType:];
-[CAMProtectionController startProtectingNebulaDaemonWritesForIdentifier:];
-[CAMProtectionController _addBurstProcessingProtectionIndicatorForIdentifier:];
-[CAMProtectionController startProtectingBurstProcessingForIdentifier:];
-[CAMProtectionController _burstProcessingProtectionFileDescriptorForIdentifier:];
-[CAMProtectionController _persistenceProtectionInflightRequestsByType];
-[CAMProtectionController _protectionQueue];
-[CAMProtectionController startProtectingPersistenceForRequest:];
-[CAMProtectionController _protectionQueueRemoveBurstProcessingProtectionIndicatorForIdentifier:];
-[CAMProtectionController _protectionQueueStartProtectingPersistenceForType:logIdentifier:];
-[CAMProtectionController abortOutstandingNebulaDaemonWriteProtectionsForReason:];
-[CAMProtectionController _protectionQueueStopProtectingNebulaDaemonWritesForIdentifier:closeFile:];
-[CAMProtectionController stopProtectingNebulaDaemonWritesForIdentifier:];
-[CAMProtectionController _nebulaDaemonWriteProtectionInflightIdentifiers];
-[CAMProtectionController _burstProcessingProtectionPathForIdentifier:];
-[CAMProtectionController _protectionQueueRemovePersistenceProtectionIndicatorForType:unlinkFile:logIdentifier:];
-[CAMProtectionController _persistenceProtectionPathForType:];
-[CAMProtectionController stopProtectingBurstProcessingForIdentifier:];
-[CAMProtectionController _protectionQueueAbortProtectionForNebulaDaemonWritesForReason:];
-[CAMProtectionController _addPersistenceProtectionIndicatorForType:logIdentifier:];
```
