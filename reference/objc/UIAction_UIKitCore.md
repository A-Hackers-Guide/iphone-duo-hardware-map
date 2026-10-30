# `UIAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIMenuElement`
- Protocols: `_UIMenuLeaf`, `_UIMenuStateObserverableLeaf`, `UIMenuLeaf`
- 14 instance variables, 31 properties, 57 instance methods, 10 class methods

## Instance variables

```
B _allowsGlobeKeyModifier;
@"NSPointerArray" stateObservers;
@ _sender;
@"UIImage" _selectedImage;
q _repeatBehavior;
@"NSArray" _leafAlternates;
@"_UIMenuLeafKeyboardShortcut" _keyboardShortcut;
q _enumerationPriority;
q _systemBehaviorsToOutPrioritize;
@"NSString" _discoverabilityTitle;
@"NSString" _identifier;
Q _attributes;
q _state;
@? _handler;
```

## Properties

```
@property (T@?,C,N,V_handler) handler;
@property (T@"_UIMenuLeafKeyboardShortcut",&,N,S_setKeyboardShortcut:,V_keyboardShortcut) _keyboardShortcut;
@property (Tq,N,V_systemBehaviorsToOutPrioritize) _systemBehaviorsToOutPrioritize;
@property (T@"NSString",C,D,N) title;
@property (T@"UIImage",C,D,N) image;
@property (T@"NSString",C,N,V_discoverabilityTitle) discoverabilityTitle;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (TQ,N,V_attributes) attributes;
@property (Tq,N,V_state) state;
@property (T@,R,N,V_sender) sender;
@property (T@"NSAttributedString",C,N) attributedTitle;
@property (TB,R,N) keepsMenuPresented;
@property (T@"_UITextStyleDescriptor",C,N) _titleStyleDescriptor;
@property (T@"UISPasteVariant",R,N) _pasteVariant;
@property (T@"<UISSecureVariant>",R,N) _secureVariant;
@property (T@"NSArray",C,N,S_setLeafAlternates:,V_leafAlternates) _leafAlternates;
@property (Tq,N,S_setEnumerationPriority:,V_enumerationPriority) _enumerationPriority;
@property (T@"BKSHIDEventDeferringEnvironment",R,N) _eventDeferringEnvironment;
@property (TB,N,S_setAllowsGlobeKeyModifier:,V_allowsGlobeKeyModifier) _allowsGlobeKeyModifier;
@property (TB,R,N) _isIntelligentAssistantAction;
@property (T@"<UIPopoverPresentationControllerSourceItem>",?,W,N,S_setOverridePresentationSourceItem:) _overridePresentationSourceItem;
@property (T@"NSString",C,N) subtitle;
@property (T@"UIImage",C,N,V_selectedImage) selectedImage;
@property (Tq,N) preferredImageVisibility;
@property (Tq,N,V_repeatBehavior) repeatBehavior;
@property (T@"<UIPopoverPresentationControllerSourceItem>",R,N) presentationSourceItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSPointerArray",&,N,G_getStateObservers,S_setStateObservers:,VstateObservers) stateObservers;
```

## Class methods

```
+[UIAction supportsSecureCoding];
+[UIAction _intelligentAssistantActionWithIdentifier:configuration:];
+[UIAction _textFromCameraImage];
+[UIAction _textFromCameraImageName];
+[UIAction _textFromCameraTitle];
+[UIAction _textFromCameraTitleForResponder:];
+[UIAction actionWithHandler:];
+[UIAction actionWithTitle:image:identifier:handler:];
+[UIAction captureTextFromCameraActionForResponder:identifier:];
+[UIAction textInteractableItemDefaultAction];
```

## Instance methods

```
-[UIAction setState:];
-[UIAction identifier];
-[UIAction setAttributes:];
-[UIAction setHandler:];
-[UIAction keepsMenuPresented];
-[UIAction setSubtitle:];
-[UIAction sender];
-[UIAction initWithAction:];
-[UIAction handler];
-[UIAction selectedImage];
-[UIAction encodeWithCoder:];
-[UIAction hash];
-[UIAction description];
-[UIAction initWithCoder:];
-[UIAction setTitle:];
-[UIAction attributes];
-[UIAction setSelectedImage:];
-[UIAction copyWithZone:];
-[UIAction isEqual:];
-[UIAction state];
-[UIAction setImage:];
-[UIAction _acceptMenuVisit:commandVisit:actionVisit:deferredElementVisit:];
-[UIAction _isLeaf];
-[UIAction _acceptBoolMenuVisit:leafVisit:];
-[UIAction _leafAlternates];
-[UIAction _systemBehaviorsToOutPrioritize];
-[UIAction _acceptBoolMenuVisit:commandVisit:actionVisit:];
-[UIAction _acceptMenuVisit:leafVisit:];
-[UIAction _addStateObserver:];
-[UIAction _allowsGlobeKeyModifier];
-[UIAction _enumerationPriority];
-[UIAction _eventDeferringEnvironment];
-[UIAction _getStateObservers];
-[UIAction _isDefaultCommand];
-[UIAction _keyboardShortcut];
-[UIAction _menuLeafWithKeyboardShortcut:];
-[UIAction _pasteVariant];
-[UIAction _performWithTarget:];
-[UIAction _removeStateObserver:];
-[UIAction _resolvedTargetFromFirstTarget:sender:];
-[UIAction _secureVariant];
-[UIAction _setAllowsGlobeKeyModifier:];
-[UIAction _setEnumerationPriority:];
-[UIAction _setKeyboardShortcut:];
-[UIAction _setLeafAlternates:];
-[UIAction _setState:notifyingObservers:];
-[UIAction _setStateObservers:];
-[UIAction _validatedLeafWithTarget:validator:];
-[UIAction _wantsPriorityOverSystemBehavior:];
-[UIAction discoverabilityTitle];
-[UIAction initWithTitle:image:identifier:discoverabilityTitle:attributes:state:handler:];
-[UIAction performWithSender:target:];
-[UIAction presentationSourceItem];
-[UIAction repeatBehavior];
-[UIAction setDiscoverabilityTitle:];
-[UIAction setRepeatBehavior:];
-[UIAction set_systemBehaviorsToOutPrioritize:];
```
