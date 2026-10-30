# `_UIMenuLeaf` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UIMenuLeaf`
- 0 instance variables, 12 properties, 23 instance methods, 0 class methods

## Properties

```
@property (T@"NSAttributedString",C,N) attributedTitle;
@property (TB,R,N) keepsMenuPresented;
@property (T@"_UITextStyleDescriptor",C,N) _titleStyleDescriptor;
@property (T@"UISPasteVariant",R,N) _pasteVariant;
@property (T@"<UISSecureVariant>",R,N) _secureVariant;
@property (T@"NSArray",C,N,S_setLeafAlternates:) _leafAlternates;
@property (T@"_UIMenuLeafKeyboardShortcut",R,N) _keyboardShortcut;
@property (Tq,N,S_setEnumerationPriority:) _enumerationPriority;
@property (T@"BKSHIDEventDeferringEnvironment",R,N) _eventDeferringEnvironment;
@property (TB,N,S_setAllowsGlobeKeyModifier:) _allowsGlobeKeyModifier;
@property (TB,R,N) _isIntelligentAssistantAction;
@property (T@"<UIPopoverPresentationControllerSourceItem>",?,W,N,S_setOverridePresentationSourceItem:) _overridePresentationSourceItem;
```

## Instance methods

```
-[_UIMenuLeaf setAttributedTitle:];
-[_UIMenuLeaf _isIntelligentAssistantAction];
-[_UIMenuLeaf keepsMenuPresented];
-[_UIMenuLeaf attributedTitle];
-[_UIMenuLeaf _leafAlternates];
-[_UIMenuLeaf _allowsGlobeKeyModifier];
-[_UIMenuLeaf _enumerationPriority];
-[_UIMenuLeaf _eventDeferringEnvironment];
-[_UIMenuLeaf _isDefaultCommand];
-[_UIMenuLeaf _keyboardShortcut];
-[_UIMenuLeaf _menuLeafWithKeyboardShortcut:];
-[_UIMenuLeaf _pasteVariant];
-[_UIMenuLeaf _resolvedTargetFromFirstTarget:sender:];
-[_UIMenuLeaf _secureVariant];
-[_UIMenuLeaf _setAllowsGlobeKeyModifier:];
-[_UIMenuLeaf _setEnumerationPriority:];
-[_UIMenuLeaf _setLeafAlternates:];
-[_UIMenuLeaf _titleStyleDescriptor];
-[_UIMenuLeaf _validatedLeafWithTarget:validator:];
-[_UIMenuLeaf _wantsPriorityOverSystemBehavior:];
-[_UIMenuLeaf set_titleStyleDescriptor:];
-[_UIMenuLeaf _overridePresentationSourceItem];
-[_UIMenuLeaf _setOverridePresentationSourceItem:];
```
