Thanks for using this :)

# Courser Fix

You will need to execute this script in your roblox exploit (Fluxus recommended, idk if it works in other crap):
```lua
local function isFirstPerson()
	local camera = workspace.CurrentCamera
	local character = game:GetService("Players").LocalPlayer.Character or game:GetService("Players").LocalPlayer.CharacterAdded
	if (character.Head.CFrame.p - camera.CFrame.p).magnitude < 1 then
		return true
	else
		return false
	end
end

while wait(0.3) do
	local isFirstPerson = isFirstPerson()
	
	if isFirstPerson == true then
    	writefile("CamFix.txt", "true\n" .. tostring(workspace.CurrentCamera.ViewportSize.X / 2) .. " " .. tostring(workspace.CurrentCamera.ViewportSize.Y / 2))
    else
		writefile("CamFix.txt", "false")
	end
end
```

once you have executed the script, make sure you move the CamFix.exe into the workspace folder from Fluxus, then execute it.
## This can trigger antiviruses, but it is completely secure! If you dont trust, execute the CamFix.py (cuz you can see source then)
But you need python 3 installed for it

well thats it actually..

So simply:
1. Move the CamFix.exe into workspace folder of your exploit
2. Execute CamFix.exe
3. Execute CamFix.lua in your exploit
4. Just play like always, but without courser moving out of screen

# Warning:
## If you close roblox in first person, press F10 to disable the Fix, or else your courser gets stuck lol
## May not work for every game