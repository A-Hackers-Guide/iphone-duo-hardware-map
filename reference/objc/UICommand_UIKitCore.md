# `UICommand`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIMenuElement`
- Protocols: `_UIMenuLeaf`, `_UIMenuStateObserverableLeaf`, `UIMenuLeaf`
- 13 instance variables, 35 properties, 65 instance methods, 9 class methods

## Instance variables

```
@"NSArray" _alternates;
b32 _attributes;
b32 _state;
b32 _repeatBehavior;
B __useSenderForResolvingTarget;
@"NSPointerArray" stateObservers;
@ _sender;
@"UIImage" _selectedImage;
@"NSString" _discoverabilityTitle;
: _action;
@ _propertyList;
: _fallbackAction;
@ __target;
```

## Properties

```
@property (T@"_UICommandIdentifier",R,N) _identifier;
@property (T:,R,N,V_fallbackAction) fallbackAction;
@property (TB,N,V__useSenderForResolvingTarget) _useSenderForResolvingTarget;
@property (T@,R,N,V__target) _target;
@property (T@"NSString",C,D,N) title;
@property (T@"UIImage",C,D,N) image;
@property (T@"NSString",C,N,V_discoverabilityTitle) discoverabilityTitle;
@property (T:,R,N,V_action) action;
@property (T@,R,N,V_propertyList) propertyList;
@property (TQ,N,V_attributes) attributes;
@property (Tq,N,V_state) state;
@property (T@"NSArray",R,N) alternates;
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
@property (T@"NSString",C,N) subtitle;
@property (T@"UIImage",C,N,V_selectedImage) selectedImage;
@property (Tq,N) preferredImageVisibility;
@property (Tq,N) repeatBehavior;
@property (T@,R,N,V_sender) sender;
@property (T@"<UIPopoverPresentationControllerSourceItem>",R,N) presentationSourceItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSPointerArray",&,N,G_getStateObservers,S_setStateObservers:,VstateObservers) stateObservers;
```

## Class methods

```
+[UICommand supportsSecureCoding];
+[UICommand _defaultCommandForAction:];
+[UICommand _originalCommandForAction:];
+[UICommand commandWithTitle:image:action:propertyList:];
+[UICommand commandWithTitle:image:action:propertyList:alternates:];
+[UICommand commandWithTitle:imageName:action:];
+[UICommand commandWithTitle:imageName:action:fallbackAction:];
+[UICommand commandWithTitle:imageName:attributes:action:];
+[UICommand commandWithTitle:imageName:preferredDisplayMode:action:];
```

## Instance methods

```
-[UICommand _target];
-[UICommand setState:];
-[UICommand propertyList];
-[UICommand setAttributes:];
-[UICommand action];
-[UICommand keepsMenuPresented];
-[UICommand setSubtitle:];
-[UICommand sender];
-[UICommand selectedImage];
-[UICommand encodeWithCoder:];
-[UICommand hash];
-[UICommand description];
-[UICommand initWithCoder:];
-[UICommand setTitle:];
-[UICommand attributes];
-[UICommand setSelectedImage:];
-[UICommand initWithCommand:];
-[UICommand copyWithZone:];
-[UICommand isEqual:];
-[UICommand _identifier];
-[UICommand state];
-[UICommand alternates];
-[UICommand setImage:];
-[UICommand _acceptMenuVisit:commandVisit:actionVisit:deferredElementVisit:];
-[UICommand _isLeaf];
-[UICommand initWithTitle:image:imageName:action:fallbackAction:propertyList:leafOrCommandAlternates:discoverabilityTitle:attributes:state:];
-[UICommand _acceptBoolMenuVisit:leafVisit:];
-[UICommand _leafAlternates];
-[UICommand _acceptBoolMenuVisit:commandVisit:actionVisit:];
-[UICommand _acceptMenuVisit:leafVisit:];
-[UICommand _addStateObserver:];
-[UICommand _allowsGlobeKeyModifier];
-[UICommand _appendDescriptionComponentsToDescription:];
-[UICommand _enumerationPriority];
-[UICommand _eventDeferringEnvironment];
-[UICommand _getStateObservers];
-[UICommand _isDefaultCommand];
-[UICommand _keyboardShortcut];
-[UICommand _menuLeafWithKeyboardShortcut:];
-[UICommand _pasteVariant];
-[UICommand _performAction:withSender:target:notifyingStateObservers:];
-[UICommand _performFallbackActionWithSender:target:];
-[UICommand _performWithSender:handler:];
-[UICommand _removeStateObserver:];
-[UICommand _resolvedTargetFromFirstTarget:sender:];
-[UICommand _resolvedTargetFromFirstTarget:sender:shouldUseFallbackActionOut:];
-[UICommand _secureVariant];
-[UICommand _setAllowsGlobeKeyModifier:];
-[UICommand _setEnumerationPriority:];
-[UICommand _setLeafAlternates:];
-[UICommand _setState:notifyingObservers:];
-[UICommand _setStateObservers:];
-[UICommand _storedLeafAlternates];
-[UICommand _useSenderForResolvingTarget];
-[UICommand _validatedLeafWithTarget:validator:];
-[UICommand _wantsPriorityOverSystemBehavior:];
-[UICommand discoverabilityTitle];
-[UICommand fallbackAction];
-[UICommand initWithTitle:image:imageName:action:propertyList:leafOrCommandAlternates:discoverabilityTitle:attributes:state:];
-[UICommand performWithSender:target:];
-[UICommand presentationSourceItem];
-[UICommand repeatBehavior];
-[UICommand setDiscoverabilityTitle:];
-[UICommand setRepeatBehavior:];
-[UICommand set_useSenderForResolvingTarget:];
```
