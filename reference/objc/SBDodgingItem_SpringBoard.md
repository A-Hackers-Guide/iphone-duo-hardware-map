# `SBDodgingItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 9 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"SBDodgingResolverViewController" _dodgingResolverViewController;
@"NSString" _uniqueIdentifier;
@"<UICoordinateSpace>" _containerCoordinateSpace;
@"NSArray" _otherDodgingIdentifiers;
@"<SBDodgingItemDelegate>" _delegate;
@"UIView" _view;
@"SBDodgingItemPreference" _preference;
{CGPoint="x"d"y"d} _center;
{CGSize="width"d"height"d} _size;
{CGSize="width"d"height"d} _containerSize;
```

## Properties

```
@property (T@"<SBDodgingItemDelegate>",R,W,N,V_delegate) delegate;
@property (T@"UIView",R,N,V_view) view;
@property (T{CGPoint=dd},N,V_center) center;
@property (T{CGSize=dd},N,V_size) size;
@property (T{CGSize=dd},N,V_containerSize) containerSize;
@property (T@"<UICoordinateSpace>",&,N,V_containerCoordinateSpace) containerCoordinateSpace;
@property (T@"NSArray",&,N,V_otherDodgingIdentifiers) otherDodgingIdentifiers;
@property (T@"SBDodgingItemPreference",&,N,V_preference) preference;
@property (T@"NSString",R,C,N,V_uniqueIdentifier) uniqueIdentifier;
```

## Instance methods

```
-[SBDodgingItem containerSize];
-[SBDodgingItem setContainerSize:];
-[SBDodgingItem setCenter:];
-[SBDodgingItem uniqueIdentifier];
-[SBDodgingItem preference];
-[SBDodgingItem size];
-[SBDodgingItem invalidate];
-[SBDodgingItem view];
-[SBDodgingItem center];
-[SBDodgingItem delegate];
-[SBDodgingItem hash];
-[SBDodgingItem description];
-[SBDodgingItem copyWithZone:];
-[SBDodgingItem isEqual:];
-[SBDodgingItem setSize:];
-[SBDodgingItem containerCoordinateSpace];
-[SBDodgingItem setContainerCoordinateSpace:];
-[SBDodgingItem setPreference:];
-[SBDodgingItem initWithUniqueIdentifier:view:delegate:dodgingResolverViewController:];
-[SBDodgingItem otherDodgingIdentifiers];
-[SBDodgingItem setNeedsUpdateAnimated:];
-[SBDodgingItem setOtherDodgingIdentifiers:];
```
