# `_UITextInputSessionEfficacyAccumulator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 2 properties, 13 instance methods, 4 class methods

## Instance variables

```
@"NSMutableDictionary" _entries;
@"NSString" _language;
@"NSString" _region;
@"NSString" _keyboardVariant;
@"NSString" _keyboardLayout;
@"NSString" _keyboardType;
B _sessionIsModeless;
@"NSMutableSet" _sessionErrors;
Q _largestSessionInsertionLength;
Q _largestSessionDeletionLength;
q _sessionNetCharacters;
B _insertionObservedInSession;
Q _charsRemovedBeforeFirstInsertionCount;
Q _emojisRemovedBeforeFirstInsertionCount;
@"NSString" _name;
@"NSDictionary" _keyboardTrialParameters;
```

## Properties

```
@property (T@"NSString",R,C,N,V_name) name;
@property (T@"NSDictionary",C,N,V_keyboardTrialParameters) keyboardTrialParameters;
```

## Class methods

```
+[_UITextInputSessionEfficacyAccumulator accumulatorWithName:];
+[_UITextInputSessionEfficacyAccumulator getOrInitializeArrayFromArray:forKey:initCapacity:];
+[_UITextInputSessionEfficacyAccumulator getOrInitializeArrayFromDictionary:forKey:initCapacity:];
+[_UITextInputSessionEfficacyAccumulator getOrInitializeDictionaryFrom:forKey:initCapacity:];
```

## Instance methods

```
-[_UITextInputSessionEfficacyAccumulator setKeyboardTrialParameters:];
-[_UITextInputSessionEfficacyAccumulator init];
-[_UITextInputSessionEfficacyAccumulator keyboardTrialParameters];
-[_UITextInputSessionEfficacyAccumulator reset];
-[_UITextInputSessionEfficacyAccumulator name];
-[_UITextInputSessionEfficacyAccumulator isPrimaryInput:];
-[_UITextInputSessionEfficacyAccumulator cleanIdForPublishing:];
-[_UITextInputSessionEfficacyAccumulator computeSessionActionsStringOnSession:];
-[_UITextInputSessionEfficacyAccumulator enumerateTextInputActionsAnalytics:];
-[_UITextInputSessionEfficacyAccumulator generateSessionErrorStringFromSet:];
-[_UITextInputSessionEfficacyAccumulator increaseCountForAppBundleId:forSource:forActionType:forFlagOptions:forInputModeKey:byAccumulatorEntry:];
-[_UITextInputSessionEfficacyAccumulator increaseWithAction:];
-[_UITextInputSessionEfficacyAccumulator logErrorCodeIfNotNil:];
```
