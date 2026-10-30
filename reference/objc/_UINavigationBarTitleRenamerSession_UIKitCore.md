# `_UINavigationBarTitleRenamerSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"UIView<_UINavigationBarTitleRenamerContentView>" _renamerContentView;
@"_UINavigationBarTitleRenamer" _attachedRenamer;
@"NSString" _title;
@"LPLinkMetadata" _iconMetadata;
@ _context;
@"NSUUID" _sessionIdentifier;
```

## Properties

```
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSUUID",R,N,V_sessionIdentifier) sessionIdentifier;
@property (T@"_UINavigationBarTitleRenamer",R,W,N,V_attachedRenamer) attachedRenamer;
@property (T@"LPLinkMetadata",R,N,V_iconMetadata) iconMetadata;
@property (T@,W,N,V_context) context;
@property (T@"UIView<_UINavigationBarTitleRenamerContentView>",R,N,V_renamerContentView) renamerContentView;
```

## Class methods

```
+[_UINavigationBarTitleRenamerSession supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UINavigationBarTitleRenamerSession sessionDidEnd];
-[_UINavigationBarTitleRenamerSession sessionIdentifier];
-[_UINavigationBarTitleRenamerSession iconMetadata];
-[_UINavigationBarTitleRenamerSession setContext:];
-[_UINavigationBarTitleRenamerSession title];
-[_UINavigationBarTitleRenamerSession setTitle:];
-[_UINavigationBarTitleRenamerSession encodeWithBSXPCCoder:];
-[_UINavigationBarTitleRenamerSession initWithBSXPCCoder:];
-[_UINavigationBarTitleRenamerSession context];
-[_UINavigationBarTitleRenamerSession attachedRenamer];
-[_UINavigationBarTitleRenamerSession _sanitizedTitleForText:];
-[_UINavigationBarTitleRenamerSession _textFieldDidEndEditingWithText:];
-[_UINavigationBarTitleRenamerSession _textFieldShouldEndEditingWithText:];
-[_UINavigationBarTitleRenamerSession _willBeginRenamingWithText:selectedRange:];
-[_UINavigationBarTitleRenamerSession cancelSession];
-[_UINavigationBarTitleRenamerSession createRenamerContentView];
-[_UINavigationBarTitleRenamerSession existingRenamerContentView];
-[_UINavigationBarTitleRenamerSession initWithSuggestedTitle:];
-[_UINavigationBarTitleRenamerSession initWithSuggestedTitle:iconMetadata:];
-[_UINavigationBarTitleRenamerSession renamerContentView];
-[_UINavigationBarTitleRenamerSession sessionDidStartInRenamer:];
```
