# `SBWindowingLayoutFormatAdapter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _containerViewBounds;
@"SBSwitcherWindowingConfiguration" _windowingConfiguration;
q _lastInteractionTime;
d _xPositionOffset;
@"SBSwitcherWindowManagementContext" _windowManagementContext;
@"NSArray" _layoutRequests;
@"NSDictionary" _layoutRoleToLayoutAttributes;
@"SBUnlockedEnvironmentState" _unlockedEnvironmentState;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_layoutRequests) layoutRequests;
@property (T@"NSDictionary",R,C,N,V_layoutRoleToLayoutAttributes) layoutRoleToLayoutAttributes;
@property (T@"SBUnlockedEnvironmentState",R,C,N,V_unlockedEnvironmentState) unlockedEnvironmentState;
```

## Instance methods

```
-[SBWindowingLayoutFormatAdapter unlockedEnvironmentState];
-[SBWindowingLayoutFormatAdapter initWithWindowScene:];
-[SBWindowingLayoutFormatAdapter _createLayoutRoleToLayoutAttributesMap];
-[SBWindowingLayoutFormatAdapter _modifySizeAndPositionForLayoutAttributes:forLayoutRequest:];
-[SBWindowingLayoutFormatAdapter layoutRequests];
-[SBWindowingLayoutFormatAdapter layoutRoleToLayoutAttributes];
-[SBWindowingLayoutFormatAdapter parse:argumentType:bundleIdentifiers:error:];
```
