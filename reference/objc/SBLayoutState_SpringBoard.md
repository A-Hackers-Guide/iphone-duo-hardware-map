# `SBLayoutState`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 4 instance variables, 7 properties, 30 instance methods, 0 class methods

## Instance variables

```
q _interfaceOrientation;
@"NSDictionary" _cachedLayoutAttributesIfAny;
@"NSSet" _elements;
@"NSDictionary" _interfaceOrientationByLayoutElementIdentifier;
```

## Properties

```
@property (Tq,N,V_interfaceOrientation) interfaceOrientation;
@property (T@"NSDictionary",C,N,V_interfaceOrientationByLayoutElementIdentifier) interfaceOrientationByLayoutElementIdentifier;
@property (T@"NSSet",R,N,V_elements) elements;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLayoutState interfaceOrientation];
-[SBLayoutState elements];
-[SBLayoutState succinctDescriptionBuilder];
-[SBLayoutState setInterfaceOrientation:];
-[SBLayoutState invalidateAppLayout];
-[SBLayoutState init];
-[SBLayoutState appLayout];
-[SBLayoutState invalidateFloatingAppLayout];
-[SBLayoutState descriptionWithMultilinePrefix:];
-[SBLayoutState setInterfaceOrientationByLayoutElementIdentifier:];
-[SBLayoutState succinctDescription];
-[SBLayoutState layoutAttributesMap];
-[SBLayoutState hash];
-[SBLayoutState description];
-[SBLayoutState isEqual:];
-[SBLayoutState _initWithLayoutElements:interfaceOrientation:interfaceOrientationByLayoutElement:];
-[SBLayoutState floatingAppLayout];
-[SBLayoutState _defaultInterfaceOrientation];
-[SBLayoutState descriptionBuilderWithMultilinePrefix:];
-[SBLayoutState elementWithIdentifier:];
-[SBLayoutState _interfaceOrientationForElementIdentifier:unknownAllowed:];
-[SBLayoutState elementWithRole:];
-[SBLayoutState interfaceOrientationByLayoutElementIdentifier];
-[SBLayoutState interfaceOrientationForElementIdentifier:];
-[SBLayoutState interfaceOrientationForLayoutElement:];
-[SBLayoutState interfaceOrientationForLayoutElement:unknownAllowed:];
-[SBLayoutState interfaceOrientationForLayoutRole:];
-[SBLayoutState isEqual:withRole:];
-[SBLayoutState isMeaningfullyDifferentFromLayoutState:];
-[SBLayoutState layoutContainsRole:];
```
