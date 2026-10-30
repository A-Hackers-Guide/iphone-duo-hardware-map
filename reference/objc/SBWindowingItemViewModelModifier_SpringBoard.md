# `SBWindowingItemViewModelModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- Protocols: `SBWindowingItemViewModel`
- 1 instance variables, 14 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"<SBWindowingItem>" _item;
```

## Properties

```
@property (T@"<SBWindowingItem>",R,N,V_item) item;
@property (T{SBWindowingItemFrame={CGRect={CGPoint=dd}{CGSize=dd}}{CGPoint=dd}{CGPoint=dd}{CGPoint=dd}{CGPoint=dd}},R,N) frame;
@property (T{SBWindowingItemCorners={UIRectCornerRadii=dddd}Q},R,N) corners;
@property (T{SBWindowingItemShadow=dq},R,N) shadow;
@property (T{SBWindowingItemTitleStyle=qdddqQ},R,N) titleStyle;
@property (T{SBWindowingItemBorder=ddddd{CAColorMatrix=ffffffffffffffffffff}},R,N) border;
@property (Td,R,N) opacity;
@property (T{SBSwitcherWallpaperGradientAttributes=dd},R,N) wallpaperGradientAttributes;
@property (T{CGPoint=dd},R,N) perspectiveAngle;
@property (Td,R,N) dimmingAlpha;
@property (T@"SBSwitcherAnimationAttributes",R,N) animationAttributes;
@property (TB,R,N) supportsHomeAffordance;
@property (T@"SBWindowingItemViewModel",R,N) spaceAccessoryViewModel;
@property (TQ,R,N) personalityDebugColorStyle;
```

## Instance methods

```
-[SBWindowingItemViewModelModifier wallpaperGradientAttributes];
-[SBWindowingItemViewModelModifier shadow];
-[SBWindowingItemViewModelModifier opacity];
-[SBWindowingItemViewModelModifier item];
-[SBWindowingItemViewModelModifier initWithItem:];
-[SBWindowingItemViewModelModifier border];
-[SBWindowingItemViewModelModifier dimmingAlpha];
-[SBWindowingItemViewModelModifier corners];
-[SBWindowingItemViewModelModifier mutableCopy];
-[SBWindowingItemViewModelModifier frame];
-[SBWindowingItemViewModelModifier titleStyle];
-[SBWindowingItemViewModelModifier perspectiveAngle];
-[SBWindowingItemViewModelModifier animationAttributes];
-[SBWindowingItemViewModelModifier personalityDebugColorStyle];
-[SBWindowingItemViewModelModifier spaceAccessoryViewModel];
-[SBWindowingItemViewModelModifier supportsHomeAffordance];
```
