# `LACACMHelper`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACACMHelper`
- 4 instance variables, 8 properties, 37 instance methods, 18 class methods

## Instance variables

```
q _ownership;
I _acmTrackingNumber;
^{__ACMHandle=} _acmContext;
@"<LACACMRequirementTransformer>" _requirementTransformer;
```

## Properties

```
@property (T^{__ACMHandle=},N,V_acmContext) acmContext;
@property (TI,R,N,V_acmTrackingNumber) acmTrackingNumber;
@property (T@"NSData",R,N) externalizedContext;
@property (T@"<LACACMRequirementTransformer>",&,N,V_requirementTransformer) requirementTransformer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACACMHelper catacombUUID:];
+[LACACMHelper _errorCodeFromACMStatus:];
+[LACACMHelper acmPolicyForPolicy:];
+[LACACMHelper boolEnvironmentVariable:];
+[LACACMHelper createContext:];
+[LACACMHelper createContextWithExternalForm:];
+[LACACMHelper createContextWithFlags:contextRef:];
+[LACACMHelper createPreboardBatchControl];
+[LACACMHelper createUPPControlForTeamID:];
+[LACACMHelper decodeData:seed:externalizedContext:error:];
+[LACACMHelper encodeData:seed:externalizedContext:error:];
+[LACACMHelper notifyBiometricMatchOperationStartAttempted];
+[LACACMHelper ratchetStatusWithConfig:];
+[LACACMHelper requirement:dataProperty:];
+[LACACMHelper requirement:hasFlag:andType:];
+[LACACMHelper requirement:hasState:andType:];
+[LACACMHelper requirement:uint32Property:];
+[LACACMHelper resetRatchet:];
```

## Instance methods

```
-[LACACMHelper clear];
-[LACACMHelper init];
-[LACACMHelper dealloc];
-[LACACMHelper initWithExternalizedContext:];
-[LACACMHelper externalizedContext];
-[LACACMHelper _verifyRequirement:satisfiedForType:present:flags:];
-[LACACMHelper acmContext];
-[LACACMHelper acmTrackingNumber];
-[LACACMHelper addCredential:scope:error:];
-[LACACMHelper addCredential:scope:property:data:error:];
-[LACACMHelper ageForDataWithType:error:];
-[LACACMHelper dataWithType:encoded:error:];
-[LACACMHelper dataWithType:error:];
-[LACACMHelper exchangeControlData:error:];
-[LACACMHelper hasDataWithType:error:];
-[LACACMHelper initWithACMContext:];
-[LACACMHelper isCredentialOfTypeSet:error:];
-[LACACMHelper missingACMContextError];
-[LACACMHelper performContextBlock:error:];
-[LACACMHelper performContextVerificationWithParameters:block:completion:];
-[LACACMHelper performCredentialBlock:credentialType:error:];
-[LACACMHelper performDataContextBlock:error:];
-[LACACMHelper performNumberContextBlock:error:];
-[LACACMHelper preflightPolicy:parameters:maxGlobalCredentialAge:processRequirement:];
-[LACACMHelper removeCredentialsOfType:error:];
-[LACACMHelper replacePassphraseCredentialWithPurpose:passphrase:scope:error:];
-[LACACMHelper requirementTransformer];
-[LACACMHelper setAcmContext:];
-[LACACMHelper setData:type:encoded:error:];
-[LACACMHelper setData:type:error:];
-[LACACMHelper setRequirementTransformer:];
-[LACACMHelper setSecretForPasscodeStash:error:];
-[LACACMHelper setVariable:value:error:];
-[LACACMHelper verifyAclConstraint:operation:preflight:parameters:maxGlobalCredentialAge:processRequirement:];
-[LACACMHelper verifyPolicy:preflight:parameters:maxGlobalCredentialAge:processRequirement:];
-[LACACMHelper verifyRequirementOfType:policy:error:];
-[LACACMHelper verifyRequirementOfType:policy:mustBePresent:parameters:flags:error:];
```
