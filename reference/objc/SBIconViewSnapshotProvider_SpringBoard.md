# `SBIconViewSnapshotProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBIconViewSnapshotProviding`
- 2 instance variables, 5 properties, 3 instance methods, 0 class methods

## Instance variables

```
@? _invalidationBlock;
@"UIView" _snapshotView;
```

## Properties

```
@property (T@"UIView",R,N,V_snapshotView) snapshotView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIconViewSnapshotProvider snapshotView];
-[SBIconViewSnapshotProvider invalidate];
-[SBIconViewSnapshotProvider initWithSnapshotView:invalidation:];
```
