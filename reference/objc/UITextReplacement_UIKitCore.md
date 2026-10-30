# `UITextReplacement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"UITextRange" _range;
@"NSString" _originalText;
@"NSString" _replacementText;
@"NSString" _menuTitle;
B _isDictationCommandReplacement;
I _usageTrackingMask;
@? _replacementCompletionBlock;
```

## Properties

```
@property (T@"UITextRange",R,N,V_range) range;
@property (T@"NSString",R,N,V_originalText) originalText;
@property (T@"NSString",R,N,V_replacementText) replacementText;
@property (T@"NSString",R,N,V_menuTitle) menuTitle;
@property (TB,R,V_isDictationCommandReplacement) isDictationCommandReplacement;
@property (T@?,C,N,V_replacementCompletionBlock) replacementCompletionBlock;
@property (TI,N,V_usageTrackingMask) usageTrackingMask;
```

## Class methods

```
+[UITextReplacement replacementWithRange:original:replacement:menuTitle:];
+[UITextReplacement replacementWithRange:original:replacement:menuTitle:isDictationCommandReplacement:];
```

## Instance methods

```
-[UITextReplacement usageTrackingMask];
-[UITextReplacement range];
-[UITextReplacement setUsageTrackingMask:];
-[UITextReplacement replacementText];
-[UITextReplacement _isNoReplacementsFoundItem];
-[UITextReplacement didReplaceTextWithTarget:];
-[UITextReplacement isDictationCommandReplacement];
-[UITextReplacement menuTitle];
-[UITextReplacement originalText];
-[UITextReplacement replacementCompletionBlock];
-[UITextReplacement setReplacementCompletionBlock:];
```
