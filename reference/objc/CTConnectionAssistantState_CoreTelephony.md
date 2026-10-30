# `CTConnectionAssistantState`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 18 instance variables, 18 properties, 40 instance methods, 1 class methods

## Instance variables

```
B _isEmergencyVoiceCallCapable;
Q _version;
@"CTStewieState" _stewieState;
q _internetInterface;
@"CTCATarget" _currentTarget;
@"NSArray" _backupTargets;
@"CTCATargetVisibility" _targetVisibility;
@"CTCALocationState" _locationState;
@"CTCAServiceIntervals" _serviceIntervals;
@"CTCASilenceInterval" _silenceInterval;
@"CTCAConnectionState" _connectionState;
@"CTCAConversationState" _conversationState;
@"CTCARoadsideConversationState" _roadsideConversationState;
@"NSString" _iso3166Alpha3CountryCode;
@"CTCAServicePartners" _servicePartners;
@"CTCAConnectionClosedState" _connectionClosedState;
@"CTCATryOutState" _tryOutState;
@"NSString" _emergencyOrRoadsideSessionInitiatedBy;
```

## Properties

```
@property (TQ,N,V_version) version;
@property (T@"CTStewieState",&,N,V_stewieState) stewieState;
@property (Tq,N,V_internetInterface) internetInterface;
@property (T@"CTCATarget",&,N,V_currentTarget) currentTarget;
@property (T@"NSArray",&,N,V_backupTargets) backupTargets;
@property (T@"CTCATargetVisibility",&,N,V_targetVisibility) targetVisibility;
@property (T@"CTCALocationState",&,N,V_locationState) locationState;
@property (T@"CTCAServiceIntervals",&,N,V_serviceIntervals) serviceIntervals;
@property (T@"CTCASilenceInterval",&,N,V_silenceInterval) silenceInterval;
@property (T@"CTCAConnectionState",&,N,V_connectionState) connectionState;
@property (T@"CTCAConversationState",&,N,V_conversationState) conversationState;
@property (T@"CTCARoadsideConversationState",&,N,V_roadsideConversationState) roadsideConversationState;
@property (T@"NSString",&,N,V_iso3166Alpha3CountryCode) iso3166Alpha3CountryCode;
@property (T@"CTCAServicePartners",&,N,V_servicePartners) servicePartners;
@property (T@"CTCAConnectionClosedState",&,N,V_connectionClosedState) connectionClosedState;
@property (T@"CTCATryOutState",&,N,V_tryOutState) tryOutState;
@property (TB,N,V_isEmergencyVoiceCallCapable) isEmergencyVoiceCallCapable;
@property (T@"NSString",&,N,V_emergencyOrRoadsideSessionInitiatedBy) emergencyOrRoadsideSessionInitiatedBy;
```

## Class methods

```
+[CTConnectionAssistantState supportsSecureCoding];
```

## Instance methods

```
-[CTConnectionAssistantState connectionState];
-[CTConnectionAssistantState setEmergencyOrRoadsideSessionInitiatedBy:];
-[CTConnectionAssistantState setIsEmergencyVoiceCallCapable:];
-[CTConnectionAssistantState setServiceIntervals:];
-[CTConnectionAssistantState setLocationState:];
-[CTConnectionAssistantState setConversationState:];
-[CTConnectionAssistantState backupTargets];
-[CTConnectionAssistantState roadsideConversationState];
-[CTConnectionAssistantState setConnectionClosedState:];
-[CTConnectionAssistantState locationState];
-[CTConnectionAssistantState setConnectionState:];
-[CTConnectionAssistantState setCurrentTarget:];
-[CTConnectionAssistantState isEmergencyVoiceCallCapable];
-[CTConnectionAssistantState version];
-[CTConnectionAssistantState servicePartners];
-[CTConnectionAssistantState internetInterface];
-[CTConnectionAssistantState setIso3166Alpha3CountryCode:];
-[CTConnectionAssistantState connectionClosedState];
-[CTConnectionAssistantState conversationState];
-[CTConnectionAssistantState setServicePartners:];
-[CTConnectionAssistantState setSilenceInterval:];
-[CTConnectionAssistantState encodeWithCoder:];
-[CTConnectionAssistantState targetVisibility];
-[CTConnectionAssistantState silenceInterval];
-[CTConnectionAssistantState iso3166Alpha3CountryCode];
-[CTConnectionAssistantState description];
-[CTConnectionAssistantState setRoadsideConversationState:];
-[CTConnectionAssistantState initWithCoder:];
-[CTConnectionAssistantState currentTarget];
-[CTConnectionAssistantState setTargetVisibility:];
-[CTConnectionAssistantState stewieState];
-[CTConnectionAssistantState setVersion:];
-[CTConnectionAssistantState setBackupTargets:];
-[CTConnectionAssistantState setStewieState:];
-[CTConnectionAssistantState copyWithZone:];
-[CTConnectionAssistantState tryOutState];
-[CTConnectionAssistantState emergencyOrRoadsideSessionInitiatedBy];
-[CTConnectionAssistantState setTryOutState:];
-[CTConnectionAssistantState setInternetInterface:];
-[CTConnectionAssistantState serviceIntervals];
```
