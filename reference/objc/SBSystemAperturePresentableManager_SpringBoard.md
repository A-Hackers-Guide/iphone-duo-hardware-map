# `SBSystemAperturePresentableManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAUILayoutObserving`, `SBPresentableIntercepting`
- 4 instance variables, 4 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _presentablesToElements;
@"NSMapTable" _elementsToAssertions;
@"NSHashTable" _elementsThatDidAppear;
@"<SBSystemApertureBackgroundActivitiesSuppressing><SAElementRegistering>" _elementRegistrar;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemAperturePresentableManager _invalidateElement:withReason:];
-[SBSystemAperturePresentableManager _registerElement:];
-[SBSystemAperturePresentableManager _removeAssertionForElement:];
-[SBSystemAperturePresentableManager elementLayoutSpecifier:layoutModeDidChange:reason:];
-[SBSystemAperturePresentableManager _elementForPresentableCreatingIfNecessary:elementGenerator:];
-[SBSystemAperturePresentableManager _existingAssertionForElement:];
-[SBSystemAperturePresentableManager _existingElementForPresentableWithIdentification:];
-[SBSystemAperturePresentableManager _existingPresentableWithIdentification:];
-[SBSystemAperturePresentableManager _existingPresentablesWithIdentification:];
-[SBSystemAperturePresentableManager _noteElementDidAppear:];
-[SBSystemAperturePresentableManager _noteElementDidDisappear:reason:];
-[SBSystemAperturePresentableManager _noteElementDidInvalidate:reason:];
-[SBSystemAperturePresentableManager _noteElementWillDisappear:reason:];
-[SBSystemAperturePresentableManager _noteElementWillNotAppearAsBanner:reason:];
-[SBSystemAperturePresentableManager _presentableElementForElementLayoutSpecifier:];
-[SBSystemAperturePresentableManager _removeElementForPresentableWithIdentification:];
-[SBSystemAperturePresentableManager _removePresentableForElement:];
-[SBSystemAperturePresentableManager _sync_registerAssertion:forElement:];
-[SBSystemAperturePresentableManager _takeProcessAssertionForElement:];
-[SBSystemAperturePresentableManager initWithElementRegistrar:];
-[SBSystemAperturePresentableManager revocationRequestedForPresentablesWithIdentification:reason:];
-[SBSystemAperturePresentableManager willInterceptPresentable:userInfo:];
```
