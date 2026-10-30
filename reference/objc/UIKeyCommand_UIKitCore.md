# `UIKeyCommand`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICommand`
- 9 instance variables, 25 properties, 58 instance methods, 15 class methods

## Instance variables

```
: _upAction;
@"BKSHIDEventDeferringEnvironment" _eventDeferringEnvironment;
q _enumerationPriority;
b32 _buttonType;
b1 _isPlaceholder;
b1 _handleAfterKeyEvent;
@"_UIMenuLeafKeyboardShortcut" _keyboardShortcut;
B _allowsGlobeKeyModifier;
B _wantsPriorityOverSystemBehavior;
```

## Properties

```
@property (T@"NSString",R,N) _layoutAwareInput;
@property (Tq,R,N) _layoutAwareModifierFlags;
@property (T@"NSIndexSet",R,N) _layoutAwareKeyCodes;
@property (T@"NSString",R,N) discoverabilityInput;
@property (T:,R,N) upAction;
@property (TB,R,N) repeatable;
@property (TB,R,N) isPlaceholder;
@property (T@"NSIndexSet",R,N) _keyCodes;
@property (Tq,R,N) _buttonType;
@property (TB,R,N) _handleAfterKeyEvent;
@property (T@"BKSHIDEventDeferringEnvironment",&,N,S_setEventDeferringEnvironment:) _eventDeferringEnvironment;
@property (T@"NSString",R,N) _layoutAwareDisplayInputOverride;
@property (T@"NSString",C,D,N) title;
@property (T@"UIImage",C,D,N) image;
@property (T@"NSString",C,D,N) discoverabilityTitle;
@property (T:,R,D,N) action;
@property (T@"NSString",R,N) input;
@property (Tq,R,N) modifierFlags;
@property (T@,R,D,N) propertyList;
@property (TQ,D,N) attributes;
@property (Tq,D,N) state;
@property (T@"NSArray",R,D,N) alternates;
@property (TB,N) wantsPriorityOverSystemBehavior;
@property (TB,N) allowsAutomaticLocalization;
@property (TB,N) allowsAutomaticMirroring;
```

## Class methods

```
+[UIKeyCommand supportsSecureCoding];
+[UIKeyCommand commandWithTitle:image:action:input:modifierFlags:propertyList:];
+[UIKeyCommand commandWithTitle:image:action:input:modifierFlags:propertyList:alternates:];
+[UIKeyCommand commandWithTitle:imageName:action:input:modifierFlags:];
+[UIKeyCommand commandWithTitle:imageName:action:input:modifierFlags:propertyList:leafOrCommandAlternates:];
+[UIKeyCommand keyCommandWithCompactInput:action:upAction:];
+[UIKeyCommand keyCommandWithInput:modifierFlags:action:];
+[UIKeyCommand keyCommandWithInput:modifierFlags:action:discoverabilityTitle:];
+[UIKeyCommand keyCommandWithInput:modifierFlags:action:upAction:];
+[UIKeyCommand keyCommandWithInput:modifierFlags:action:upAction:discoverabilityTitle:];
+[UIKeyCommand keyCommandWithInput:modifierFlags:buttonType:];
+[UIKeyCommand keyCommandWithKeyCode:modifierFlags:action:];
+[UIKeyCommand keyCommandWithKeyCode:modifierFlags:action:discoverabilityTitle:];
+[UIKeyCommand keyCommandWithKeyCodes:modifierFlags:action:];
+[UIKeyCommand keyCommandWithKeyCodes:modifierFlags:buttonType:];
```

## Instance methods

```
-[UIKeyCommand isPlaceholder];
-[UIKeyCommand input];
-[UIKeyCommand init];
-[UIKeyCommand modifierFlags];
-[UIKeyCommand setValue:forKey:];
-[UIKeyCommand _currentGSKeyboard];
-[UIKeyCommand _readableStringForModifierFlagsUsingWords:forHUD:];
-[UIKeyCommand encodeWithCoder:];
-[UIKeyCommand hash];
-[UIKeyCommand initWithCoder:];
-[UIKeyCommand initWithCommand:];
-[UIKeyCommand copyWithZone:];
-[UIKeyCommand isEqual:];
-[UIKeyCommand wantsPriorityOverSystemBehavior];
-[UIKeyCommand setAllowsAutomaticLocalization:];
-[UIKeyCommand _allowGlobeModifierKeyCommand];
-[UIKeyCommand _allowsGlobeKeyModifier];
-[UIKeyCommand _appendDescriptionComponentsToDescription:];
-[UIKeyCommand _buttonType];
-[UIKeyCommand _defaultEnumerationPriority];
-[UIKeyCommand _enumerationPriority];
-[UIKeyCommand _eventDeferringEnvironment];
-[UIKeyCommand _handleAfterKeyEvent];
-[UIKeyCommand _initWithCommand:keyboardShortcut:];
-[UIKeyCommand _initWithInput:modifierFlags:keyCodes:action:upAction:discoverabilityTitle:buttonType:];
-[UIKeyCommand _isKeyCommandLikelyMirrored];
-[UIKeyCommand _isKeyCommandLocalized];
-[UIKeyCommand _keyCodes];
-[UIKeyCommand _keyboardShortcut];
-[UIKeyCommand _layoutAwareDisplayInputOverride];
-[UIKeyCommand _layoutAwareInput];
-[UIKeyCommand _layoutAwareKeyCodes];
-[UIKeyCommand _layoutAwareModifierFlags];
-[UIKeyCommand _localizeWithGSKeyboard:automatically:force:];
-[UIKeyCommand _markHandleAfterKeyEvent];
-[UIKeyCommand _nonRepeatableKeyCommand];
-[UIKeyCommand _performDownActionWithSender:target:];
-[UIKeyCommand _performFallbackActionWithSender:target:];
-[UIKeyCommand _performKeyCommandActionWithSender:target:actionHandler:];
-[UIKeyCommand _performUpActionWithSender:target:];
-[UIKeyCommand _placeholderKeyCommand];
-[UIKeyCommand _readableStringForInputUsingWords:forHUD:outIsSingleCharacterOrKeySymbol:];
-[UIKeyCommand _safeCopy];
-[UIKeyCommand _setAllowsGlobeKeyModifier:];
-[UIKeyCommand _setEnumerationPriority:];
-[UIKeyCommand _setEventDeferringEnvironment:];
-[UIKeyCommand _wantsPriorityOverSystemBehavior:];
-[UIKeyCommand allowsAutomaticLocalization];
-[UIKeyCommand allowsAutomaticMirroring];
-[UIKeyCommand discoverabilityInput];
-[UIKeyCommand initWithKeyCommand:];
-[UIKeyCommand initWithTitle:image:imageName:action:input:modifierFlags:propertyList:leafOrCommandAlternates:discoverabilityTitle:attributes:state:];
-[UIKeyCommand initWithTitle:image:imageName:action:propertyList:leafOrCommandAlternates:discoverabilityTitle:attributes:state:];
-[UIKeyCommand performWithSender:target:];
-[UIKeyCommand repeatable];
-[UIKeyCommand setAllowsAutomaticMirroring:];
-[UIKeyCommand setWantsPriorityOverSystemBehavior:];
-[UIKeyCommand upAction];
```
