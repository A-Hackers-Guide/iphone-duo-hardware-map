# `_UIAppearanceRecorder`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 15 instance methods, 3 class methods

## Instance variables

```
@"NSString" _classNameToRecord;
# _superclassToRecord;
@"NSArray" _containerClassNames;
@"NSMutableArray" _customizations;
@"NSArray" _unarchivedCustomizations;
```

## Properties

```
@property (T@"NSString",C,N,S_setClassNameToRecord:,V_classNameToRecord) _classNameToRecord;
@property (T#,N,S_setSuperclassToRecord:,V_superclassToRecord) _superclassToRecord;
@property (T@"NSArray",C,N,S_setContainerClassNames:,V_containerClassNames) _containerClassNames;
@property (T@"NSData",R,N) _serializedRepresentation;
```

## Class methods

```
+[_UIAppearanceRecorder _sharedAppearanceRecorder];
+[_UIAppearanceRecorder _sharedAppearanceRecorderForClass:whenContainedIn:];
+[_UIAppearanceRecorder _sharedAppearanceRecorderForClassNamed:superclass:whenContainedIn:];
```

## Instance methods

```
-[_UIAppearanceRecorder init];
-[_UIAppearanceRecorder dealloc];
-[_UIAppearanceRecorder methodSignatureForSelector:];
-[_UIAppearanceRecorder initWithSerializedRepresentation:];
-[_UIAppearanceRecorder forwardInvocation:];
-[_UIAppearanceRecorder _applyCustomizations];
-[_UIAppearanceRecorder _classNameToRecord];
-[_UIAppearanceRecorder _containerClassNames];
-[_UIAppearanceRecorder _importCustomizations:withArchiveVersion:];
-[_UIAppearanceRecorder _recordInvocation:withClassName:containerClassNames:traitCollection:selectorString:forRemoteProcess:];
-[_UIAppearanceRecorder _serializedRepresentation];
-[_UIAppearanceRecorder _setClassNameToRecord:];
-[_UIAppearanceRecorder _setContainerClassNames:];
-[_UIAppearanceRecorder _setSuperclassToRecord:];
-[_UIAppearanceRecorder _superclassToRecord];
```
