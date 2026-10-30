# `UISceneConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDebugDescriptionProviding`, `NSCopying`, `NSSecureCoding`
- 13 instance variables, 15 properties, 34 instance methods, 4 class methods

## Instance variables

```
B _hadResolutionErrorsOnLoad;
B _isDefault;
B _fromPlist;
B _isPendingInfoPlistResolution;
@"NSString" _name;
@"NSString" _requestedName;
@"NSString" _role;
# _sceneClass;
# _delegateClass;
@"UIStoryboard" _storyboard;
B _canBeAppliedToInternalScenes;
@"NSString" _bridgingID;
# _sceneDelegateWrapper;
```

## Properties

```
@property (TB,R,N,V_hadResolutionErrorsOnLoad) _hadResolutionErrorsOnLoad;
@property (TB,R,N,V_isDefault) _isDefault;
@property (TB,R,N,V_fromPlist) _fromPlist;
@property (TB,R,N,V_isPendingInfoPlistResolution) _isPendingInfoPlistResolution;
@property (T@"NSString",R,N,V_bridgingID) _bridgingID;
@property (TB,R,N,V_canBeAppliedToInternalScenes) _canBeAppliedToInternalScenes;
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_role) role;
@property (T#,&,N) sceneClass;
@property (T#,&,N) delegateClass;
@property (T@"UIStoryboard",&,N) storyboard;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISceneConfiguration supportsSecureCoding];
+[UISceneConfiguration _internalConfigurationWithRole:sceneClass:delegateClass:bridgingID:sceneDelegateWrapper:];
+[UISceneConfiguration _internalConfigurationWithRole:sceneClass:delegateClass:storyboard:];
+[UISceneConfiguration configurationWithName:sessionRole:];
```

## Instance methods

```
-[UISceneConfiguration _isDefault];
-[UISceneConfiguration debugDescription];
-[UISceneConfiguration succinctDescriptionBuilder];
-[UISceneConfiguration init];
-[UISceneConfiguration descriptionWithMultilinePrefix:];
-[UISceneConfiguration succinctDescription];
-[UISceneConfiguration debugDescriptionWithMultilinePrefix:];
-[UISceneConfiguration _initWithConfiguration:];
-[UISceneConfiguration encodeWithCoder:];
-[UISceneConfiguration role];
-[UISceneConfiguration hash];
-[UISceneConfiguration description];
-[UISceneConfiguration initWithCoder:];
-[UISceneConfiguration copyWithZone:];
-[UISceneConfiguration isEqual:];
-[UISceneConfiguration name];
-[UISceneConfiguration initWithName:];
-[UISceneConfiguration descriptionBuilderWithMultilinePrefix:];
-[UISceneConfiguration _attemptResolveAgainstInfoPlistWithName:sessionRole:];
-[UISceneConfiguration _bridgingID];
-[UISceneConfiguration _canBeAppliedToInternalScenes];
-[UISceneConfiguration _fromPlist];
-[UISceneConfiguration _hadResolutionErrorsOnLoad];
-[UISceneConfiguration _initWithConfiguration:sceneDelegateWrapper:];
-[UISceneConfiguration _initWithLoadErrorForSessionRole:];
-[UISceneConfiguration _initWithRole:bridgingID:sceneDelegateWrapper:];
-[UISceneConfiguration _isPendingInfoPlistResolution];
-[UISceneConfiguration delegateClass];
-[UISceneConfiguration initWithName:sessionRole:];
-[UISceneConfiguration sceneClass];
-[UISceneConfiguration setDelegateClass:];
-[UISceneConfiguration setSceneClass:];
-[UISceneConfiguration setStoryboard:];
-[UISceneConfiguration storyboard];
```
