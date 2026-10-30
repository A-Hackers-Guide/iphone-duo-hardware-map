# `_UIKeyboardShortcutInvocation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIMenuElement<_UIMenuLeaf>" _keyboardShortcutLeaf;
@"UIMenuElement<_UIMenuLeaf>" _validatedKeyboardShortcutLeaf;
@"UIPhysicalKeyboardEvent" _triggeringEvent;
@"UIResponder" _originatingResponder;
@ _target;
```

## Properties

```
@property (T@"UIMenuElement<_UIMenuLeaf>",R,N,V_keyboardShortcutLeaf) keyboardShortcutLeaf;
@property (T@"UIMenuElement<_UIMenuLeaf>",R,N,V_validatedKeyboardShortcutLeaf) validatedKeyboardShortcutLeaf;
@property (T@"UIPhysicalKeyboardEvent",R,N,V_triggeringEvent) triggeringEvent;
@property (T@"UIResponder",R,W,N,V_originatingResponder) originatingResponder;
@property (TB,R,N,GisRepeatable) repeatable;
@property (T@,R,W,N,V_target) target;
@property (T@"UIMenuElement<_UIMenuLeaf>",R,N) keyboardShortcutLeafToInvoke;
```

## Instance methods

```
-[_UIKeyboardShortcutInvocation keyboardShortcutLeaf];
-[_UIKeyboardShortcutInvocation originatingResponder];
-[_UIKeyboardShortcutInvocation target];
-[_UIKeyboardShortcutInvocation isRepeatable];
-[_UIKeyboardShortcutInvocation triggeringEvent];
-[_UIKeyboardShortcutInvocation canInvokeKeyboardShortcut];
-[_UIKeyboardShortcutInvocation initWithKeyboardShortcutLeaf:validatedKeyboardShortcutLeaf:triggeringEvent:originatingResponder:target:];
-[_UIKeyboardShortcutInvocation keyboardShortcutLeafToInvoke];
-[_UIKeyboardShortcutInvocation performKeyDownAction];
-[_UIKeyboardShortcutInvocation performKeyUpAction];
-[_UIKeyboardShortcutInvocation validatedKeyboardShortcutLeaf];
```
