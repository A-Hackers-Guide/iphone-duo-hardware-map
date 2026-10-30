# `LACUserServiceXPC` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 39 instance methods, 0 class methods

## Instance methods

```
-[LACUserServiceXPC changePasswordForUser:to:reply:];
-[LACUserServiceXPC updateUserRegistryConfig:reply:];
-[LACUserServiceXPC addRecoveryKey:authorizer:reply:];
-[LACUserServiceXPC addRecoveryKey:authorizerKey:reply:];
-[LACUserServiceXPC addRecoveryKey:reply:];
-[LACUserServiceXPC authenticateUser:domain:targetDisk:contextRef:reply:];
-[LACUserServiceXPC authenticateUser:domain:targetDisk:reply:];
-[LACUserServiceXPC authenticateUser:targetDisk:contextRef:reply:];
-[LACUserServiceXPC authenticateUser:targetDisk:reply:];
-[LACUserServiceXPC checkExistsOTIForUserWithUUID:targetDisk:reply:];
-[LACUserServiceXPC checkExistsUserWithUUID:targetDisk:reply:];
-[LACUserServiceXPC checkOwnershipStatusForTargetDisk:reply:];
-[LACUserServiceXPC createUser:authorizer:reply:];
-[LACUserServiceXPC createUser:recoveryCredential:reply:];
-[LACUserServiceXPC createUser:reply:];
-[LACUserServiceXPC createUserWithKeybag:canObtainOTI:reply:];
-[LACUserServiceXPC createUserWithKeybagHash:canObtainOTI:reply:];
-[LACUserServiceXPC deletePasswordHintForUserWithUUID:reply:];
-[LACUserServiceXPC deleteUserWithUUID:reply:];
-[LACUserServiceXPC fetchPasswordHintForUserWithUUID:reply:];
-[LACUserServiceXPC fetchRecoveryKeysInTargetDisk:reply:];
-[LACUserServiceXPC fetchUIDForUserWithUUID:reply:];
-[LACUserServiceXPC fetchUsersInTargetDisk:reply:];
-[LACUserServiceXPC lockSessionID:reply:];
-[LACUserServiceXPC lockStateForUserWithUUID:sessionID:reply:];
-[LACUserServiceXPC lockoutStateForUserWithUUID:domain:reply:];
-[LACUserServiceXPC lockoutStateForUserWithUUID:reply:];
-[LACUserServiceXPC loginUser:sessionID:targetDisk:reply:];
-[LACUserServiceXPC logoutSessionID:reply:];
-[LACUserServiceXPC removeRecoveryKey:externalDataUUID:reply:];
-[LACUserServiceXPC resetAllPasswords:targetDisk:reply:];
-[LACUserServiceXPC resetPasswordForUser:authorizer:targetDisk:reply:];
-[LACUserServiceXPC resetPasswordForUser:recoveryCredential:reply:];
-[LACUserServiceXPC resetPasswordForUser:recoveryCredential:targetDisk:reply:];
-[LACUserServiceXPC resetPasswordWithHashForUser:reply:];
-[LACUserServiceXPC storePasswordHintForUserWithUUID:passwordHint:reply:];
-[LACUserServiceXPC transferOwnershipFromUser:toExistingUser:targetDisk:reply:];
-[LACUserServiceXPC transferOwnershipFromUser:toNewRecoveryKey:targetDisk:reply:];
-[LACUserServiceXPC unlockUser:sessionID:reply:];
```
