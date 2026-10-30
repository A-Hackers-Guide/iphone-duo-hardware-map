# `SBIconVisibilityService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"SBIconModel" _iconModel;
@"NSLock" _iconStateDisplayIdentifiersLock;
@"NSSet" _iconStateDisplayIdentifiers;
```

## Instance methods

```
-[SBIconVisibilityService dealloc];
-[SBIconVisibilityService initWithIconModel:];
-[SBIconVisibilityService _visibleIdentifiersChanged:];
-[SBIconVisibilityService iconStateDisplayIdentifiers];
```
