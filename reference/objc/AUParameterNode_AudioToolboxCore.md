# `AUParameterNode`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 16 properties, 45 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSString" _displayName;
Q _indexInGroup;
@"AUParameterGroup" _parentNode;
^v _observerList;
@? _impl_implementorValueObserver;
@? _impl_implementorValueProvider;
@? _impl_implementorStringFromValueCallback;
@? _impl_implementorValueFromStringCallback;
@? _impl_implementorDisplayNameWithLengthCallback;
```

## Properties

```
@property (T@?,C,N) implementorValueObserver;
@property (T@?,C,N) implementorValueProvider;
@property (T@?,C,N) implementorStringFromValueCallback;
@property (T@?,C,N) implementorValueFromStringCallback;
@property (T@?,C,N) implementorDisplayNameWithLengthCallback;
@property (TQ,N,V_indexInGroup) indexInGroup;
@property (T@"AUParameterGroup",W,N,V_parentNode) parentNode;
@property (T^v,N,V_observerList) observerList;
@property (T@?,C,N,V_impl_implementorValueObserver) impl_implementorValueObserver;
@property (T@?,C,N,V_impl_implementorValueProvider) impl_implementorValueProvider;
@property (T@?,C,N,V_impl_implementorStringFromValueCallback) impl_implementorStringFromValueCallback;
@property (T@?,C,N,V_impl_implementorValueFromStringCallback) impl_implementorValueFromStringCallback;
@property (T@?,C,N,V_impl_implementorDisplayNameWithLengthCallback) impl_implementorDisplayNameWithLengthCallback;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"NSString",R,C,N) keyPath;
@property (T@"NSString",R,C,N,V_displayName) displayName;
```

## Instance methods

```
-[AUParameterNode _deserialize:fromSetFullState:];
-[AUParameterNode keyPath];
-[AUParameterNode identifier];
-[AUParameterNode _serialize:];
-[AUParameterNode displayName];
-[AUParameterNode dealloc];
-[AUParameterNode copyNodeWithOffset:];
-[AUParameterNode _observersChanged:deltaCount:];
-[AUParameterNode parentNode];
-[AUParameterNode description];
-[AUParameterNode isGroup];
-[AUParameterNode tokenByAddingParameterObserver:];
-[AUParameterNode _addRecObserver:autoObserver:];
-[AUParameterNode _rootParent];
-[AUParameterNode _walkTree:callback:];
-[AUParameterNode displayNameWithLength:];
-[AUParameterNode impl_implementorDisplayNameWithLengthCallback];
-[AUParameterNode impl_implementorStringFromValueCallback];
-[AUParameterNode impl_implementorValueFromStringCallback];
-[AUParameterNode impl_implementorValueObserver];
-[AUParameterNode impl_implementorValueProvider];
-[AUParameterNode implementorDisplayNameWithLengthCallback];
-[AUParameterNode implementorStringFromValueCallback];
-[AUParameterNode implementorValueFromStringCallback];
-[AUParameterNode implementorValueObserver];
-[AUParameterNode implementorValueProvider];
-[AUParameterNode indexInGroup];
-[AUParameterNode initWithID:name:];
-[AUParameterNode observerList];
-[AUParameterNode removeParameterObserver:];
-[AUParameterNode setImpl_implementorDisplayNameWithLengthCallback:];
-[AUParameterNode setImpl_implementorStringFromValueCallback:];
-[AUParameterNode setImpl_implementorValueFromStringCallback:];
-[AUParameterNode setImpl_implementorValueObserver:];
-[AUParameterNode setImpl_implementorValueProvider:];
-[AUParameterNode setImplementorDisplayNameWithLengthCallback:];
-[AUParameterNode setImplementorStringFromValueCallback:];
-[AUParameterNode setImplementorValueFromStringCallback:];
-[AUParameterNode setImplementorValueObserver:];
-[AUParameterNode setImplementorValueProvider:];
-[AUParameterNode setIndexInGroup:];
-[AUParameterNode setObserverList:];
-[AUParameterNode setParentNode:];
-[AUParameterNode tokenByAddingParameterAutomationObserver:];
-[AUParameterNode tokenByAddingParameterRecordingObserver:];
```
