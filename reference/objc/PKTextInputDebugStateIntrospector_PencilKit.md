# `PKTextInputDebugStateIntrospector`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 13 instance methods, 3 class methods

## Instance variables

```
@"PKTextInputInteraction" _interaction;
@"<PKTextInputDebugStateIntrospectorDelegate>" _delegate;
```

## Properties

```
@property (T@"PKTextInputInteraction",R,W,N,V_interaction) interaction;
@property (T@"<PKTextInputDebugStateIntrospectorDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[PKTextInputDebugStateIntrospector _knownInstances];
+[PKTextInputDebugStateIntrospector debugStateDidChange];
+[PKTextInputDebugStateIntrospector debugStateLineDescriptionForIntrospectable:];
```

## Instance methods

```
-[PKTextInputDebugStateIntrospector interaction];
-[PKTextInputDebugStateIntrospector dealloc];
-[PKTextInputDebugStateIntrospector initWithInteraction:];
-[PKTextInputDebugStateIntrospector setDelegate:];
-[PKTextInputDebugStateIntrospector delegate];
-[PKTextInputDebugStateIntrospector _debugStateDidChange];
-[PKTextInputDebugStateIntrospector _introspectableForStateKey:];
-[PKTextInputDebugStateIntrospector debugStateCanShowDetailsForStateKey:];
-[PKTextInputDebugStateIntrospector debugStateDescriptionForStateKey:];
-[PKTextInputDebugStateIntrospector debugStateDetailViewControllerForStateKey:];
-[PKTextInputDebugStateIntrospector debugStateKeys];
-[PKTextInputDebugStateIntrospector debugStateTitleForStateKey:];
-[PKTextInputDebugStateIntrospector fullDebugStateDescription];
```
