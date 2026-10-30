# `UIInputViewSetNotificationInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 22 properties, 52 instance methods, 1 class methods

## Instance variables

```
B _changedAccessoryOnly;
B _assistantOnScreenOnly;
B _forceNotification;
B _wasCausedRemotely;
B _dueToRotation;
B _forWritingToolsSheet;
B _shouldSendInClient;
B _waitingForInputUI;
B _nonKeyboardOverride;
d _duration;
Q _options;
Q _assistantPosition;
Q _type;
@"NSString" _debugInfo;
{CGPoint="x"d"y"d} _beginCenter;
{CGPoint="x"d"y"d} _endCenter;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _beginFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _endFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _assistantFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
```

## Properties

```
@property (T@"NSString",&,N,V_debugInfo) debugInfo;
@property (TB,N,V_nonKeyboardOverride) nonKeyboardOverride;
@property (T@"NSDictionary",R,N) userInfo;
@property (T@"NSDictionary",R,N) privateUserInfo;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_beginFrame) beginFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_endFrame) endFrame;
@property (Td,N,V_duration) duration;
@property (TQ,N,V_options) options;
@property (TB,N,V_changedAccessoryOnly) changedAccessoryOnly;
@property (TB,N,V_assistantOnScreenOnly) assistantOnScreenOnly;
@property (TQ,N,V_assistantPosition) assistantPosition;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_assistantFrame) assistantFrame;
@property (TB,N,V_forceNotification) forceNotification;
@property (TB,N,V_wasCausedRemotely) wasCausedRemotely;
@property (TB,N,V_dueToRotation) dueToRotation;
@property (TB,N,V_forWritingToolsSheet) forWritingToolsSheet;
@property (TB,N,V_shouldSendInClient) shouldSendInClient;
@property (TQ,N,V_type) type;
@property (TB,N,V_waitingForInputUI) waitingForInputUI;
@property (T{CGPoint=dd},N,V_beginCenter) beginCenter;
@property (T{CGPoint=dd},N,V_endCenter) endCenter;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_bounds) bounds;
```

## Class methods

```
+[UIInputViewSetNotificationInfo info];
```

## Instance methods

```
-[UIInputViewSetNotificationInfo setForceNotification:];
-[UIInputViewSetNotificationInfo setBeginFrame:];
-[UIInputViewSetNotificationInfo assistantPosition];
-[UIInputViewSetNotificationInfo forceNotification];
-[UIInputViewSetNotificationInfo dueToRotation];
-[UIInputViewSetNotificationInfo endFrame];
-[UIInputViewSetNotificationInfo setAssistantFrame:];
-[UIInputViewSetNotificationInfo setDueToRotation:];
-[UIInputViewSetNotificationInfo assistantFrame];
-[UIInputViewSetNotificationInfo setOptions:];
-[UIInputViewSetNotificationInfo setWasCausedRemotely:];
-[UIInputViewSetNotificationInfo beginFrame];
-[UIInputViewSetNotificationInfo setAssistantOnScreenOnly:];
-[UIInputViewSetNotificationInfo changedAccessoryOnly];
-[UIInputViewSetNotificationInfo init];
-[UIInputViewSetNotificationInfo rotationUserInfo];
-[UIInputViewSetNotificationInfo debugInfo];
-[UIInputViewSetNotificationInfo privateUserInfo];
-[UIInputViewSetNotificationInfo wasCausedRemotely];
-[UIInputViewSetNotificationInfo assistantOnScreenOnly];
-[UIInputViewSetNotificationInfo waitingForInputUI];
-[UIInputViewSetNotificationInfo setAssistantPosition:];
-[UIInputViewSetNotificationInfo setEndCenter:];
-[UIInputViewSetNotificationInfo setDebugInfo:];
-[UIInputViewSetNotificationInfo setChangedAccessoryOnly:];
-[UIInputViewSetNotificationInfo setShouldSendInClient:];
-[UIInputViewSetNotificationInfo userInfo];
-[UIInputViewSetNotificationInfo setWaitingForInputUI:];
-[UIInputViewSetNotificationInfo setEndFrame:];
-[UIInputViewSetNotificationInfo containsChange];
-[UIInputViewSetNotificationInfo setBounds:];
-[UIInputViewSetNotificationInfo duration];
-[UIInputViewSetNotificationInfo setNonKeyboardOverride:];
-[UIInputViewSetNotificationInfo setType:];
-[UIInputViewSetNotificationInfo type];
-[UIInputViewSetNotificationInfo forWritingToolsSheet];
-[UIInputViewSetNotificationInfo nonKeyboardOverride];
-[UIInputViewSetNotificationInfo bounds];
-[UIInputViewSetNotificationInfo setForWritingToolsSheet:];
-[UIInputViewSetNotificationInfo description];
-[UIInputViewSetNotificationInfo endCenter];
-[UIInputViewSetNotificationInfo options];
-[UIInputViewSetNotificationInfo setDuration:];
-[UIInputViewSetNotificationInfo inverseInfo];
-[UIInputViewSetNotificationInfo logGeometry];
-[UIInputViewSetNotificationInfo populateEndInfoWithFrame:];
-[UIInputViewSetNotificationInfo populateStartInfoWithFrame:];
-[UIInputViewSetNotificationInfo populateWithAnimationStyle:];
-[UIInputViewSetNotificationInfo addKeyboardNotificationDebuggingInfo:];
-[UIInputViewSetNotificationInfo setBeginCenter:];
-[UIInputViewSetNotificationInfo beginCenter];
-[UIInputViewSetNotificationInfo shouldSendInClient];
```
