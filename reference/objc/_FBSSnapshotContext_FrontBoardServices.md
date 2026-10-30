# `_FBSSnapshotContext`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"FBSDisplayConfiguration" _displayConfiguration;
@"NSOrderedSet" _layers;
B _opaque;
d _scale;
{CGSize="width"d"height"d} _snapshotSize;
B _allowsProtectedContent;
B _alternateLayout;
```

## Properties

```
@property (T@"FBSDisplayConfiguration",R,N,V_displayConfiguration) displayConfiguration;
@property (T@"NSOrderedSet",R,N,V_layers) layers;
@property (TB,N,GisOpaque,V_opaque) opaque;
@property (Td,N,V_scale) scale;
@property (T{CGSize=dd},N,V_snapshotSize) snapshotSize;
@property (TB,N,V_allowsProtectedContent) allowsProtectedContent;
@property (TB,N,V_alternateLayout) alternateLayout;
```

## Instance methods

```
-[_FBSSnapshotContext initWithDisplayConfiguration:layer:];
-[_FBSSnapshotContext layers];
-[_FBSSnapshotContext displayConfiguration];
-[_FBSSnapshotContext setOpaque:];
-[_FBSSnapshotContext isOpaque];
-[_FBSSnapshotContext setScale:];
-[_FBSSnapshotContext snapshotSize];
-[_FBSSnapshotContext setAllowsProtectedContent:];
-[_FBSSnapshotContext scale];
-[_FBSSnapshotContext setSnapshotSize:];
-[_FBSSnapshotContext setAlternateLayout:];
-[_FBSSnapshotContext initWithDisplayConfiguration:layers:];
-[_FBSSnapshotContext copyWithZone:];
-[_FBSSnapshotContext allowsProtectedContent];
-[_FBSSnapshotContext alternateLayout];
```
