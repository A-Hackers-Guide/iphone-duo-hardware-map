# `SBSystemStatusStatusBarOverridesArchiver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"STStatusBarOverridesStatusDomain" _overridesDomain;
@"STStatusBarOverridesStatusDomainPublisher" _overridesPublisher;
@"NSObject<OS_dispatch_queue>" _queue;
@"_SBSystemStatusStatusBarOverridesArchiveRecord" _queue_archiveRecord;
```

## Class methods

```
+[SBSystemStatusStatusBarOverridesArchiver _archiveFileURL];
```

## Instance methods

```
-[SBSystemStatusStatusBarOverridesArchiver init];
-[SBSystemStatusStatusBarOverridesArchiver dealloc];
-[SBSystemStatusStatusBarOverridesArchiver _queue_persistUpdatedArchiveRecord:];
-[SBSystemStatusStatusBarOverridesArchiver _queue_readStatusBarOverridesArchiveRecord];
-[SBSystemStatusStatusBarOverridesArchiver _queue_setupObservingAndReconcileInitialState];
-[SBSystemStatusStatusBarOverridesArchiver _queue_writeOutArchiveRecord:];
```
