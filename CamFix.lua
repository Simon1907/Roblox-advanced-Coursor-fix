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
