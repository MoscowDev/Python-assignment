import java.util.Scanner;

public class Four{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int myCollections = 20;

        while (myCollections != 0) {
            String menu = """
                1-> Phonebook
                2-> Messages
                3-> Chat
                4-> Call Register
                5-> Tones
                6-> Settings
                7-> Call Divert
                8-> Games
                9-> Calculator
                10-> Reminders
                11-> Clock
                12-> Profiles
                13-> SIM services
                0-> Exit
                """;

            System.out.print(menu);
            myCollections = scanner.nextInt();

            switch (myCollections) {
                case 1 -> {
                    System.out.println("Phonebook");
                    int phonebookSelect = 20;
                    while (phonebookSelect != 0) {
                        String phonebookMenu = """
                            1-> Search
                            2-> Service Nos
                            3-> Add Name
                            4-> Erase
                            5-> Edit
                            6-> Assign Tone
                            7-> Send b'card
                            8-> Options
                            9-> Speed Dials
                            10-> Voice Tags
                            0-> Back
                            """;

                        System.out.print(phonebookMenu);
                        phonebookSelect = scanner.nextInt();

                        switch (phonebookSelect) {
                            case 1 -> {System.out.println("Search");}
                            case 2 -> {System.out.println("Service Nos");}
                            case 3 -> {System.out.println("Add Name");}
                            case 4 -> {System.out.println("Erase");}
                            case 5 -> {System.out.println("Edit");}
                            case 6 -> {System.out.println("Assign Tone");}
                            case 7 -> {System.out.println("Send b'card");}
                            case 8 -> {
                                System.out.println("Options");
                                int optionSelect = 20;
                                while (optionSelect != 0) {
                                    String optionMenu = """
                                        1-> Type of view
                                        2-> Memory status
                                        0-> Back
                                        """;
                                    System.out.print(optionMenu);
                                    optionSelect = scanner.nextInt();
                                    switch (optionSelect) {
                                        case 1 -> {System.out.println("Type of view");}
                                        case 2 -> {System.out.println("Memory status");}
                                        case 0 -> {System.out.println("Back");}
                                        default -> {System.out.println("Invalid");}
                                    }
                                }
                            }
                            case 9 -> {System.out.println("Speed Dials");}
                            case 10 -> {System.out.println("Voice Tags");}
                            case 0 -> {System.out.println("Back");}
                            default -> {System.out.println("Invalid");}
                        }
                    }
                }

                case 2 -> {
                    System.out.println("Messages");
                    int messageSelect = 20;
                    while (messageSelect != 0) {
                        String messageMenu = """
                            1-> Write message
                            2-> Inbox
                            3-> Outbox
                            4-> Picture messages
                            5-> Templates
                            6-> Smileys
                            7-> Message settings
                            8-> Info service
                            9-> Voice mailbox number
                            10-> Service command editor
                            0-> Back
                            """;
                        System.out.print(messageMenu);
                        messageSelect = scanner.nextInt();

                        switch (messageSelect) {
                            case 1 -> {
                                System.out.println("Write a message");
                                int writeSelect = 20;
                                while (writeSelect != 0) {
                                    String writeMenu = """
                                        1-> Nothing to enter
                                        0-> Back
                                        """;
                                    System.out.print(writeMenu);
                                    writeSelect = scanner.nextInt();
                                    switch (writeSelect) {
                                        case 1 -> {System.out.println("Nothing to enter");}
                                        case 0 -> {System.out.println("Back");}
                                        default -> {System.out.println("Invalid");}
                                    }
                                }
                            }
                            case 2 -> {System.out.println("Check inbox");}
                            case 3 -> {System.out.println("Check outbox");}
                            case 4 -> {System.out.println("Picture messages");}
                            case 5 -> {System.out.println("Templates");}
                            case 6 -> {System.out.println("Smileys");}
                            case 7 -> {
                                System.out.println("Message settings");
                                int settingSelect = 20;
                                while (settingSelect != 0) {
                                    String settingMenu = """
                                        1-> Set
                                        2-> Common
                                        0-> Back
                                        """;
                                    System.out.print(settingMenu);
                                    settingSelect = scanner.nextInt();
                                    switch (settingSelect) {
                                        case 1 -> {
                                            System.out.println("Set");
                                            int setSelect = 20;
                                            while (setSelect != 0) {
                                                String setMenu = """
                                                    1-> Message centre number
                                                    2-> Message sent as
                                                    3-> Message validity
                                                    0-> Back
                                                    """;
                                                System.out.print(setMenu);
                                                setSelect = scanner.nextInt();
                                                switch (setSelect) {
                                                    case 1 -> {System.out.println("Message centre number");}
                                                    case 2 -> {System.out.println("Message sent as");}
                                                    case 3 -> {System.out.println("Message validity");}
                                                    case 0 -> {System.out.println("Back");}
                                                    default -> {System.out.println("Invalid");}
                                                }
                                            }
                                        }
                                        case 2 -> {
                                            System.out.println("Common");
                                            int commonSelect = 20;
                                            while (commonSelect != 0) {
                                                String commonMenu = """
                                                    1-> Delivery reports
                                                    2-> Reply via same centre
                                                    3-> Character support
                                                    0-> Back
                                                    """;
                                                System.out.print(commonMenu);
                                                commonSelect = scanner.nextInt();
                                                switch (commonSelect) {
                                                    case 1 -> {System.out.println("Delivery reports");}
                                                    case 2 -> {System.out.println("Reply via same centre");}
                                                    case 3 -> {System.out.println("Character support");}
                                                    case 0 -> {System.out.println("Back");}
                                                    default -> {System.out.println("Invalid");}
                                                }
                                            }
                                        }
                                        case 0 -> {System.out.println("Back");}
                                        default -> {System.out.println("Invalid");}
                                    }
                                }
                            }
                            case 8 -> {System.out.println("Check out service info");}
                            case 9 -> {System.out.println("Voice mailbox number");}
                            case 10 -> {System.out.println("Service command editor");}
                            case 0 -> {System.out.println("Back");}
                            default -> {System.out.println("Invalid");}
                        }
                    }
                }

                case 3 -> {
                    System.out.println("Chat");
                    int chatSelect = 20;
                    while (chatSelect != 0) {
                        String chatMenu = """
                            1-> Chat
                            0-> Back
                            """;
                        System.out.print(chatMenu);
                        chatSelect = scanner.nextInt();
                        switch (chatSelect) {
                            case 1 -> {System.out.println("Chat");}
                            case 0 -> {System.out.println("Back");}
                            default -> {System.out.println("Invalid");}
                        }
                    }
                }

                case 4 -> {System.out.println("Call Register");}
                case 5 -> {System.out.println("Tones");}
                case 6 -> {System.out.println("Settings");}
                case 7 -> {System.out.println("Call Divert");}
                case 8 -> {System.out.println("Games");}
                case 9 -> {System.out.println("Calculator");}
                case 10 -> {System.out.println("Reminders");}
                case 11 -> {System.out.println("Clock");}
                case 12 -> {System.out.println("Profiles");}
                case 13 -> {System.out.println("SIM services");}
                case 0 -> {System.out.println("Exit");}
                default -> {System.out.println("Invalid");}
            }
        }
    }
}
