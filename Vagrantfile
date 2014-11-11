# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "kaedroho/wagtail-base"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.provision :shell, :path => "vagrant/provision.sh", :args => "{{ project_name }}"

  if File.exist? "Vagrantfile.local"
    instance_eval File.read("Vagrantfile.local"), "Vagrantfile.local"
  end
end
