# `ANConnectionAttempt`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 11 properties, 30 instance methods, 0 class methods

## Instance variables

```
Q _startTime;
I _usecase;
i _failureCode;
@"NSUUID" _identifier;
@"ANConnectionAttemptRequestContext" _requestContext;
Q _connectionAttemptCount;
@"NSMutableArray" _krMaterials;
@"NSString" _outcome;
@"NSMutableDictionary" _allMaterials;
@"NSMutableDictionary" _pendingMaterials;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_allMaterials) allMaterials;
@property (T@"NSMutableDictionary",&,V_pendingMaterials) pendingMaterials;
@property (T@"NSUUID",R,V_identifier) identifier;
@property (Tq,R) state;
@property (T@"ANConnectionAttemptRequestContext",R,V_requestContext) requestContext;
@property (TQ,V_connectionAttemptCount) connectionAttemptCount;
@property (T@"NSMutableArray",&,V_krMaterials) krMaterials;
@property (TI,V_usecase) usecase;
@property (Ti,R,V_failureCode) failureCode;
@property (T@"NSString",R,V_outcome) outcome;
@property (T@"NSArray",R,N) possiblePeripherals;
```

## Instance methods

```
-[ANConnectionAttempt identifier];
-[ANConnectionAttempt dealloc];
-[ANConnectionAttempt outcome];
-[ANConnectionAttempt state];
-[ANConnectionAttempt requestContext];
-[ANConnectionAttempt usecase];
-[ANConnectionAttempt initWithRequestContext:];
-[ANConnectionAttempt failureCode];
-[ANConnectionAttempt setUsecase:];
-[ANConnectionAttempt attemptDuration];
-[ANConnectionAttempt setKrMaterials:];
-[ANConnectionAttempt addPossiblePeripheral:withConnectionMaterial:];
-[ANConnectionAttempt allMaterials];
-[ANConnectionAttempt connectionAttemptCount];
-[ANConnectionAttempt connectionMaterialsForPeripheral:];
-[ANConnectionAttempt doesPeripheral:haveAddress:];
-[ANConnectionAttempt getAttemptFailureString];
-[ANConnectionAttempt hasConnectionMaterialForPeripheral:];
-[ANConnectionAttempt inertCopy];
-[ANConnectionAttempt krMaterials];
-[ANConnectionAttempt nextConnectionMaterialForPeripheral:];
-[ANConnectionAttempt pendingMaterials];
-[ANConnectionAttempt popConnectionMaterialForPeripheral:];
-[ANConnectionAttempt possiblePeripherals];
-[ANConnectionAttempt removePossiblePeripheral:];
-[ANConnectionAttempt setAllMaterials:];
-[ANConnectionAttempt setBluetoothPeripheralFailureCode:];
-[ANConnectionAttempt setConnectionAttemptCount:];
-[ANConnectionAttempt setLocationPeripheralFailureCode:];
-[ANConnectionAttempt setPendingMaterials:];
```
