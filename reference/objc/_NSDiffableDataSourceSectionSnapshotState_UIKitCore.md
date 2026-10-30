# `_NSDiffableDataSourceSectionSnapshotState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"_UITreeDataSourceSnapshotter" _snapshotter;
@"NSOrderedSet" _guaranteedPerformanceIdentifiers;
Q _identifierLookupCount;
@"NSOrderedSet" _identifiers;
```

## Properties

```
@property (T@"<_UITreeDataSourceSnapshotter>",R,N) snapshotter;
@property (T@"NSOrderedSet",R,N,V_identifiers) identifiers;
```

## Instance methods

```
-[_NSDiffableDataSourceSectionSnapshotState identifiers];
-[_NSDiffableDataSourceSectionSnapshotState init];
-[_NSDiffableDataSourceSectionSnapshotState willBecomeWiredToDataSource];
-[_NSDiffableDataSourceSectionSnapshotState description];
-[_NSDiffableDataSourceSectionSnapshotState copyWithZone:];
-[_NSDiffableDataSourceSectionSnapshotState isEqual:];
-[_NSDiffableDataSourceSectionSnapshotState snapshotter];
-[_NSDiffableDataSourceSectionSnapshotState containsIdentifier:];
-[_NSDiffableDataSourceSectionSnapshotState indexOfIdentifier:];
-[_NSDiffableDataSourceSectionSnapshotState initWithSnapshotter:identifiers:];
-[_NSDiffableDataSourceSectionSnapshotState initWithSnapshotter:identifiers:identifiersHaveGuaranteedPerformance:];
-[_NSDiffableDataSourceSectionSnapshotState snapshotterMutableCopy];
```
