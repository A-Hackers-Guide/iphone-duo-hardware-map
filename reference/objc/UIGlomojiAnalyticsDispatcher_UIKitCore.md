# `UIGlomojiAnalyticsDispatcher`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _KBMenuAppeared;
Q _glomojiType;
Q _KBMenuInteractionSource;
Q _KBMenuDismissSource;
@"NSString" _originalInputMode;
@"NSString" _updatedInputMode;
Q _KBMenuSelectedAction;
```

## Properties

```
@property (TQ,N,V_glomojiType) glomojiType;
@property (TB,N,V_KBMenuAppeared) KBMenuAppeared;
@property (TQ,N,V_KBMenuInteractionSource) KBMenuInteractionSource;
@property (TQ,N,V_KBMenuDismissSource) KBMenuDismissSource;
@property (T@"NSString",C,N,V_originalInputMode) originalInputMode;
@property (T@"NSString",C,N,V_updatedInputMode) updatedInputMode;
@property (TQ,N,V_KBMenuSelectedAction) KBMenuSelectedAction;
```

## Instance methods

```
-[UIGlomojiAnalyticsDispatcher init];
-[UIGlomojiAnalyticsDispatcher setUpdatedInputMode:];
-[UIGlomojiAnalyticsDispatcher updatedInputMode];
-[UIGlomojiAnalyticsDispatcher KBMenuAppeared];
-[UIGlomojiAnalyticsDispatcher KBMenuInteractionSource];
-[UIGlomojiAnalyticsDispatcher didKBMenuAppear];
-[UIGlomojiAnalyticsDispatcher setGlomojiType:];
-[UIGlomojiAnalyticsDispatcher KBMenuDismissSource];
-[UIGlomojiAnalyticsDispatcher KBMenuSelectedAction];
-[UIGlomojiAnalyticsDispatcher didKBMenuAction];
-[UIGlomojiAnalyticsDispatcher didGlomojiTap];
-[UIGlomojiAnalyticsDispatcher didKBMenuDismiss];
-[UIGlomojiAnalyticsDispatcher didKBMenuInteraction];
-[UIGlomojiAnalyticsDispatcher getGlomojiButtonTypeEnumValue];
-[UIGlomojiAnalyticsDispatcher getInputMode];
-[UIGlomojiAnalyticsDispatcher glomojiType];
-[UIGlomojiAnalyticsDispatcher originalInputMode];
-[UIGlomojiAnalyticsDispatcher setKBMenuAppeared:];
-[UIGlomojiAnalyticsDispatcher setKBMenuDismissSource:];
-[UIGlomojiAnalyticsDispatcher setKBMenuInteractionSource:];
-[UIGlomojiAnalyticsDispatcher setKBMenuSelectedAction:];
-[UIGlomojiAnalyticsDispatcher setOriginalInputMode:];
```
