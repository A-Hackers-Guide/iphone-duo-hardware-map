# `SBAlwaysOnPolicySettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 11 instance variables, 12 properties, 25 instance methods, 2 class methods

## Instance variables

```
B _semanticTypeCustom;
B _semanticTypeDefault;
B _semanticTypeSleep;
B _semanticTypeDriving;
B _semanticTypeExercise;
B _semanticTypeWork;
B _semanticTypePersonal;
B _semanticTypeReading;
B _semanticTypeGaming;
B _semanticTypeMindfulness;
q _focusStrategy;
```

## Properties

```
@property (TB,N,V_semanticTypeCustom) semanticTypeCustom;
@property (TB,N,V_semanticTypeDefault) semanticTypeDefault;
@property (TB,N,V_semanticTypeSleep) semanticTypeSleep;
@property (TB,N,V_semanticTypeDriving) semanticTypeDriving;
@property (TB,N,V_semanticTypeExercise) semanticTypeExercise;
@property (TB,N,V_semanticTypeWork) semanticTypeWork;
@property (TB,N,V_semanticTypePersonal) semanticTypePersonal;
@property (TB,N,V_semanticTypeReading) semanticTypeReading;
@property (TB,N,V_semanticTypeGaming) semanticTypeGaming;
@property (TB,N,V_semanticTypeMindfulness) semanticTypeMindfulness;
@property (Tq,N,V_focusStrategy) focusStrategy;
@property (T@"NSSet",C,D,N) alwaysOnDisablingFocusSemanticTypes;
```

## Class methods

```
+[SBAlwaysOnPolicySettings settingsControllerModule];
+[SBAlwaysOnPolicySettings _keyPathForSemanticTypeName:];
```

## Instance methods

```
-[SBAlwaysOnPolicySettings setDefaultValues];
-[SBAlwaysOnPolicySettings alwaysOnDisablingFocusSemanticTypes];
-[SBAlwaysOnPolicySettings focusStrategy];
-[SBAlwaysOnPolicySettings semanticTypeCustom];
-[SBAlwaysOnPolicySettings semanticTypeDefault];
-[SBAlwaysOnPolicySettings semanticTypeDriving];
-[SBAlwaysOnPolicySettings semanticTypeExercise];
-[SBAlwaysOnPolicySettings semanticTypeGaming];
-[SBAlwaysOnPolicySettings semanticTypeMindfulness];
-[SBAlwaysOnPolicySettings semanticTypePersonal];
-[SBAlwaysOnPolicySettings semanticTypeReading];
-[SBAlwaysOnPolicySettings semanticTypeSleep];
-[SBAlwaysOnPolicySettings semanticTypeWork];
-[SBAlwaysOnPolicySettings setAlwaysOnDisablingFocusSemanticTypes:];
-[SBAlwaysOnPolicySettings setFocusStrategy:];
-[SBAlwaysOnPolicySettings setSemanticTypeCustom:];
-[SBAlwaysOnPolicySettings setSemanticTypeDefault:];
-[SBAlwaysOnPolicySettings setSemanticTypeDriving:];
-[SBAlwaysOnPolicySettings setSemanticTypeExercise:];
-[SBAlwaysOnPolicySettings setSemanticTypeGaming:];
-[SBAlwaysOnPolicySettings setSemanticTypeMindfulness:];
-[SBAlwaysOnPolicySettings setSemanticTypePersonal:];
-[SBAlwaysOnPolicySettings setSemanticTypeReading:];
-[SBAlwaysOnPolicySettings setSemanticTypeSleep:];
-[SBAlwaysOnPolicySettings setSemanticTypeWork:];
```
