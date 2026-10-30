# `UIAccessibilityHUDPositionManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSMapTable" _managedHUDs;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _keyboardAvoidanceArea;
```

## Class methods

```
+[UIAccessibilityHUDPositionManager sharedInstance];
```

## Instance methods

```
-[UIAccessibilityHUDPositionManager init];
-[UIAccessibilityHUDPositionManager dealloc];
-[UIAccessibilityHUDPositionManager adjustViewPropertiesForHUD:withReferenceView:];
-[UIAccessibilityHUDPositionManager adjustViewPropertiesForHUD:withReferenceView:keyboardFrame:];
-[UIAccessibilityHUDPositionManager beginManagingPositionOfHUD:withReferenceView:];
-[UIAccessibilityHUDPositionManager keyboardFrameDidChange:];
-[UIAccessibilityHUDPositionManager stopManagingPositionOfHUD:];
-[UIAccessibilityHUDPositionManager updateFramesForManagedHUDsUsingKeyboardFrame:];
```
