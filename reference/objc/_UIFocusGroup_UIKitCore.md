# `_UIFocusGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 9 properties, 27 instance methods, 1 class methods

## Instance variables

```
{?="itemOrderValid"b1"childGroupOrderValid"b1"primaryItemValid"b1"primaryRectValid"b1} _flags;
@"NSMutableArray" _childGroups;
@"NSMutableArray" _items;
@"<UIFocusItem>" _primaryItem;
@"NSString" _identifier;
@"_UIFocusGroup" _parentGroup;
@"<UICoordinateSpace>" _coordinateSpace;
@"<UIFocusEnvironment>" _owningEnvironment;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _primaryRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundingBox;
```

## Properties

```
@property (T@"<UIFocusEnvironment>",R,N,V_owningEnvironment) owningEnvironment;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_primaryRect) primaryRect;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"_UIFocusGroup",R,W,N,V_parentGroup) parentGroup;
@property (T@"NSArray",R,N) childGroups;
@property (T@"<UIFocusItem>",R,N,V_primaryItem) primaryItem;
@property (T@"NSArray",R,N) items;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_boundingBox) boundingBox;
@property (T@"<UICoordinateSpace>",R,N,V_coordinateSpace) coordinateSpace;
```

## Class methods

```
+[_UIFocusGroup nullGroupWithCoordinateSpace:];
```

## Instance methods

```
-[_UIFocusGroup parentGroup];
-[_UIFocusGroup coordinateSpace];
-[_UIFocusGroup debugDescription];
-[_UIFocusGroup identifier];
-[_UIFocusGroup items];
-[_UIFocusGroup boundingBox];
-[_UIFocusGroup hash];
-[_UIFocusGroup description];
-[_UIFocusGroup isEqual:];
-[_UIFocusGroup _validatePrimaryItemIfNecessary];
-[_UIFocusGroup _deepCopyWithNewIdentifierToGroupMap:];
-[_UIFocusGroup _insertChildGroup:];
-[_UIFocusGroup _insertItem:];
-[_UIFocusGroup _invalidateChildGroupOrder];
-[_UIFocusGroup _invalidateItemOrder];
-[_UIFocusGroup _invalidatePrimaryItem];
-[_UIFocusGroup _invalidatePrimaryRect];
-[_UIFocusGroup _updateWithEnvironment:];
-[_UIFocusGroup _validateChildGroupOrderIfNecessary];
-[_UIFocusGroup _validateItemOrderIfNecessary];
-[_UIFocusGroup _validatePrimaryRectIfNeccessary];
-[_UIFocusGroup childGroups];
-[_UIFocusGroup initWithIdentifier:parentGroup:coordinateSpace:];
-[_UIFocusGroup isEqualToFocusGroup:];
-[_UIFocusGroup owningEnvironment];
-[_UIFocusGroup primaryItem];
-[_UIFocusGroup primaryRect];
```
