# `SBAppsRegionModel`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSFastEnumeration`
- 4 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
Q _hash;
@"SBAppLayout" _appLayoutRepresentation;
@"SBAppLayout" _leadingAppLayout;
@"SBAppLayout" _trailingAppLayout;
```

## Properties

```
@property (T@"SBAppLayout",R,N) currentLeftAppLayout;
@property (T@"SBAppLayout",R,N) currentRightAppLayout;
@property (T@"SBAppLayout",R,N) currentAppLayout;
```

## Class methods

```
+[SBAppsRegionModel emptyAppsRegion];
```

## Instance methods

```
-[SBAppsRegionModel debugDescription];
-[SBAppsRegionModel currentAppLayout];
-[SBAppsRegionModel succinctDescription];
-[SBAppsRegionModel countByEnumeratingWithState:objects:count:];
-[SBAppsRegionModel hash];
-[SBAppsRegionModel description];
-[SBAppsRegionModel appendDescriptionToStream:];
-[SBAppsRegionModel copyWithZone:];
-[SBAppsRegionModel isEqual:];
-[SBAppsRegionModel currentLeftAppLayout];
-[SBAppsRegionModel currentRightAppLayout];
-[SBAppsRegionModel initWithCurrentLeftAppLayout:currentRightAppLayout:];
```
